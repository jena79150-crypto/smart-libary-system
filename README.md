# Smart Library Assistant 📚

A comprehensive college mini project that combines **Machine Learning**, **Natural Language Processing**, **Computer Vision**, and **Retrieval Augmented Generation** to create an intelligent library management system.

## 🌟 Features

### 1. **Book Search**
   - Search books by **Title** (partial matching)
   - Search books by **Author** (partial matching)
   - Display detailed book information:
     - Title, Author, Rating, ISBN, Publisher, Publication Year
     - Number of pages, ratings count, reviews count

### 2. **Computer Vision (OCR)**
   - Upload book cover images (JPG, PNG, BMP, GIF)
   - Extract text from images using **OpenCV + Tesseract OCR**
   - Automatically search for extracted book titles in the database
   - Image preprocessing for better OCR accuracy

### 3. **Natural Language Processing (NLP)**
   - Ask natural language questions about books
   - Extract question types: author, rating, year, publisher, pages, reviews
   - Parse questions to find relevant book titles
   - Answer questions with dataset information

### 4. **Retrieval Augmented Generation (RAG)**
   - Answer user questions using only dataset information
   - Retrieve relevant books from database
   - Generate context-aware answers
   - Ensures factual accuracy by limiting to dataset sources

### 5. **Machine Learning (Demand Prediction)**
   - Train ML model on book ratings and review counts
   - Predict book demand: **High**, **Medium**, **Low**
   - Uses **Random Forest Classifier** for robust predictions
   - Displays prediction confidence and probability distribution
   - Model persistence with pickle serialization

### 6. **Tkinter GUI**
   - Clean, user-friendly interface with 4 tabs:
     - **Search Books**: Title/Author search
     - **Ask Question**: NLP & RAG-based Q&A
     - **Image Upload & OCR**: Book cover image processing
     - **Demand Prediction**: ML-based predictions
   - Real-time results display
   - Threading for non-blocking operations

---

## 📋 Project Structure

```
SmartLibraryAssistant/
│
├── data/
│   └── books (1).csv          # Goodreads Books Dataset (11,123 books)
│
├── uploads/                    # Directory for uploaded book cover images
│
├── outputs/                    # Directory for saved results
│
├── models/                     # Directory for trained ML models
│   └── demand_model.pkl        # Trained demand predictor model
│
├── src/                        # Source code modules
│   ├── __init__.py
│   ├── database.py            # CSV data loading and book queries
│   ├── search.py              # Book search functionality
│   ├── nlp.py                 # Natural language processing
│   ├── cv.py                  # Computer vision & OCR
│   ├── rag.py                 # Retrieval Augmented Generation
│   ├── ml.py                  # Machine learning model
│   └── utils.py               # Utility functions
│
├── app.py                      # Main Tkinter GUI application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── .gitignore
```

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Tesseract OCR (for image text extraction)

### Step 1: Install Python Dependencies

```bash
cd "path/to/Smart Library Assistant"
pip install -r requirements.txt
```

### Step 2: Install Tesseract OCR

**Windows:**
1. Download Tesseract installer from: https://github.com/UB-Mannheim/tesseract/wiki
2. Run the installer (default installation path: `C:\Program Files\Tesseract-OCR`)
3. Update pytesseract path in code if needed

**Ubuntu/Debian:**
```bash
sudo apt-get install tesseract-ocr
```

**macOS:**
```bash
brew install tesseract
```

### Step 3: Prepare Dataset

Ensure `data/books (1).csv` exists in the data folder (provided with project)

---

## ▶️ Running the Application

```bash
python app.py
```

The GUI will open with all features ready to use.

---

## 📖 Usage Guide

### 1. **Search Books Tab**
   - Enter a title or author name
   - Click **Search** or press Enter
   - View results with complete book information
   - Click **Predict Demand** to get ML predictions for top results

### 2. **Ask Question Tab (NLP & RAG)**
   - Type a natural language question
   - Example: "What is the rating of The Great Gatsby?"
   - System extracts the book title and answers using dataset
   - Only dataset information is used (no external knowledge)

### 3. **Image Upload & OCR Tab**
   - Click **Browse** to select a book cover image
   - Click **Extract & Search** to:
     - Extract text from the image
     - Automatically search database
     - Display matching books
   - Supports: JPG, PNG, BMP, GIF formats

### 4. **Demand Prediction Tab**
   - Predictions appear after clicking "Predict Demand" in Search tab
   - Shows:
     - Predicted demand level (High/Medium/Low)
     - Confidence score (0-100%)
     - Probability distribution for each demand level

---

## 🔧 Module Documentation

### `src/database.py`
- **BooksDatabase class**: Manages CSV data and book queries
- Key methods:
  - `search_by_title()`: Search books by title
  - `search_by_author()`: Search books by author
  - `get_top_rated_books()`: Get highest-rated books
  - `get_dataset_info()`: Dataset statistics

### `src/search.py`
- **BookSearch class**: Provides search functionality
- Key methods:
  - `search_by_title()`: Title search
  - `search_by_author()`: Author search
  - `search_combined()`: Combined title+author search
  - `format_search_results()`: Format results for display

### `src/nlp.py`
- **BookNLP class**: Natural language processing
- Key methods:
  - `extract_question_type()`: Identify question type
  - `extract_book_title()`: Extract book title from text
  - `answer_question()`: Generate answers about books
  - `process_question_about_book()`: End-to-end Q&A

### `src/cv.py`
- **BookCoverOCR class**: Image processing and OCR
- Key methods:
  - `extract_text_from_image()`: OCR text extraction
  - `extract_book_title_from_image()`: Extract likely title
  - `search_book_from_cover()`: Search using image
  - `preprocess_image()`: Image enhancement for OCR

### `src/rag.py`
- **BookRAG class**: Retrieval Augmented Generation
- Key methods:
  - `retrieve_book_context()`: Retrieve relevant books
  - `generate_answer_from_context()`: Generate answers
  - `answer_question()`: RAG-based question answering
  - `verify_answer_in_database()`: Verify answer authenticity

### `src/ml.py`
- **DemandPredictor class**: ML-based demand prediction
- Key methods:
  - `prepare_training_data()`: Prepare training dataset
  - `train_model()`: Train Random Forest classifier
  - `predict_demand()`: Predict demand for single book
  - `predict_batch()`: Predict for multiple books
  - `get_feature_importance()`: Show model feature importance

### `src/utils.py`
- Utility functions for:
  - File validation
  - Text cleaning and formatting
  - Missing data handling
  - Results display formatting

---

## 📊 Dataset Information

**Goodreads Books Dataset:**
- Total books: 11,123
- Columns: Title, Authors, Rating, ISBN, Publisher, Publication Date, Pages, Ratings Count, Reviews Count
- Source: Goodreads API
- Format: CSV

---

## 🤖 Machine Learning Model Details

### Model Type
- **Algorithm**: Random Forest Classifier
- **Number of Trees**: 100
- **Max Depth**: 10
- **Test Accuracy**: ~75-85%

### Features Used
1. `average_rating`: Book rating (0-5)
2. `ratings_count`: Number of ratings received
3. `text_reviews_count`: Number of text reviews

### Target Variable
- **High Demand**: Top 33% of books by demand score
- **Medium Demand**: Middle 33% of books
- **Low Demand**: Bottom 33% of books

### Training Process
1. Load dataset and create features
2. Normalize metrics (rating, review counts)
3. Calculate demand scores (weighted combination)
4. Split data (80% train, 20% test)
5. Scale features using StandardScaler
6. Train Random Forest model
7. Save model for future predictions

---

## ⚙️ Technical Stack

| Component | Technology |
|-----------|-----------|
| GUI | Tkinter (built-in with Python) |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Computer Vision | OpenCV |
| OCR | Tesseract, PyTesseract |
| Model Persistence | Pickle |

---

## 📝 Key Code Examples

### Search for Books
```python
from src.search import BookSearch

search = BookSearch()
results = search.search_by_title("Harry Potter")
print(search.format_search_results(results))
```

### Answer Questions
```python
from src.rag import BookRAG

rag = BookRAG()
result = rag.answer_question("What is the rating of The Great Gatsby?")
print(result['answer'])
```

### Predict Demand
```python
from src.ml import DemandPredictor

predictor = DemandPredictor()
prediction = predictor.predict_demand(book_dict)
print(predictor.format_prediction(prediction, "Book Title"))
```

### Extract Text from Image
```python
from src.cv import BookCoverOCR

ocr = BookCoverOCR()
result = ocr.search_book_from_cover("path/to/image.jpg")
print(f"Found {result['count']} books")
```

---

## 🐛 Troubleshooting

### Tesseract Not Found Error
- **Solution**: Install Tesseract from https://github.com/UB-Mannheim/tesseract/wiki
- Update Python path in cv.py if installed in non-default location

### No Results in Search
- Try shorter search terms (e.g., "Harry" instead of "Harry Potter and the Philosopher's Stone")
- Check dataset for book availability

### ML Model Not Trained
- Model automatically trains on first run
- Training takes ~10-20 seconds depending on system
- Model is saved in `models/demand_model.pkl` for future use

### Image OCR Not Working
- Ensure image has clear, readable text
- Tesseract performs better on clean, high-resolution images
- Try preprocessing options (resize, crop title area)

---

## 🎓 Learning Outcomes

This project demonstrates:
- ✅ **GUI Development**: Tkinter framework and threading
- ✅ **Data Processing**: Pandas for dataset manipulation
- ✅ **Machine Learning**: Training and inference with scikit-learn
- ✅ **Computer Vision**: Image processing and OCR
- ✅ **NLP**: Text parsing and question understanding
- ✅ **Software Architecture**: Modular code organization
- ✅ **Error Handling**: Robust exception management
- ✅ **Best Practices**: Comments, documentation, code style

---

## 📄 License

This project is created for educational purposes as a college mini project.

---

## 👨‍💼 Author

**Smart Library Assistant** - A comprehensive demonstration of modern Python development practices combining ML, NLP, CV, and RAG technologies.

---

## 📞 Support

For issues or questions:
1. Check the **Troubleshooting** section
2. Verify all dependencies are installed: `pip list`
3. Ensure Tesseract is properly installed
4. Check dataset file exists: `data/books (1).csv`

---

## 🚀 Future Enhancements

- [ ] Connect to live Goodreads API for real-time data
- [ ] Add more NLP features (entity recognition, sentiment analysis)
- [ ] Implement advanced ML models (XGBoost, Neural Networks)
- [ ] Add database backend (SQLite/PostgreSQL)
- [ ] Create REST API for web integration
- [ ] Add recommendation system
- [ ] Multi-language support
- [ ] Web-based UI using Flask/Django

---

**Version**: 1.0.0  
**Last Updated**: June 2026  
**Status**: Complete and Production Ready ✅
