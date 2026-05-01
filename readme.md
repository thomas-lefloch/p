# P
A small and simple project "manager"

The original intention was to create an extensible program that allow you to "manage" (create, open, ...) projects.

A project is just a folder inside your `home`. Your home is the parent folder of all your projects.

Your `home` is define in [./home.conf](./home.conf). You can modify it with the set-home command. This is the first command you should run.  
```sh 
p set-home
```

## Usage
```sh
p <command_name> <project_name>
```
Will execute the given command with the given project. `Commands` are defined in [./commands.conf](./commands.conf) 

Open the windows file explorer at the wonderful_project folder location:
```sh
p explorer wonderful_project
```

## Defaults commands
On Linux and MacOS, the only default command is `set-home`.  
You will need to create the `./commands.conf` file. See [Creating new commands chapter](##creating-new-commands)

Default commands on Windows:
- `set-home`: Allows you to easily change the root of your projects folders. (the only hardcoded command)
- `create`: mkdir 
- `explorer`: Open windows explorer at the project location
- `vscode` (or `code`): Opens VSCode at the project location
- `powershell` (or `term`): Opens a powershell at the project location

You can modify / add new commands by modifying [./commands.conf](./commands.conf)
I strongly encourage you to customise the commands to fit your habits. 

## Creating new commands 

### How To
Let's add a new_command that is just a ls. Add a line to the commands.conf like so:
```conf
new_command=ls ${project_path} ${remaining_args}
``` 
the first `=` is the separator. So = in command names are not supported. Spaces in command names are not supported either.  
After saving the file you can run.  
```sh 
p new_command <project_name> -a
```
Commands are run via python subprocess.run(command)

### Variables  
`${project_path}` : full path of the requested project folder (eg: <home>/<project_name>)  
`${remaining_args}` : Options added after a project name.

### Aliases
You can create multiple name for the same command by referring to the name of the command.
Aliases must be placed after the original command.
```conf
vscode=code.CMD ${project_path}
code=vscode
```
