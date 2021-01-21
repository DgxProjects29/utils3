import click
import core.register as register

@click.group()
def cli():
    pass

@cli.group(help="drive semester manager")
def ds():
    pass

@cli.group(help="gmail utilities")
def gm():
    pass


if __name__ == '__main__':
    register.register_commands([
        {
            'command': ds,
            "module": 'dsmodule.module'
        },
        {
            'command': gm,
            "module": 'gmmodule.module'
        }
    ])
    cli()
