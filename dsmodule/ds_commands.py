from core.commands_templates import CommandInvoker
import click
import datetime

@click.command(cls = CommandInvoker)
def login():
    
    """ 
    log in to drive

    """

@click.command(cls = CommandInvoker)
@click.argument('subjects_file', type=str)
@click.option('--rootname', 
    type = str, help = "root folder name for all the subjects. default is uninorte-semesters-3")
def init():

    """ 
    generate the subjects structure needed to create the folders in drive

    """


@click.command(cls = CommandInvoker)
def create():

    """
    upload the folders created by init command
    and store the ids of those folders

    """

@click.command(cls = CommandInvoker)
def ls():
    """
    List available subjects with its respective id,

    """

@click.command(cls = CommandInvoker)
@click.argument('subject_id', type=int)
@click.argument('part', type=int)
def set():
    """
    set the current class to upload screenshots and notes
    """



@click.command(cls = CommandInvoker)
@click.option('--region', nargs=4, type=int, 
    help = "set left, top, width, and height of the region to capture.\n" +
    "by default the whole screen")
@click.option('--reset/--no-reset', default=False, 
    help = 'remove region from screenshot')
@click.option('--tags', '-t' , type=str, multiple = True,
    help = "add tags for the screenshot")
def ts(region, tags, reset):

    """
    take a screenshot and upload to drive
    """


@click.command(cls = CommandInvoker)
@click.option('--tags', '-t' , type=str, multiple = True,
    help = "add tags for the note")
def note():

    """
    write a note and upload to drive

    """

def validate_parts(ctx, param, value):
    part = value
    double_point_idx = part.find(":")
    #Range part
    if part == 'all':
        # Empty lit means all classes
        parts = []
    elif double_point_idx != -1:
        try:
            from_ = int(part[:double_point_idx])
            to = int(part[double_point_idx + 1:])
            parts = [str(i) for i in range(from_, to + 1)]
        except:
            raise click.BadParameter(
                "Part format must be p or p1:p2, example: 2:4 means 'retrieve from part 2 to 4'"
            )
    else:
        parts = [str(part)]

    return parts

def validate_date(ctx, param, value):

    if value == 'now':
        return datetime.datetime.now().date()
    if value:
        str_date_formate = "%y-%m-%d"
        try:
            return datetime.datetime.strptime(value, str_date_formate).date()
        except:
            raise click.BadParameter(f"Date format must be: {str_date_formate}")
    else:
        return value

@click.command(cls = CommandInvoker)
def mergenotes():

    """
    merge all notes in current-class, ignore merged notes
    
    """

@click.command(cls = CommandInvoker)
@click.argument('subject_id', type = int)
@click.argument('parts', callback = validate_parts, type=str)
@click.option('--from-date', callback = validate_date, type=str)
@click.option('--to-date', callback = validate_date, type=str)
@click.option('--tags', '-t' , type=str, multiple = True)
@click.option('--copy/--no-copy', default=False)
def getnotes():

    """
    get notes, you can either copy to a sync folder or download to local
    
    """

@click.command(cls = CommandInvoker)
@click.argument('subject_id', type = int)
@click.argument('parts', callback = validate_parts, type=str)
@click.option('--from-date', callback = validate_date, type=str)
@click.option('--to-date', callback = validate_date, type=str)
@click.option('--tags', '-t' , type=str, multiple = True)
@click.option('--copy/--no-copy', default=False)
def getimgs():

    """
    get images, you can either copy to a sync folder or download to local
    
    """
@click.command(cls = CommandInvoker)
@click.argument('folder_id', type = str)
def syncfolder():
    """
    Set the drive folder to copy files after getting its content

    """

@click.command(cls = CommandInvoker)
@click.argument('tag', type = str)
@click.argument('from_date', callback = validate_date, type=str)
@click.argument('to_date', callback = validate_date, type=str)
def tagger():
    """
    Set the drive folder to copy files after getting its content

    """