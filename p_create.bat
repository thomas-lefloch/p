@echo off
chcp 65001 >nul
setlocal

set "projects_root=C:\Users\%USERNAME%\Documents\projects"

REM Vérifie si un argument a été passé, sinon demande à l'utilisateur
if "%1"=="" (
    set /p project_name="Enter the name of the project : "
) else (
    set "project_name=%1"
)

if "%project_name%"=="" (
    echo Error: No project name given
    echo Usage: p_create.bat ^<project_name^>
    pause
    exit /b
)

if not exist "%projects_root%" (
    mkdir "%projects_root%" >nul
)

if not exist "%projects_root%" (
    echo Error:  Making projects folder: "%projects_root%"
    pause
    exit /b
)

set "project_path=%projects_root%\%project_name%"
if exist project_path (
    echo Error: Folder "%project_name%" already exists.
    pause
    exit /b
)

mkdir "%project_path%"