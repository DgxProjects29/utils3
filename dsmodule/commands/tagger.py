from dsmodule.drive_utilites import DriveCommandTemplate, FileDonwloader
from dsmodule.filters import filter_by_date
import core.settings as settings

SREENSHOT_DATA_FOLDER = 'data/dsmodule_data/last_screenshot.png'

class Command(DriveCommandTemplate):

    def execute_drive_command(self, drive):

        class_id = settings.get_setting('current_class')

        filter_funcs = [
            filter_by_date(self.params['from_date'], self.params['to_date'])
        ]

        self.merged_notes = ""
        file_downloader = FileDonwloader([class_id, ])
        file_downloader.set_filters_funcs(filter_funcs)
        file_downloader.get_content_file(drive, self.add_tag)

    def add_tag(self, file):
        print(f"Tagging the following file: {file['title']}")
        extension = '.' + file['fileExtension']
        new_title = file['title'].replace(
            extension,
            '-' + self.params['tag'] + extension
        )
        file['title'] =  new_title
        file.Upload()