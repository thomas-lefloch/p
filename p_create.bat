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

REM Vérifie si le nom du projet est vide
if "%project_name%"=="" (
    echo Error: No project name given
    exit /b
)

REM Crée le dossier projects s'il n'existe pas déjà
if not exist "%projects_root%" (
    mkdir "%projects_root%" >nul
)

if not exist "%projects_root%" (
    echo Error:  Making project folder: "%projects_root%"
)

set "project_path=%projects_root%\%project_name%"
if exist project_path (
    echo Error: Folder already exists.
    exit /b
)

mkdir "%project_path%"