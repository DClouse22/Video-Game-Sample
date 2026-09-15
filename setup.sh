#!/bin/bash

# Video Games Sales Dashboard - Setup Script
# This script sets up the environment and runs the Streamlit dashboard

echo "🎮 Video Games Sales Dashboard - Setup"
echo "======================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python $(python3 --version | cut -d' ' -f2) detected"
echo ""

# Check if CSV file exists
if [ ! -f "video_games_sales.csv" ]; then
    echo "⚠️  Warning: 'video_games_sales.csv' not found in the current directory."
    echo "   Please ensure the CSV file is placed in the same directory as this script."
    echo ""
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

echo ""
echo "🔌 Activating virtual environment..."

# Activate virtual environment
source venv/bin/activate

echo "✅ Virtual environment activated"
echo ""

# Install requirements
echo "📚 Installing dependencies..."
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""
echo "======================================="
echo "✅ Setup complete!"
echo "======================================="
echo ""
echo "🚀 To run the dashboard, use:"
echo "   streamlit run video_games_dashboard.py"
echo ""
echo "Or execute: ./run.sh"
echo ""
