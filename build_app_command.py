import os

modules_abbreviation = ['gm', 'ds']

# No commands will be register in data folders
command = "pyinstaller --onefile {hidden_imports} utils3.py"

def create_flag(hidden_module):
    return f"--hidden-import {hidden_module} "

hidden_imports = ""
for module_abbr in modules_abbreviation:
    module_name = f"{module_abbr}module"
    module_settings = f"{module_name}.module"
    module_click_commands = f"{module_name}.{module_abbr}_commands"
    commands_path = f"{module_name}/commands"

    hidden_imports += create_flag(module_name) \
    + create_flag(module_settings) + create_flag(module_click_commands) 

    for command_file in os.listdir(commands_path):
        if command_file.endswith(".py"):
            command_name = command_file.strip(".py")
            hidden_imports += create_flag(
                f"{module_name}.commands.{command_name}"
            )

print("Your command: ")
print(command.format(hidden_imports = hidden_imports))
