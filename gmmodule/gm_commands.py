from core.commands_templates import CommandInvoker
import click

@click.command(cls = CommandInvoker)
@click.option('--type', '-t' ,
    type = click.Choice(['normal', ], case_sensitive=False),
    default = 'normal',
    help = "choose a email format")
@click.option('--male/--no-male', 
    default = True,
    help = "choose a email format")
@click.option('--purpose', '-p',
    type = str,
    default = '<purpose>',
    help = "the purpose of the email")
def template():

    """ 
    copy to your clipboard a email template to send 

    """

@click.command(cls = CommandInvoker)
@click.argument('gmail_user', type=str)
def user():

    """ 
    save your gmail user to sign your template emails

    """