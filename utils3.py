import click
import core.register as register

@click.group()
def cli():
    pass

@cli.group(help="drive semester manager")
def ds():
    pass

# register_command(ds, 'dsmodule/commands', 'dsmodule.ds_commands')

if __name__ == '__main__':
    register.register_commands([
        {
            'command': ds,
            "module": 'dsmodule.module'
        }
    ])
    cli()
