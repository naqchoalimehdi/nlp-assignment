"""
Quick test script for the FAQ chatbot
"""
import sys
sys.path.insert(0, 'src')

from chatbot import FAQChatbot

print("Initializing chatbot...")
chatbot = FAQChatbot(
    faq_file='data/faqs.csv',
    model_name='all-MiniLM-L6-v2',
    confidence_threshold=0.5
)

print("\n" + "="*60)
print("Testing chatbot with sample queries")
print("="*60 + "\n")

# Test queries
test_queries = [
    "How do I apply for admission?",
    "What are the fees?",
    "Do you have hostel facilities?",
    "What is the minimum GPA required?"
]

for query in test_queries:
    print(f"Query: {query}")
    response = chatbot.get_response(query)
    print(f"Answer: {response['answer'][:100]}...")
    print(f"Similarity: {response['similarity_score']:.3f} | Confidence: {response['confidence']}")
    print("-" * 60)
    print()

print("✓ Chatbot test completed successfully!")
