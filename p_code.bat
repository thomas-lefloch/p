@echo off
setlocal

set "projects_root=C:\Users\%USERNAME%\Documents\projects"

if "%~1"=="" (
    echo Error : No project name was given.
    echo Usage: p_code.bat ^<project_name^>
    pause
    exit /b
)

set "project_dir=%projects_root%\%~1"

if exist "%project_dir%" (
    call code "%project_dir%" >nul
) else (
    echo Error: "%project_dir%" doesn't exist.
    pause
    exit /b
)