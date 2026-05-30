"""
Evaluation module for FAQ chatbot
Tests chatbot performance on various query types
"""

import pandas as pd
from chatbot import FAQChatbot
import time


class ChatbotEvaluator:
    """Evaluates chatbot performance on test queries"""
    
    def __init__(self, chatbot, test_queries_file):
        """
        Initialize evaluator
        
        Args:
            chatbot: FAQChatbot instance
            test_queries_file: Path to test queries CSV
        """
        self.chatbot = chatbot
        self.test_df = pd.read_csv(test_queries_file)
    
    def evaluate(self, verbose=True):
        """
        Run evaluation on all test queries
        
        Args:
            verbose: Whether to print detailed results
            
        Returns:
            Dictionary with evaluation metrics
        """
        results = []
        
        print("=" * 80)
        print("CHATBOT EVALUATION")
        print("=" * 80)
        print(f"Testing {len(self.test_df)} queries...\n")
        
        for idx, row in self.test_df.iterrows():
            query = row['query']
            expected_category = row['expected_category']
            query_type = row['query_type']
            
            # Get chatbot response
            start_time = time.time()
            response = self.chatbot.get_response(query)
            response_time = time.time() - start_time
            
            # Check if category matches
            category_match = response['category'] == expected_category if response['category'] else False
            
            # Store result
            result = {
                'query': query,
                'expected_category': expected_category,
                'query_type': query_type,
                'matched_question': response['matched_question'],
                'answer': response['answer'],
                'similarity_score': response['similarity_score'],
                'confidence': response['confidence'],
                'category_match': category_match,
                'response_time': response_time
            }
            results.append(result)
            
            # Print if verbose
            if verbose:
                print(f"Query #{idx + 1}: {query}")
                print(f"Type: {query_type} | Expected Category: {expected_category}")
                print(f"Similarity: {response['similarity_score']:.3f} | Confidence: {response['confidence']}")
                print(f"Category Match: {'✓' if category_match else '✗'}")
                if response['matched_question']:
                    print(f"Matched: {response['matched_question']}")
                print(f"Answer: {response['answer'][:100]}...")
                print("-" * 80)
                print()
        
        # Calculate metrics
        results_df = pd.DataFrame(results)
        
        metrics = {
            'total_queries': len(results_df),
            'high_confidence': len(results_df[results_df['confidence'] == 'high']),
            'medium_confidence': len(results_df[results_df['confidence'] == 'medium']),
            'low_confidence': len(results_df[results_df['confidence'] == 'low']),
            'category_accuracy': results_df['category_match'].sum() / len(results_df) * 100,
            'avg_similarity': results_df['similarity_score'].mean(),
            'avg_response_time': results_df['response_time'].mean(),
            'by_query_type': results_df.groupby('query_type').agg({
                'similarity_score': 'mean',
                'category_match': 'sum'
            }).to_dict()
        }
        
        # Print summary
        print("=" * 80)
        print("EVALUATION SUMMARY")
        print("=" * 80)
        print(f"Total Queries: {metrics['total_queries']}")
        print(f"High Confidence: {metrics['high_confidence']} ({metrics['high_confidence']/metrics['total_queries']*100:.1f}%)")
        print(f"Medium Confidence: {metrics['medium_confidence']} ({metrics['medium_confidence']/metrics['total_queries']*100:.1f}%)")
        print(f"Low Confidence: {metrics['low_confidence']} ({metrics['low_confidence']/metrics['total_queries']*100:.1f}%)")
        print(f"Category Accuracy: {metrics['category_accuracy']:.1f}%")
        print(f"Average Similarity Score: {metrics['avg_similarity']:.3f}")
        print(f"Average Response Time: {metrics['avg_response_time']*1000:.2f}ms")
        print("\nPerformance by Query Type:")
        for query_type, stats in metrics['by_query_type']['similarity_score'].items():
            print(f"  {query_type}: Avg Similarity = {stats:.3f}")
        print("=" * 80)
        
        return metrics, results_df
    
    def analyze_failures(self, results_df, threshold=0.6):
        """
        Analyze queries with low similarity scores
        
        Args:
            results_df: DataFrame with evaluation results
            threshold: Similarity threshold for failure analysis
        """
        failures = results_df[results_df['similarity_score'] < threshold]
        
        if len(failures) == 0:
            print("\nNo failures found (all queries above threshold)")
            return
        
        print("\n" + "=" * 80)
        print(f"FAILURE ANALYSIS (Similarity < {threshold})")
        print("=" * 80)
        print(f"Found {len(failures)} queries below threshold\n")
        
        for idx, row in failures.iterrows():
            print(f"Query: {row['query']}")
            print(f"Type: {row['query_type']}")
            print(f"Similarity: {row['similarity_score']:.3f}")
            print(f"Expected Category: {row['expected_category']}")
            if row['matched_question']:
                print(f"Matched: {row['matched_question']}")
            print("-" * 80)
            print()


def main():
    """Main evaluation function"""
    # Initialize chatbot
    print("Initializing chatbot...\n")
    chatbot = FAQChatbot(
        faq_file='data/faqs.csv',
        model_name='all-MiniLM-L6-v2',
        confidence_threshold=0.5
    )
    
    # Initialize evaluator
    evaluator = ChatbotEvaluator(chatbot, 'tests/test_queries.csv')
    
    # Run evaluation
    metrics, results_df = evaluator.evaluate(verbose=True)
    
    # Analyze failures
    evaluator.analyze_failures(results_df, threshold=0.6)
    
    # Save results
    results_df.to_csv('tests/evaluation_results.csv', index=False)
    print("\nResults saved to tests/evaluation_results.csv")


if __name__ == "__main__":
    main()
