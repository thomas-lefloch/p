@echo off
setlocal

set "projects_root=C:\Users\%USERNAME%\Documents\projects"

REM Check if both arguments are provided
if "%~1"=="" (
    echo Error: You need to provide a project name.
    echo Usage: p_run.bat ^<project_name^> ^<script_name^>
    pause
    exit /b
)
if "%~2"=="" (
    echo Error: You need to provide a script name.
    echo Usage: p_run.bat ^<project_name^> ^<script_name^>
    pause
    exit /b
)

set "project_name=%~1"
set "script_name=%~2"

set "project_dir=%projects_root%\%project_name%"

if not exist "%project_dir%" (
    echo Error: The project folder "%project_dir%" does not exist.
    exit /b
)

set "script_path=%project_dir%\%script_name%.bat"

if not exist "%script_path%" (
    echo Error: The script "%script_name%" does not exist in the folder "%project_dir%".
    exit /b
)

call "%script_path%"
pause