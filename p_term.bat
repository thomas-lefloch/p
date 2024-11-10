@echo off
set "project_path=C:\Users\%USERNAME%\Documents\projects"

if "%~1"=="" (
    echo Please provide a project name as the first argument.
    echo Usage: p_run.bat ^<project_name^>
    pause
    exit /b
)

set "full_path=%project_path%\%~1"

if not exist "%full_path%" (
    echo The specified project does not exist: "%full_path%"
    pause
    exit /b
)

start cmd /k "cd /d %full_path%"
