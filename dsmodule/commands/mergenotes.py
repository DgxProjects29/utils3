import textwrap

import core.settings as settings
from dsmodule.drive_utilites import (CurrentClassFileUploader,
                                     DriveCommandTemplate, FileDonwloader)
from dsmodule.filters import filter_by_extension, filter_by_tags


class Command(DriveCommandTemplate):

    def execute_drive_command(self, drive):

        class_id = settings.get_setting('current_class')

        filter_funcs = [
            filter_by_extension('txt'), 
            filter_by_tags(set(['mergednote']), reverse = True)
        ]

        self.merged_notes = ""
        file_downloader = FileDonwloader([class_id, ])
        file_downloader.set_filters_funcs(filter_funcs)
        file_downloader.get_content_file(drive, self.add_note)
        
        if self.merged_notes:
            current_class_uploader = CurrentClassFileUploader(class_id)
            current_class_uploader.set_tags(['mergednote'])
            current_class_uploader.upload_file_from_text(
                drive, 
                self.merged_notes
            )
            title = current_class_uploader.get_title()
            print(f"file with title {title} was uploaded")
        else:
            print("Nothing to upload") 

    def add_note(self, file):
        title = file['title']
        date = file['createdDate']
        print(f"Adding the following file: {title}")
        content = file.GetContentString()
        self.merged_notes += self.get_note_item(date, title, content)

    def get_note_item(self, date, title ,content):
        template =  textwrap.dedent(
            """
            Date: {date}
            Title: {title}
            ----------------------------------
            {content}
            """
        )
        template = template.format(
            date = date,
            title = title,
            content = content
        )
        return template
