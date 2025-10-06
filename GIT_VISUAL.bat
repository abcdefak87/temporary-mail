@echo off
title Git Visual Commit Manager
color 0A

:: Enable UTF-8 for better graph display
chcp 65001 >nul 2>&1

echo ========================================
echo     GIT VISUAL COMMIT MANAGER
echo     Branch Graph Visualization
echo ========================================
echo.

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed
    pause
    exit /b 1
)

:: Run visual manager
python git_visual.py %*

:: Keep window open on error
if errorlevel 1 (
    echo.
    echo [ERROR] Script failed
    pause
)
