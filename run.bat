@echo off
REM Video Games Sales Dashboard - Windows Run Script

if not exist "venv" (
    echo Virtual environment not found. Running setup first...
    call setup.bat
)

echo.
echo 🚀 Starting Video Games Sales Dashboard...
echo.

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Run Streamlit
streamlit run video_games_dashboard.py
