@echo off
title Personal Board of Directors - Quick Start
color 0B
echo ==================================================
echo   Personal Board of Directors - Quick Start
echo   Initializing full-stack decision sandtable...
echo ==================================================
echo.

:: 1. Start Backend Server
echo [1/3] Checking Backend Server (Port 8080)...
netstat -ano | findstr :8080 >nul
if %errorlevel% equ 0 (
    echo   [+] Backend is already running.
) else (
    echo   [*] Starting Backend Server in a new window...
    start "Personal Board - Backend API" cmd /c "cd /d backend && python -m uvicorn main:app --host 127.0.0.1 --port 8080"
    echo   [*] Waiting for backend indexing to initialize (usually 10-15s)...
    timeout /t 8 >nul
)

:: 2. Start Frontend Server
echo [2/3] Checking Frontend Server (Port 5173)...
netstat -ano | findstr :5173 >nul
if %errorlevel% equ 0 (
    echo   [+] Frontend is already running.
) else (
    echo   [*] Starting Frontend Server in a new window...
    start "Personal Board - Frontend Web" cmd /c "cd /d frontend && npm run dev"
    timeout /t 3 >nul
)

:: 3. Launch Browser
echo [3/3] Launching web browser...
start http://localhost:5173/

echo.
echo ==================================================
echo   Startup sequence complete!
echo   Enjoy your collaborative multi-agent debate!
echo ==================================================
timeout /t 5
