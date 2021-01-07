import core.settings as settings
from dsmodule.drive_utilites import DriveCommandTemplate, FileDonwloader
from dsmodule.subjects import UserSubject, SubjectSubfolders
from dsmodule.filters import filter_by_date, filter_by_extension, filter_by_tags

SCRENSHOOTS_PATH = 'data/dsmodule_data/screenshots/'

class Command(DriveCommandTemplate):

    def execute_drive_command(self, drive):

        self.drive = drive

        user_subject = UserSubject()
        subject_subfolders = SubjectSubfolders()
        
        subject_name = user_subject.get_subject_name_by_id(
            self.params['subject_id']
        )

        if self.params['parts']:
            parent_ids = subject_subfolders.get_class_ids(
                subject_name, 
                self.params['parts']
            )
        else:
            parent_ids = subject_subfolders.get_all_classes(subject_name)

        file_downloader = FileDonwloader(parent_ids)

        filter_funcs = [
            filter_by_extension('png'),
            filter_by_tags(set(self.params['tags'])),
            filter_by_date(self.params['from_date'], self.params['to_date'])
        ]

        if self.params['copy']:
            action_func = self.copy_to_sync_folder
        else:
            action_func = self.download_file

        file_downloader.set_filters_funcs(filter_funcs)
        file_downloader.get_content_file(self.drive, action_func)

    def download_file(self, file):
        print(f"Downloading the following image: {file['title']}")
        file.GetContentFile(
            SCRENSHOOTS_PATH + file['title']
        )

    def copy_to_sync_folder(self, file):

        sync_folder = settings.get_setting('sync_folder')

        print(f"Copy the following image: {file['title']}")
        self.drive.auth.service.files().copy(
            fileId = file['id'],
            body = {
                "parents": [
                    {
                        "kind": "drive#fileLink",
                        "id": sync_folder
                    }
                ], 
                'title': file['title']
                }
            ).execute()