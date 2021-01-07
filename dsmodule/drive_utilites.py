from concurrent.futures import ThreadPoolExecutor
import datetime

from core.commands_templates import CommandTemplate
from pydrive.auth import (AuthenticationError, AuthenticationRejected,
                          GoogleAuth, InvalidCredentialsError)
from pydrive.drive import GoogleDrive

CREDENTIALS_FOLDER_PATH = "data/dsmodule_data/credentials/mycreds.json"

class DriveCommandTemplate(CommandTemplate):

    def execute_command(self):

        try:
            gauth = GoogleAuth()
            gauth.LoadCredentialsFile(CREDENTIALS_FOLDER_PATH)

            if gauth.credentials is None:
                gauth.LocalWebserverAuth()
            elif gauth.access_token_expired:
                #id this does not work usee localwebserver
                gauth.LocalWebserverAuth()
                # gauth.Refresh()
            else:
                gauth.Authorize()
            
            gauth.SaveCredentialsFile(CREDENTIALS_FOLDER_PATH)
        
            drive = GoogleDrive(gauth)

            self.execute_drive_command(drive)
        except InvalidCredentialsError as e:
            print(str(e))
        except AuthenticationRejected as e:
            print(str(e))
        except AuthenticationError as e:
            print(str(e))
    
    def execute_drive_command(self, drive):
        pass


def create_drive_folder_and_get_id(drive, title, parent_id = None):

    folder_metadata = {   
        'title' : title,
        'mimeType' : 'application/vnd.google-apps.folder'
    }

    if parent_id:
        folder_metadata.update(
            {'parents': [{'kind': 'drive#fileLink', 'id': parent_id}]}
        )

    folder = drive.CreateFile(folder_metadata)
    folder.Upload()

    return folder['id']

class FileDonwloader:

    def __init__(self, parent_ids):
        
        self.filter_funcs = []
        self.parent_ids = parent_ids

    def get_content_file(self, drive, func):
        
        file_scraper = FileSraper(self.parent_ids, self.filter_funcs)
        file_scraper.find_files(drive)
        files = file_scraper.get_files()

        with ThreadPoolExecutor() as executor:
            for file in files:
                executor.submit(func, file)

    def set_filters_funcs(self, filter_funcs):
        self.filter_funcs = filter_funcs

class FileSraper:

    def __init__(self, parent_ids, filter_funcs = []):
        self.parent_ids = parent_ids
        self.filter_funcs = filter_funcs

        self.files = []

    def find_files(self, drive):

        with ThreadPoolExecutor() as executor:
            for parent_id in self.parent_ids:
                executor.submit(self.add_files, drive, parent_id)

    def add_files(self, drive, parent_id):
        file_list = drive.ListFile(
            {
                'q': f"'{parent_id}' in parents and trashed=false"
            }
        ).GetList()

        for file in file_list:
            if all(func(file) for func in self.filter_funcs):
                self.files.append(file)

    def get_files(self):
        return self.files


class CurrentClassFileUploader:

    def __init__(self, class_id) -> None:
        
        self.class_id = class_id
        current_date = datetime.datetime.now()
        self.title = current_date.strftime("%y%m%d%H%M%S")

    def set_tags(self, tags = []):
        for tag in tags:
            self.title += f"-{tag}"

    def upload_file_from_path(self, drive, path, ext):

        drive_file = drive.CreateFile(
            {
                'title': self.title + ext,
                'parents': [{'id': self.class_id}]
            }
        )

        drive_file.SetContentFile(path)
        drive_file.Upload()

    def upload_file_from_text(self, drive, text):

        drive_file = drive.CreateFile(
            {
                'title': self.title + ".txt",
                'parents': [{'id': self.class_id}]
            }
        )

        drive_file.SetContentString(text)
        drive_file.Upload()

    def get_title(self):
        return self.title
