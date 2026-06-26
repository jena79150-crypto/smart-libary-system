"""
Quick Test Script for Smart Library Assistant
Tests all major components
"""

from src.database import BooksDatabase
from src.search import BookSearch
from src.nlp import BookNLP
from src.ml import DemandPredictor

print("\n" + "="*60)
print("SMART LIBRARY ASSISTANT - COMPONENT TEST")
print("="*60 + "\n")

# Test 1: Database
print("TEST 1: Loading Database...")
try:
    db = BooksDatabase()
    print(f"✅ Successfully loaded {len(db.df)} books")
    print(f"   Columns: {db.df.columns.tolist()}\n")
except Exception as e:
    print(f"❌ Error: {e}\n")

# Test 2: Search by Title
print("TEST 2: Searching by Title...")
try:
    search = BookSearch(db)
    results = search.search_by_title("Harry Potter", limit=3)
    print(f"✅ Found {len(results)} books for 'Harry Potter'")
    for book in results:
        print(f"   - {book['title']} by {book['authors']}")
    print()
except Exception as e:
    print(f"❌ Error: {e}\n")

# Test 3: Search by Author
print("TEST 3: Searching by Author...")
try:
    results = search.search_by_author("J.K. Rowling", limit=3)
    print(f"✅ Found {len(results)} books by 'J.K. Rowling'")
    for book in results[:2]:
        print(f"   - {book['title']}")
    print()
except Exception as e:
    print(f"❌ Error: {e}\n")

# Test 4: NLP Question Answering
print("TEST 4: NLP Question Answering...")
try:
    nlp = BookNLP(db)
    question = "What is the rating of The Great Gatsby?"
    answer = nlp.process_question_about_book(question)
    print(f"Question: {question}")
    print(f"✅ Answer: {answer}\n")
except Exception as e:
    print(f"❌ Error: {e}\n")

# Test 5: ML Demand Prediction
print("TEST 5: Training ML Model...")
try:
    predictor = DemandPredictor(db)
    
    # Get a book to predict
    sample_book = results[0] if results else None
    if sample_book:
        prediction = predictor.predict_demand(sample_book)
        print(f"Book: {sample_book['title']}")
        print(f"✅ Prediction: {prediction['demand']}")
        print(f"   Confidence: {prediction['confidence']:.2%}\n")
except Exception as e:
    print(f"❌ Error: {e}\n")

# Test 6: Dataset Info
print("TEST 6: Dataset Statistics...")
try:
    info = db.get_dataset_info()
    print(f"✅ Total Books: {info['total_books']}")
    print(f"   Unique Authors: {info['total_authors']}")
    print(f"   Average Rating: {info['avg_rating']:.2f}/5.0")
    print(f"   Rating Range: {info['min_rating']:.2f} - {info['max_rating']:.2f}\n")
except Exception as e:
    print(f"❌ Error: {e}\n")

print("="*60)
print("ALL TESTS COMPLETED!")
print("="*60)
print("\nYou can now run the GUI with: python app.py\n")
