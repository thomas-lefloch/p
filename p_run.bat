@echo off
setlocal

set "projects_root=C:\Users\%USERNAME%\Documents\projects"

REM Check if both arguments are provided
if "%~1"=="" (
    echo Error: You need to provide the project name.
    echo Usage: p_run.bat ^<project_name^> ^<script_name^>
    pause
    exit /b
)
if "%~2"=="" (
    echo Error: You need to provide the script name.
    echo Usage: p_run.bat ^<project_name^> ^<script_name^>
    pause
    exit /b
)

REM Set the project name and script name
set "project_name=%~1"
set "script_name=%~2"

REM Define the path to the project folder and the script
set "project_dir=%projects_root%\%project_name%"

REM Check if the project folder exists
if not exist "%project_dir%" (
    echo "Error: The project folder %project_dir% does not exist."
    exit /b
)

set "script_path=%project_dir%\%script_name%.bat"

REM Check if the script exists in the project folder
if not exist "%script_path%" (
    echo Error: The script "%script_name%" does not exist in the folder "%project_dir%".
    exit /b
)

REM Change directory to the project folder and execute the script
call "%script_path%"
pause