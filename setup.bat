@echo off
echo yt-dlp MCP Server Setup
echo ========================

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

echo Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Trying with --user flag...
    pip install --user -r requirements.txt
    if %errorlevel% neq 0 (
        echo Failed to install dependencies
        echo Please run: pip install fastmcp yt-dlp youtube-search-python
        pause
        exit /b 1
    )
)

echo Installing package in development mode...
pip install -e .
if %errorlevel% neq 0 (
    echo Trying with --user flag...
    pip install --user -e .
    if %errorlevel% neq 0 (
        echo Failed to install package
        pause
        exit /b 1
    )
)

echo.
echo Setup completed successfully!
echo.
echo You can now run the MCP server with:
echo   yt-dlp-mcp
echo.
echo Or test the functionality with:
echo   python test_server.py
echo.
pause
