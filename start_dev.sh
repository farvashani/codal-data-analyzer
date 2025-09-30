#!/bin/bash
# Development Environment Setup Script for Codal Data Analyzer

echo "Starting Codal Data Analyzer Development Environment"
echo "=================================================="

# Setup SSH Agent and add key
echo "Setting up SSH..."
eval "$(ssh-agent -s)" > /dev/null 2>&1
ssh-add ~/.ssh/github_key > /dev/null 2>&1

# Test GitHub connection
echo "Testing GitHub connection..."
if ssh -T git@github.com > /dev/null 2>&1; then
    echo "GitHub connection: OK"
else
    echo "GitHub connection: FAILED"
fi

# Activate virtual environment
echo "Activating virtual environment..."
if [ -d "codal_env" ]; then
    source codal_env/bin/activate
    echo "Virtual environment: ACTIVATED"
else
    echo "Virtual environment: NOT FOUND (run ./setup.sh first)"
fi

echo ""
echo "Development environment is ready!"
echo ""
echo "Useful commands:"
echo "  Test project:    python test_codal.py"
echo "  Run analyzer:    python codal_data_analyzer.py"
echo "  Jupyter:         jupyter notebook codal_analysis.ipynb"
echo "  Git push:        git push origin main"
echo ""
