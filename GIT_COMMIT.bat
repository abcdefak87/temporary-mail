@echo off
title Git Branch and Commit Manager
color 0A

echo ========================================
echo     GIT BRANCH AND COMMIT MANAGER
echo ========================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

:: Run the Git manager
python git_commit.py

:: Keep window open if there was an error
if errorlevel 1 (
    echo.
    echo [ERROR] Script failed to run
    pause
)
