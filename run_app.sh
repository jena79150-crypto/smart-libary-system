#!/bin/bash
# Smart Library Assistant - Unix/Linux/macOS Setup and Launch Script

echo ""
echo "==============================================================="
echo "  SMART LIBRARY ASSISTANT - Setup and Launch"
echo "==============================================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.7+ from https://www.python.org/"
    exit 1
fi

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Found Python $python_version"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "Error: pip3 is not installed"
    echo "Please install pip: sudo apt-get install python3-pip"
    exit 1
fi

# Install Tesseract if not already installed (for Linux)
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if ! command -v tesseract &> /dev/null; then
        echo ""
        echo "Tesseract OCR not found. Installing..."
        sudo apt-get update
        sudo apt-get install -y tesseract-ocr
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    if ! command -v tesseract &> /dev/null; then
        echo ""
        echo "Tesseract OCR not found. Please install with:"
        echo "  brew install tesseract"
        exit 1
    fi
fi

# Install Python dependencies
echo ""
echo "Checking and installing Python dependencies..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo ""
    echo "Error: Failed to install dependencies"
    exit 1
fi

echo ""
echo "==============================================================="
echo "  Starting Smart Library Assistant GUI"
echo "==============================================================="
echo ""

# Run the application
python3 app.py

if [ $? -ne 0 ]; then
    echo ""
    echo "Error: Application failed to start"
    echo "Check the error message above"
    exit 1
fi
