"""
Smart Library Assistant - Main Application
A complete college mini project using Python with Tkinter GUI
Features: Book Search, OCR, NLP, RAG, and ML-based Demand Prediction
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import threading
from typing import Optional
from src.database import BooksDatabase
from src.search import BookSearch
from src.nlp import BookNLP
from src.cv import BookCoverOCR
from src.rag import BookRAG
from src.ml import DemandPredictor
from src.utils import format_book_display, validate_image_file


class SmartLibraryGUI:
    """
    Tkinter GUI for Smart Library Assistant
    Provides user interface for all features:
    - Book Search (Title/Author)
    - Image Upload & OCR
    - Question Answering (NLP/RAG)
    - Demand Prediction (ML)
    """
    
    def __init__(self, root):
        """
        Initialize the GUI application
        
        Args:
            root: Tkinter root window
        """
        self.root = root
        self.root.title("Smart Library Assistant")
        self.root.geometry("1000x800")
        self.root.configure(bg='#f0f0f0')
        
        # Initialize modules
        self.db = BooksDatabase()
        self.search = BookSearch(self.db)
        self.nlp = BookNLP(self.db)
        self.cv = BookCoverOCR(self.db)
        self.rag = BookRAG(self.db)
        self.ml = DemandPredictor(self.db)
        
        # Current search results
        self.current_results = []
        
        # Setup GUI
        self.setup_ui()
    
    def setup_ui(self):
        """
        Setup the main user interface with tabs
        """
        # Title
        title_frame = tk.Frame(self.root, bg='#2c3e50')
        title_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            title_frame,
            text="📚 Smart Library Assistant",
            font=("Arial", 20, "bold"),
            bg='#2c3e50',
            fg='white',
            pady=10
        )
        title_label.pack()
        
        # Notebook (Tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create tabs
        self.create_search_tab()
        self.create_nlp_tab()
        self.create_cv_tab()
        self.create_ml_tab()
    
    def create_search_tab(self):
        """Create the search tab for title and author search"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Search Books")
        
        # Search options
        options_frame = tk.Frame(frame, bg='white')
        options_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(options_frame, text="Search Type:", font=("Arial", 10, "bold"), bg='white').pack(side=tk.LEFT, padx=5)
        
        self.search_type_var = tk.StringVar(value="title")
        tk.Radiobutton(options_frame, text="By Title", variable=self.search_type_var, 
                      value="title", bg='white').pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(options_frame, text="By Author", variable=self.search_type_var, 
                      value="author", bg='white').pack(side=tk.LEFT, padx=5)
        
        # Search input
        search_frame = tk.Frame(frame, bg='white')
        search_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(search_frame, text="Search Query:", font=("Arial", 10), bg='white').pack(side=tk.LEFT, padx=5)
        
        self.search_entry = tk.Entry(search_frame, font=("Arial", 10), width=40)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.search_entry.bind('<Return>', lambda e: self.perform_search())
        
        search_btn = tk.Button(search_frame, text="Search", command=self.perform_search, 
                              bg='#3498db', fg='white', font=("Arial", 10, "bold"))
        search_btn.pack(side=tk.LEFT, padx=5)
        
        # Results display
        results_frame = tk.Frame(frame)
        results_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(results_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.search_results_text = scrolledtext.ScrolledText(
            results_frame,
            font=("Courier", 9),
            yscrollcommand=scrollbar.set,
            bg='white',
            fg='#2c3e50'
        )
        self.search_results_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.search_results_text.yview)
        
        # Action buttons
        action_frame = tk.Frame(frame, bg='white')
        action_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(action_frame, text="Predict Demand", command=self.predict_from_search,
                 bg='#e74c3c', fg='white', font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        tk.Button(action_frame, text="Clear", command=lambda: self.search_results_text.delete('1.0', tk.END),
                 bg='#95a5a6', fg='white', font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
    
    def create_nlp_tab(self):
        """Create the NLP tab for question answering"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Ask Question (NLP & RAG)")
        
        # Question input
        question_frame = tk.Frame(frame, bg='white')
        question_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(question_frame, text="Ask a Question:", font=("Arial", 10, "bold"), bg='white').pack(side=tk.LEFT, padx=5)
        
        self.question_entry = tk.Entry(question_frame, font=("Arial", 10), width=50)
        self.question_entry.pack(side=tk.LEFT, padx=5)
        self.question_entry.bind('<Return>', lambda e: self.answer_question())
        
        ask_btn = tk.Button(question_frame, text="Ask", command=self.answer_question,
                           bg='#27ae60', fg='white', font=("Arial", 10, "bold"))
        ask_btn.pack(side=tk.LEFT, padx=5)
        
        # Example questions
        examples_frame = tk.Frame(frame, bg='#ecf0f1')
        examples_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(examples_frame, text="Example Questions:", font=("Arial", 9, "bold"), bg='#ecf0f1').pack(anchor=tk.W, padx=5, pady=5)
        
        examples = [
            "What is the rating of Harry Potter?",
            "Who is the author of The Great Gatsby?",
            "When was To Kill a Mockingbird published?"
        ]
        
        for example in examples:
            tk.Label(examples_frame, text="• " + example, font=("Arial", 9), bg='#ecf0f1', justify=tk.LEFT).pack(anchor=tk.W, padx=20)
        
        # Answer display
        answer_frame = tk.Frame(frame)
        answer_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(answer_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.answer_text = scrolledtext.ScrolledText(
            answer_frame,
            font=("Courier", 9),
            yscrollcommand=scrollbar.set,
            bg='white',
            fg='#2c3e50'
        )
        self.answer_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.answer_text.yview)
    
    def create_cv_tab(self):
        """Create the CV tab for image upload and OCR"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Image Upload & OCR")
        
        # Upload section
        upload_frame = tk.Frame(frame, bg='white')
        upload_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(upload_frame, text="Upload Book Cover Image:", font=("Arial", 10, "bold"), bg='white').pack(side=tk.LEFT, padx=5)
        
        self.image_path_var = tk.StringVar(value="No image selected")
        tk.Label(upload_frame, textvariable=self.image_path_var, font=("Arial", 9), bg='#ecf0f1', fg='#7f8c8d').pack(side=tk.LEFT, padx=5)
        
        upload_btn = tk.Button(upload_frame, text="Browse", command=self.select_image,
                              bg='#9b59b6', fg='white', font=("Arial", 10))
        upload_btn.pack(side=tk.LEFT, padx=5)
        
        # OCR button
        ocr_btn = tk.Button(upload_frame, text="Extract & Search", command=self.perform_ocr,
                           bg='#e67e22', fg='white', font=("Arial", 10, "bold"))
        ocr_btn.pack(side=tk.LEFT, padx=5)
        
        # Info
        info_frame = tk.Frame(frame, bg='#fff3cd')
        info_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(info_frame, text="ℹ Supported formats: JPG, PNG, BMP, GIF",
                font=("Arial", 9), bg='#fff3cd', fg='#856404').pack(anchor=tk.W, padx=5, pady=5)
        
        # Results display
        results_frame = tk.Frame(frame)
        results_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(results_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.cv_results_text = scrolledtext.ScrolledText(
            results_frame,
            font=("Courier", 9),
            yscrollcommand=scrollbar.set,
            bg='white',
            fg='#2c3e50'
        )
        self.cv_results_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.cv_results_text.yview)
    
    def create_ml_tab(self):
        """Create the ML tab for demand prediction"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Demand Prediction (ML)")
        
        # Instructions
        instructions_frame = tk.Frame(frame, bg='#e8f8f5')
        instructions_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(instructions_frame, 
                text="1. Search for a book first\n2. Click 'Predict Demand' on the Search tab\n3. Results show High/Medium/Low demand prediction",
                font=("Arial", 9), bg='#e8f8f5', fg='#16a085', justify=tk.LEFT).pack(anchor=tk.W, padx=5, pady=5)
        
        # Predictions display
        predictions_frame = tk.Frame(frame)
        predictions_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(predictions_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.ml_results_text = scrolledtext.ScrolledText(
            predictions_frame,
            font=("Courier", 9),
            yscrollcommand=scrollbar.set,
            bg='white',
            fg='#2c3e50'
        )
        self.ml_results_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.ml_results_text.yview)
    
    def perform_search(self):
        """Perform book search based on selected type"""
        query = self.search_entry.get().strip()
        
        if not query:
            messagebox.showwarning("Input Error", "Please enter a search query")
            return
        
        search_type = self.search_type_var.get()
        
        # Run search in separate thread to prevent GUI freezing
        thread = threading.Thread(target=self._search_thread, args=(query, search_type))
        thread.daemon = True
        thread.start()
    
    def _search_thread(self, query: str, search_type: str):
        """Run search in separate thread"""
        try:
            if search_type == "title":
                self.current_results = self.search.search_by_title(query)
            else:
                self.current_results = self.search.search_by_author(query)
            
            # Format and display results
            results_text = self.search.format_search_results(self.current_results)
            
            self.search_results_text.config(state=tk.NORMAL)
            self.search_results_text.delete('1.0', tk.END)
            self.search_results_text.insert('1.0', results_text)
            self.search_results_text.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Error", f"Search failed: {e}")
    
    def answer_question(self):
        """Answer a question using NLP and RAG"""
        question = self.question_entry.get().strip()
        
        if not question:
            messagebox.showwarning("Input Error", "Please enter a question")
            return
        
        # Run in separate thread
        thread = threading.Thread(target=self._answer_thread, args=(question,))
        thread.daemon = True
        thread.start()
    
    def _answer_thread(self, question: str):
        """Run question answering in separate thread"""
        try:
            result = self.rag.answer_question(question)
            
            answer_text = f"Question: {question}\n"
            answer_text += f"{'='*60}\n\n"
            answer_text += result['answer']
            answer_text += f"\n\nConfidence: {result['confidence']:.2%}"
            
            self.answer_text.config(state=tk.NORMAL)
            self.answer_text.delete('1.0', tk.END)
            self.answer_text.insert('1.0', answer_text)
            self.answer_text.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to answer question: {e}")
    
    def select_image(self):
        """Select an image file"""
        file_path = filedialog.askopenfilename(
            title="Select a book cover image",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif"), ("All files", "*.*")]
        )
        
        if file_path:
            self.image_path_var.set(file_path)
    
    def perform_ocr(self):
        """Perform OCR on selected image"""
        image_path = self.image_path_var.get()
        
        if image_path == "No image selected":
            messagebox.showwarning("Input Error", "Please select an image first")
            return
        
        # Run in separate thread
        thread = threading.Thread(target=self._ocr_thread, args=(image_path,))
        thread.daemon = True
        thread.start()
    
    def _ocr_thread(self, image_path: str):
        """Run OCR in separate thread"""
        try:
            result = self.cv.search_book_from_cover(image_path)
            
            output = f"Image: {image_path}\n"
            output += f"{'='*60}\n\n"
            
            if result['success']:
                output += f"Extracted Text: {result['extracted_text']}\n\n"
                output += f"Found {result['count']} matching book(s):\n\n"
                
                for idx, book in enumerate(result['results'], 1):
                    output += f"{idx}. {book['title']}\n"
                    output += f"   Author: {book['authors']}\n"
                    output += f"   Rating: {book['average_rating']}/5.0\n\n"
            else:
                output += f"Error: {result['message']}\n"
            
            self.cv_results_text.config(state=tk.NORMAL)
            self.cv_results_text.delete('1.0', tk.END)
            self.cv_results_text.insert('1.0', output)
            self.cv_results_text.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Error", f"OCR failed: {e}")
    
    def predict_from_search(self):
        """Predict demand for books in current search results"""
        if not self.current_results:
            messagebox.showwarning("No Results", "Please perform a search first")
            return
        
        # Run in separate thread
        thread = threading.Thread(target=self._predict_thread)
        thread.daemon = True
        thread.start()
    
    def _predict_thread(self):
        """Run demand prediction in separate thread"""
        try:
            output = "DEMAND PREDICTIONS\n"
            output += f"{'='*60}\n\n"
            
            for book in self.current_results[:5]:  # Predict for top 5 results
                result = self.ml.predict_demand(book)
                
                output += f"Book: {book['title']}\n"
                output += f"Author: {book['authors']}\n"
                
                if result['success']:
                    output += f"Predicted Demand: {result['demand']}\n"
                    output += f"Confidence: {result['confidence']:.2%}\n"
                else:
                    output += f"Error: {result.get('message', 'Unknown error')}\n"
                
                output += f"{'-'*60}\n"
            
            self.ml_results_text.config(state=tk.NORMAL)
            self.ml_results_text.delete('1.0', tk.END)
            self.ml_results_text.insert('1.0', output)
            self.ml_results_text.config(state=tk.DISABLED)
            
            # Switch to ML tab
            self.notebook.select(3)
        except Exception as e:
            messagebox.showerror("Error", f"Prediction failed: {e}")


def main():
    """
    Main entry point for the application
    """
    root = tk.Tk()
    app = SmartLibraryGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
