import sys
import os
import subprocess
from tkinter import filedialog, messagebox

# https://stackoverflow.com/questions/41315873/attempting-to-resolve-blurred-tkinter-text-scaling-on-windows-10-high-dpi-disp
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

# To debug commands:
# import shutil
# print(shutil.which("powershell"))

home_filepath = "./home.conf"
command_filepath = "./commands.conf"

requested_command = sys.argv[1]

# set-home is the only hardcoded command.
if requested_command == "set-home":
    new_home = filedialog.askdirectory(mustexist=True)
    with open(home_filepath, "w") as f:
        f.write(new_home)
    exit(0)


# Reading project fodler path
project_folderpath = ""
with open(home_filepath, "r") as f:
    project_folderpath = f.readline()

if project_folderpath == "":
    messagebox.showerror(
        title="Project folder not set !",
        message="No project folder found in 'home.conf'.",
        detail="run 'p set-home' to set a project folder",
    )
    exit(1)

if not os.path.isdir(project_folderpath):
    messagebox.showerror(
        title="Invalid project folder !",
        message="Project folder found in 'home.conf' does not exist.",
        detail=project_folderpath,
    )
    exit(1)


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


if requested_command not in commands:
    messagebox.showerror(
        title="Command not found !",
        message=f"Command '{requested_command}' was not found in 'commands.conf'.",
    )
    exit(2)

command = commands[requested_command]

# User input
if "${project_path}" in command:
    command = command.replace("${project_path}", f"{project_folderpath}/{sys.argv[2]}")

if "${remaining_args}" in command:
    command = command.replace("${remaining_args}", " ".join(sys.argv[3:]))

subprocess.run(command)
