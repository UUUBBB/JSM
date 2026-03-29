@echo off
chcp 65001 >nul
title AI Video Narrator
cd /d "%~dp0"

REM 将上级目录加入 PATH（ffmpeg/ffprobe 在上级目录）
set "PATH=%~dp0..;%PATH%"

echo ========================================
echo   AI Video Narrator - Starting...
echo ========================================
echo.

REM ===== 检查并应用待处理的更新 =====
if exist "_pending_update\_update_pending.json" (
    echo [更新] 检测到待应用的更新，正在应用...
    ..\python312\python.exe _apply_pending_update.py
    echo.
)

REM 首次启动自动创建默认 .env（不打断用户）
if not exist ".env" (
    if exist ".env.example" (
        copy ".env.example" ".env" >nul
    ) else (
        echo # API配置> ".env"
        echo API_BASE_URL=>> ".env"
        echo API_KEY=>> ".env"
        echo MODEL_NAME=gemini-2.0-flash>> ".env"
    )
)

REM Run system check (已移除，改为在main_app.py中显示)
REM echo [1/2] Checking environment...
REM ..\python312\python.exe system_check.py
REM if %errorlevel% neq 0 (
REM     echo.
REM     echo Environment check failed
REM     pause
REM     exit /b 1
REM )

REM 检查并应用待处理的更新
if exist "_pending_update\_update_pending.json" (
    echo.
    echo ========= 正在应用更新 =========
    ..\python312\python.exe _apply_pending_update.py
    echo ==================================
    echo.
)

REM Start main program
echo [1/1] Starting main program...
echo.
..\python312\python.exe -u -c "import sys; sys.path.insert(0, '.'); from ui.main_app import main; main()"

pause
