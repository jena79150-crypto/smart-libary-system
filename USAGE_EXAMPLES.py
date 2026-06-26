"""
USAGE EXAMPLES - Smart Library Assistant
Demonstrates how to use each module programmatically
"""

# ===========================================================================
# Example 1: Loading and Searching Books
# ===========================================================================

from src.database import BooksDatabase
from src.search import BookSearch

# Initialize database
db = BooksDatabase()

# Initialize search
search = BookSearch(db)

# Search by title
print("=== SEARCH BY TITLE ===")
results = search.search_by_title("Harry Potter", limit=5)
print(search.format_search_results(results))

# Search by author
print("=== SEARCH BY AUTHOR ===")
results = search.search_by_author("J.K. Rowling", limit=3)
print(search.format_search_results(results))

# Combined search
print("=== COMBINED SEARCH ===")
results = search.search_combined("The Great Gatsby", limit=5)
print(search.format_search_results(results))


# ===========================================================================
# Example 2: Natural Language Processing (NLP)
# ===========================================================================

from src.nlp import BookNLP

# Initialize NLP
nlp = BookNLP(db)

# Ask a question
question = "What is the rating of Harry Potter and the Philosopher's Stone?"
answer = nlp.process_question_about_book(question)
print(f"Q: {question}")
print(f"A: {answer}\n")

# Extract question type
question_type = nlp.extract_question_type("Who wrote The Great Gatsby?")
print(f"Question type: {question_type}\n")

# Extract book title from question
title = nlp.extract_book_title("Tell me about 'To Kill a Mockingbird'")
print(f"Extracted title: {title}\n")


# ===========================================================================
# Example 3: Retrieval Augmented Generation (RAG)
# ===========================================================================

from src.rag import BookRAG

# Initialize RAG
rag = BookRAG(db)

# Answer question using RAG
question = "What is the rating of The Hobbit?"
result = rag.answer_question(question)

print("=== RAG ANSWER ===")
print(f"Question: {question}")
print(f"Answer:\n{result['answer']}")
print(f"Confidence: {result['confidence']:.2%}")
print(f"Sources: {result['sources']}\n")

# Ask about specific book
answer = rag.ask_about_book("1984", "When was it published?")
print(f"Answer: {answer}\n")


# ===========================================================================
# Example 4: Machine Learning - Demand Prediction
# ===========================================================================

from src.ml import DemandPredictor

# Initialize predictor
predictor = DemandPredictor(db)

# Get a book to predict
results = search.search_by_title("Harry Potter", limit=1)
if results:
    book = results[0]
    
    # Predict demand
    prediction = predictor.predict_demand(book)
    
    print("=== DEMAND PREDICTION ===")
    print(f"Book: {book['title']}")
    print(predictor.format_prediction(prediction, book['title']))
    
    # Get feature importance
    importance = predictor.get_feature_importance()
    print("Feature Importance:")
    for feature, score in importance.items():
        print(f"  {feature}: {score:.4f}")


# ===========================================================================
# Example 5: Computer Vision - OCR
# ===========================================================================

from src.cv import BookCoverOCR

# Initialize OCR
ocr = BookCoverOCR(db)

# Search book from cover image
image_path = "path/to/book_cover.jpg"
if True:  # Check if file exists
    result = ocr.search_book_from_cover(image_path)
    
    print("=== OCR SEARCH ===")
    if result['success']:
        print(f"Extracted text: {result['extracted_text']}")
        print(f"Found {result['count']} books:")
        for book in result['results']:
            print(f"  - {book['title']}")
    else:
        print(f"Error: {result['message']}")


# ===========================================================================
# Example 6: Advanced Search with Filters
# ===========================================================================

# Search with rating filter
print("=== FILTERED SEARCH ===")
results = search.search_with_filters(
    query="love",
    min_rating=4.0,
    max_rating=5.0,
    limit=5
)
print(f"Found {len(results)} highly-rated books about love:")
for book in results:
    print(f"  - {book['title']} ({book['average_rating']}/5.0)")


# ===========================================================================
# Example 7: Dataset Statistics
# ===========================================================================

# Get dataset info
info = db.get_dataset_info()

print("\n=== DATASET STATISTICS ===")
print(f"Total Books: {info['total_books']}")
print(f"Unique Authors: {info['total_authors']}")
print(f"Average Rating: {info['avg_rating']:.2f}/5.0")
print(f"Min Rating: {info['min_rating']:.2f}")
print(f"Max Rating: {info['max_rating']:.2f}")


# ===========================================================================
# Example 8: Working with Individual Books
# ===========================================================================

# Get book by index
print("\n=== INDIVIDUAL BOOK ===")
book = db.get_book_by_index(0)
if book:
    print(f"Title: {book['title']}")
    print(f"Author: {book['authors']}")
    print(f"Rating: {book['average_rating']}/5.0")
    print(f"ISBN: {book['isbn']}")
    print(f"Publisher: {book['publisher']}")
    print(f"Year: {book['publication_date']}")


# ===========================================================================
# Example 9: Batch Operations
# ===========================================================================

from src.utils import format_book_display

# Search multiple times
titles = ["1984", "The Great Gatsby", "To Kill a Mockingbird"]
all_results = []

print("\n=== BATCH SEARCH ===")
for title in titles:
    results = db.search_by_title(title, limit=1)
    if results:
        all_results.append(results[0])
        print(f"✓ Found: {title}")
    else:
        print(f"✗ Not found: {title}")

# Batch predictions
print("\n=== BATCH PREDICTIONS ===")
predictions = predictor.predict_batch(all_results)
for book, pred in zip(all_results, predictions):
    if pred['success']:
        print(f"{book['title']}: {pred['demand']} ({pred['confidence']:.0%})")


# ===========================================================================
# Example 10: Custom Question Answering
# ===========================================================================

# Different types of questions
questions = [
    "Who is the author of 1984?",
    "What is the rating of The Great Gatsby?",
    "When was To Kill a Mockingbird published?",
    "Who published The Hobbit?",
    "How many pages in Pride and Prejudice?"
]

print("\n=== QUESTION ANSWERING ===")
for q in questions:
    try:
        answer = nlp.process_question_about_book(q)
        print(f"Q: {q}")
        print(f"A: {answer}\n")
    except Exception as e:
        print(f"Q: {q}")
        print(f"A: Could not answer - {e}\n")


# ===========================================================================
# Example 11: Saving Results
# ===========================================================================

from src.utils import save_result_to_file

# Save search results
results = search.search_by_title("Harry Potter", limit=10)
formatted = search.format_search_results(results)
save_result_to_file(formatted, "harry_potter_search.txt")
print("Results saved to outputs/harry_potter_search.txt")

# Save predictions
if results:
    predictions = predictor.predict_batch(results)
    pred_text = "PREDICTIONS\n" + "="*50 + "\n"
    for book, pred in zip(results, predictions):
        if pred['success']:
            pred_text += f"{book['title']}: {pred['demand']}\n"
    save_result_to_file(pred_text, "predictions.txt")
    print("Predictions saved to outputs/predictions.txt")


# ===========================================================================
# Example 12: Error Handling
# ===========================================================================

# Proper error handling
print("\n=== ERROR HANDLING ===")

# Empty search
try:
    results = search.search_by_title("")
    print(f"Found {len(results)} results")
except Exception as e:
    print(f"Error: {e}")

# Invalid image
try:
    result = ocr.search_book_from_cover("nonexistent.jpg")
    if not result['success']:
        print(f"OCR Error: {result['message']}")
except Exception as e:
    print(f"Error: {e}")

# Invalid question
if nlp.validate_question("What?"):
    answer = nlp.process_question_about_book("What?")
else:
    print("Invalid question provided")


# ===========================================================================
# QUICK START TEMPLATE
# ===========================================================================

"""
# Copy this template for quick usage:

from src.database import BooksDatabase
from src.search import BookSearch
from src.nlp import BookNLP
from src.rag import BookRAG
from src.ml import DemandPredictor

# Initialize
db = BooksDatabase()
search = BookSearch(db)
nlp = BookNLP(db)
rag = BookRAG(db)
ml = DemandPredictor(db)

# Use modules
results = search.search_by_title("book title")
answer = rag.answer_question("your question?")
prediction = ml.predict_demand(results[0])

print(answer)
print(prediction)
"""
