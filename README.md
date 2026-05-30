# FAQ Chatbot - University Admissions

A retrieval-based FAQ chatbot using sentence embeddings for semantic similarity matching. The chatbot answers questions about university admissions, programs, fees, campus facilities, and academic policies.

## Features

- **Semantic Similarity**: Uses sentence-transformers (all-MiniLM-L6-v2) for understanding query intent
- **Confidence Scoring**: Returns answers only when similarity exceeds threshold
- **50+ FAQ Entries**: Comprehensive dataset covering university-related queries
- **Text Preprocessing**: Handles spelling errors, paraphrasing, and informal language
- **Evaluation Framework**: Automated testing with 20 test queries

## Project Structure

```
project/
├── data/
│   └── faqs.csv                    # FAQ dataset (50+ Q&A pairs)
├── src/
│   ├── chatbot.py                  # Main chatbot logic
│   ├── preprocessing.py            # Text preprocessing utilities
│   └── evaluation.py               # Evaluation and testing
├── tests/
│   ├── test_queries.csv            # Test queries for evaluation
│   └── evaluation_results.csv      # Generated evaluation results
├── requirements.txt                # Python dependencies
├── README.md                       # This file
└── task.md                         # Assignment requirements
```

## Installation

1. **Install Python dependencies**:
```bash
pip install -r requirements.txt
```

2. **Download NLTK data** (automatic on first run):
The chatbot will automatically download required NLTK data (punkt, stopwords, wordnet) on first execution.

## Usage

### Interactive Chat Mode

Run the chatbot in interactive mode:

```bash
cd src
python chatbot.py
```

Example interaction:
```
You: How do I apply for admission?
Chatbot: You can apply online through our university portal...
[Confidence: HIGH | Similarity: 0.892]
```

### Evaluation Mode

Run automated evaluation on test queries:

```bash
cd src
python evaluation.py
```

This will:
- Test 20 different query types (exact matches, paraphrases, spelling errors)
- Calculate accuracy and similarity metrics
- Analyze failure cases
- Save results to `tests/evaluation_results.csv`

### Programmatic Usage

```python
from src.chatbot import FAQChatbot

# Initialize chatbot
chatbot = FAQChatbot(
    faq_file='data/faqs.csv',
    confidence_threshold=0.5
)

# Get response
response = chatbot.get_response("What are the admission requirements?")
print(response['answer'])
print(f"Similarity: {response['similarity_score']:.3f}")
```

## Technical Details

### Text Representation
- **Model**: all-MiniLM-L6-v2 (sentence-transformers)
- **Embedding Dimension**: 384
- **Similarity Metric**: Cosine similarity

### Preprocessing Pipeline
1. Lowercase conversion
2. URL and email removal
3. Special character cleaning
4. Light preprocessing (preserves sentence structure for embeddings)

### Confidence Levels
- **High**: Similarity > 0.7
- **Medium**: Similarity 0.5 - 0.7
- **Low**: Similarity < 0.5 (fallback response)

## Dataset

The FAQ dataset (`data/faqs.csv`) contains 50 question-answer pairs across 6 categories:
- **Admissions** (10 FAQs): Requirements, deadlines, application process
- **Programs** (5 FAQs): Available programs, duration, credit transfer
- **Fees** (5 FAQs): Fee structure, payment plans, financial aid
- **Campus** (10 FAQs): Location, facilities, hostel, security
- **Academic** (10 FAQs): Grading, attendance, registration, exams
- **Contact** (8 FAQs): Office hours, helpline, support contacts
- **International** (2 FAQs): International student requirements

## Evaluation Results

The chatbot is tested on 20 queries including:
- Exact matches from FAQ
- Paraphrased questions
- Spelling errors
- Informal language
- Abbreviations

Expected performance:
- Category Accuracy: >85%
- Average Similarity: >0.75
- High Confidence Rate: >70%

## Dependencies

- **pandas**: Dataset handling
- **sentence-transformers**: Sentence embeddings
- **scikit-learn**: Cosine similarity computation
- **nltk**: Text preprocessing
- **numpy**: Numerical operations

## Limitations

1. **Domain-Specific**: Only answers university admission-related questions
2. **Static Knowledge**: Cannot answer questions outside the FAQ dataset
3. **No Context Memory**: Each query is independent (no conversation history)
4. **Embedding Quality**: Performance depends on semantic similarity model
5. **Threshold Sensitivity**: May reject valid queries if similarity is low

## Future Improvements

- Add conversation context/history
- Implement multi-turn dialogue
- Expand FAQ dataset
- Add intent classification
- Support multiple languages
- Integrate with live database

## License

This project is created for academic purposes as part of an NLP course assignment.

## Authors

[Add your names and roll numbers here]

## Acknowledgments

- Sentence-Transformers library by UKPLab
- NLTK for text preprocessing utilities
- scikit-learn for similarity computation
