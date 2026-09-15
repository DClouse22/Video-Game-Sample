#!/bin/bash

# Video Games Sales Dashboard - Run Script
# Activates the virtual environment and starts the Streamlit app

if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Running setup first..."
    ./setup.sh
fi

echo "🚀 Starting Video Games Sales Dashboard..."
echo ""

# Activate virtual environment
source venv/bin/activate

# Run Streamlit
streamlit run video_games_dashboard.py
