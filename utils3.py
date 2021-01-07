import click
import importlib
import os

DS_COMMANDS_PATH = "dsmodule/commands"
DS_MODULE_DATA = {
    'name': 'dsmodule_data',
    'childs': [
        {
            'name': 'credentials',
            'childs': []
        },
        {
            'name': 'notes',
            'childs': []
        },
        {
            'name': 'screenshots',
            'childs': []
        },
    ]
}

def create_folder_recursive(path, folder_node):

    childs = folder_node['childs']
    if childs:
        for child in childs:
            create_folder_recursive(os.path.join(path, child['name']), child)
    else:
        if not os.path.exists(path):
            os.makedirs(path)

def register_command(click_command, commands_path, module_name):

    commands_module = importlib.import_module(module_name)

    for command_file in os.listdir(commands_path):
        if command_file.endswith(".py"):
            command_name = command_file.strip(".py")
            click_command.add_command(commands_module.__dict__[command_name])

def init_utils3():
    if not os.path.exists('data'):
        os.mkdir('data')
    
    if not os.path.exists('data/settings.json'):
        with open('data/settings.json', 'w') as settings_file:
            settings_file.write('{}')
    
    create_folder_recursive(
        os.path.join('data', DS_MODULE_DATA['name']), 
        DS_MODULE_DATA
    )

@click.group()
def cli():
    pass

@cli.group(help="drive semester manager")
def ds():
    pass

register_command(ds, 'dsmodule/commands', 'dsmodule.ds_commands')

if __name__ == '__main__':
    init_utils3()
    cli()
