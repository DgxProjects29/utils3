import importlib
import click

class CommandInvoker(click.Command):

    def invoke(self, ctx):
        
        commands_path = 'dsmodule.commands.{name}'
        command_name = ctx.command.name
        #print(ctx.parent.command.nKame)
        try:

            command_module = importlib.import_module(
                commands_path.format(name = command_name)
            )
            command = command_module.Command(ctx.params)
            command.execute()
        
        except ImportError:
            
            print("Couldn't find command called {name}".format(
                name = command_name
            ))

class Utils3Exception(Exception):
    pass

class CommandTemplate:

    def __init__(self, params: dict):
        self.params = params

    def execute(self):
        try:
            self.execute_command()
        except Utils3Exception as utils3error:
            print(utils3error)
        except FileNotFoundError as not_found_err:
            print(not_found_err)
    
    # Let subsclass implement this method
    def execute_command(self):
        pass
