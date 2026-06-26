@echo off
REM Smart Library Assistant - Windows Setup and Launch Script

echo.
echo ===============================================================
echo   SMART LIBRARY ASSISTANT - Setup and Launch
echo ===============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://www.python.org/
    pause
    exit /b 1
)

REM Check if requirements are installed
echo Checking dependencies...
pip list | findstr "pandas opencv" >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo Installing required packages...
    echo This may take a few minutes...
    echo.
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo.
        echo Error: Failed to install dependencies
        pause
        exit /b 1
    )
)

echo.
echo ===============================================================
echo   Starting Smart Library Assistant GUI
echo ===============================================================
echo.

REM Run the application
python app.py

if %errorlevel% neq 0 (
    echo.
    echo Error: Application failed to start
    echo Check the error message above
    pause
    exit /b 1
)
