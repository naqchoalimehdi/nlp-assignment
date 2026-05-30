"""
FAQ Chatbot using Sentence Embeddings
Main chatbot logic for semantic similarity-based retrieval
"""

import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from preprocessing import TextPreprocessor


class FAQChatbot:
    """Retrieval-based FAQ chatbot using sentence embeddings"""
    
    def __init__(self, faq_file, model_name='all-MiniLM-L6-v2', confidence_threshold=0.5):
        """
        Initialize chatbot
        
        Args:
            faq_file: Path to FAQ CSV file
            model_name: Sentence transformer model name
            confidence_threshold: Minimum similarity score to return answer
        """
        self.confidence_threshold = confidence_threshold
        self.preprocessor = TextPreprocessor(remove_stopwords=False, use_lemmatization=False)
        
        # Load FAQ data
        print("Loading FAQ dataset...")
        self.faq_df = pd.read_csv(faq_file, encoding='utf-8')
        print(f"Loaded {len(self.faq_df)} FAQ entries")
        
        # Load sentence transformer model
        print(f"Loading sentence transformer model: {model_name}...")
        self.model = SentenceTransformer(model_name)
        print("Model loaded successfully")
        
        # Preprocess and encode FAQ questions
        print("Encoding FAQ questions...")
        self.faq_questions = self.faq_df['question'].tolist()
        self.faq_answers = self.faq_df['answer'].tolist()
        self.faq_categories = self.faq_df['category'].tolist() if 'category' in self.faq_df.columns else None
        
        # Preprocess questions (light preprocessing for embeddings)
        preprocessed_questions = [self.preprocessor.preprocess_light(q) for q in self.faq_questions]
        
        # Generate embeddings for all FAQ questions
        self.faq_embeddings = self.model.encode(preprocessed_questions, show_progress_bar=True)
        print("FAQ questions encoded successfully\n")
    
    def get_response(self, user_query):
        """
        Get chatbot response for user query
        
        Args:
            user_query: User's question
            
        Returns:
            Dictionary containing answer, similarity score, and matched question
        """
        # Preprocess user query
        preprocessed_query = self.preprocessor.preprocess_light(user_query)
        
        # Encode user query
        query_embedding = self.model.encode([preprocessed_query])
        
        # Compute cosine similarity with all FAQ questions
        similarities = cosine_similarity(query_embedding, self.faq_embeddings)[0]
        
        # Get best match
        best_match_idx = np.argmax(similarities)
        best_similarity = similarities[best_match_idx]
        
        # Check confidence threshold
        if best_similarity < self.confidence_threshold:
            return {
                'answer': "Sorry, I could not find a reliable answer to your question. Please try rephrasing or contact our support team.",
                'similarity_score': float(best_similarity),
                'matched_question': None,
                'category': None,
                'confidence': 'low'
            }
        
        # Return matched answer
        return {
            'answer': self.faq_answers[best_match_idx],
            'similarity_score': float(best_similarity),
            'matched_question': self.faq_questions[best_match_idx],
            'category': self.faq_categories[best_match_idx] if self.faq_categories else None,
            'confidence': 'high' if best_similarity > 0.7 else 'medium'
        }
    
    def get_top_k_responses(self, user_query, k=3):
        """
        Get top K most similar FAQ responses
        
        Args:
            user_query: User's question
            k: Number of top results to return
            
        Returns:
            List of dictionaries with top K matches
        """
        # Preprocess user query
        preprocessed_query = self.preprocessor.preprocess_light(user_query)
        
        # Encode user query
        query_embedding = self.model.encode([preprocessed_query])
        
        # Compute cosine similarity
        similarities = cosine_similarity(query_embedding, self.faq_embeddings)[0]
        
        # Get top K matches
        top_k_indices = np.argsort(similarities)[-k:][::-1]
        
        results = []
        for idx in top_k_indices:
            results.append({
                'question': self.faq_questions[idx],
                'answer': self.faq_answers[idx],
                'similarity_score': float(similarities[idx]),
                'category': self.faq_categories[idx] if self.faq_categories else None
            })
        
        return results
    
    def chat(self):
        """Interactive chat interface"""
        print("=" * 60)
        print("FAQ Chatbot - University Admissions")
        print("=" * 60)
        print("Ask me anything about university admissions!")
        print("Type 'quit' or 'exit' to end the conversation.\n")
        
        while True:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("\nChatbot: Thank you for using the FAQ chatbot. Goodbye!")
                break
            
            # Get response
            response = self.get_response(user_input)
            
            # Display response
            print(f"\nChatbot: {response['answer']}")
            print(f"[Confidence: {response['confidence'].upper()} | Similarity: {response['similarity_score']:.3f}]")
            
            if response['matched_question']:
                print(f"[Matched FAQ: {response['matched_question']}]")
            
            print()


def main():
    """Main function to run the chatbot"""
    # Initialize chatbot
    chatbot = FAQChatbot(
        faq_file='data/faqs_clean.csv',
        model_name='all-MiniLM-L6-v2',
        confidence_threshold=0.5
    )
    
    # Start interactive chat
    chatbot.chat()


if __name__ == "__main__":
    main()
