import sys
import os
import subprocess
from tkinter import filedialog, messagebox
import pathlib

# https://stackoverflow.com/questions/41315873/attempting-to-resolve-blurred-tkinter-text-scaling-on-windows-10-high-dpi-disp
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

# To debug commands:
# import shutil
# print(shutil.which("powershell"))

exe_folder = os.path.dirname(sys.argv[0])
home_filepath = str(pathlib.Path(exe_folder, "home.conf"))
command_filepath = str(pathlib.Path(exe_folder, "commands.conf"))

# Reading available commands
LINE_MAX_CHAR_LENGTH = 1000
commands = {}
with open(command_filepath, "r") as f:
    line = f.readline(LINE_MAX_CHAR_LENGTH)
    while line != "":
        command_name, *command_array = line.strip().split("=")
        command = "=".join(command_array)
        if command in commands:
            commands[command_name] = commands[command]
        else:
            commands[command_name] = command
        line = f.readline(LINE_MAX_CHAR_LENGTH)


if len(sys.argv) < 2:
    print("Usage: p <command> [project_name]")
    print("Available commands:")
    print("\t- set-home")
    for command in commands:
        print(f"\t- {command}")
    sys.exit(0)
        
requested_command = sys.argv[1]

# set-home is the only hardcoded command.
if requested_command == "set-home":
    new_home = filedialog.askdirectory(mustexist=True)
    with open(home_filepath, "w") as f:
        f.write(str(pathlib.Path(new_home)))
    sys.exit(0)

# Reading project folder path
project_folderpath = ""
with open(home_filepath, "r") as f:
    project_folderpath = f.readline()

if project_folderpath == "":
    messagebox.showerror(
        title="Project folder not set !",
        message="No project folder found in 'home.conf'.",
        detail="run 'p set-home' to set a project folder",
    )
    sys.exit(1)

if not os.path.isdir(project_folderpath):
    messagebox.showerror(
        title="Invalid project folder !",
        message="Project folder found in 'home.conf' does not exist.",
        detail=project_folderpath,
    )
    sys.exit(1)

# User input, command
if requested_command not in commands:
    messagebox.showerror(
        title="Command not found !",
        message=f"Command '{requested_command}' was not found in 'commands.conf'.",
    )
    sys.exit(2)
    
command = commands[requested_command]

# Making sure the project exists to avoid weird behavior
project_path = pathlib.Path(project_folderpath, sys.argv[2])
if not project_path.exists():
    messagebox.showerror(
        title="Project not found !",
        message=str(project_path),
    )
    sys.exit(3)

# User input, project and args
if "${project_path}" in command:
    command = command.replace("${project_path}", str(project_path))

if "${remaining_args}" in command:
    command = command.replace("${remaining_args}", " ".join(sys.argv[3:]))

try:
    subprocess.run(command.strip(), shell=True)
except Exception:
    messagebox.showerror(
        title="Failed to run command !",
        message=command,
    )
    sys.exit(4)
