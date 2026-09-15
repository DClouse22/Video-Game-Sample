@echo off
REM Video Games Sales Dashboard - Windows Setup Script

echo.
echo 🎮 Video Games Sales Dashboard - Windows Setup
echo ==============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH.
    echo Please install Python 3.8 or higher from https://www.python.org
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ Python %PYTHON_VERSION% detected
echo.

REM Check if CSV file exists
if not exist "video_games_sales.csv" (
    echo ⚠️  Warning: 'video_games_sales.csv' not found in the current directory.
    echo    Please ensure the CSV file is placed in the same directory.
    echo.
)

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
    echo ✅ Virtual environment created
) else (
    echo ✅ Virtual environment already exists
)

echo.
echo 🔌 Activating virtual environment...
call venv\Scripts\activate.bat
echo ✅ Virtual environment activated
echo.

REM Install requirements
echo 📚 Installing dependencies...
python -m pip install --upgrade pip > nul 2>&1
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

echo ✅ Dependencies installed successfully
echo.
echo ==============================================
echo ✅ Setup complete!
echo ==============================================
echo.
echo 🚀 To run the dashboard, use:
echo    streamlit run video_games_dashboard.py
echo.
echo Or double-click: run.bat
echo.
pause
