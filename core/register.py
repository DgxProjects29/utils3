import os
import importlib

def create_folder_recursive(path, folder_node):

    childs = folder_node['childs']
    if childs:
        for child in childs:
            create_folder_recursive(os.path.join(path, child['name']), child)
    else:
        if not os.path.exists(path):
            os.makedirs(path)

def register_command(click_command, commands_path, module_name, module_data):

    if module_data:
        data_path = os.path.join('data', module_data['name'])
        create_folder_recursive(data_path, module_data)

    commands_module = importlib.import_module(module_name)

    for command_file in os.listdir(commands_path):
        if command_file.endswith(".py"):
            command_name = command_file.strip(".py")
            click_command.add_command(commands_module.__dict__[command_name])


def create_data_and_settings():
    if not os.path.exists('data'):
        os.mkdir('data')
    
    if not os.path.exists('data/settings.json'):
        with open('data/settings.json', 'w') as settings_file:
            settings_file.write('{}')

def register_commands(modules_data):

    create_data_and_settings()

    for module_data in modules_data:
        click_command = module_data['command']
        module = importlib.import_module(module_data['module'])
        register_command(
            click_command, 
            module.COMMANDS_PATH,
            module.CLICK_COMMANDS_MODULE,
            module.MODULE_DATA
        )