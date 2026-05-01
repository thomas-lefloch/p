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
commands: dict[str, list[str]] = {}
with open(command_filepath, "r") as f:
    line = f.readline(LINE_MAX_CHAR_LENGTH)
    while line != "":
        command_name, *command_array = line.strip().split("=")
        command = "=".join(command_array)
        # aliases
        if command in commands: 
            commands[command_name] = commands[command]
        else:
            commands[command_name] = command.split()
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
        title="(p) Project folder not set !",
        message="No project folder found in 'home.conf'.",
        detail="run 'p set-home' to set a project folder",
    )
    sys.exit(1)

if not os.path.isdir(project_folderpath):
    messagebox.showerror(
        title="(p) Invalid project folder !",
        message="Project folder found in 'home.conf' does not exist.",
        detail=project_folderpath,
    )
    sys.exit(1)

# User input, command
if requested_command not in commands:
    messagebox.showerror(
        title="(p) Command not found !",
        message=f"Command '{requested_command}' was not found in 'commands.conf'.",
    )
    sys.exit(2)
    
command = commands[requested_command]

if len(sys.argv) < 3:
    messagebox.showerror(
        title="(p) Project Not found !",
        message=f"You must provide a project name.",
    )
    
project_name = sys.argv[2]

# Making sure the project exists to avoid weird behavior
project_path = pathlib.Path(project_folderpath, project_name)
if not project_path.exists():
    messagebox.showerror(
        title="(p) Project not found !",
        message="Project not found !",
        detail=str(project_path),
    )
    sys.exit(3)

# User input, project and args
for i in range(len(command)):
    if command[i] == "${project_path}":
        command[i] = str(project_path)
    elif command[i] == "${remaining_args}":
        command[i] = " ".join(sys.argv[3:])

try:
    subprocess.run(command)
except Exception:
    messagebox.showerror(
        title="(p) Failed to run command !",
        message="Failed to run command !",
        detail=" ".join(command),
    )
    sys.exit(4)
