@echo off
setlocal

set "projects_root=C:\Users\%USERNAME%\Documents\projects"

REM Vérifie si un argument a été passé
if "%~1"=="" (
    echo Erreur : No project name was given.
    exit /b
)

REM Définit le nom du projet et le chemin du dossier correspondant
set "project_dir=%projects_root%\%~1"

REM Vérifie si le dossier existe
if exist "%project_dir%" (
    call code "%project_dir%" >nul
) else (
    echo Error: "%project_dir%" doesn't exist.
    exit /b
)