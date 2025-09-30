#!/bin/bash
# 🚀 راه‌اندازی پروژه تحلیلگر کدال ایران
# Setup script for Codal Data Analyzer

echo "Setting up Codal Data Analyzer Project"
echo "====================================="

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 is not installed. Please install Python3 first."
    exit 1
fi

echo "Python3 found: $(python3 --version)"

# Create virtual environment
if [ ! -d "codal_env" ]; then
    echo "Creating virtual environment..."
    python3 -m venv codal_env
    echo "Virtual environment created"
else
    echo "Virtual environment already exists"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source codal_env/bin/activate

# Install dependencies
echo "Installing required packages..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "Setup completed successfully!"
echo ""
echo "Useful commands:"
echo "  Activate env:   source codal_env/bin/activate"
echo "  Run tests:      python test_codal.py"
echo "  Run analyzer:   python codal_data_analyzer.py"
echo "  Jupyter:        jupyter notebook codal_analysis.ipynb"
echo ""
echo "To get started:"
echo "  1. source codal_env/bin/activate"
echo "  2. python test_codal.py"
echo ""
