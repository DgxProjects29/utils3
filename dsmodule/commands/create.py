import concurrent.futures
import os
import dsmodule.commons as commons
from dsmodule.drive_utilites import (DriveCommandTemplate,
                                        create_drive_folder_and_get_id)
from dsmodule.subjects import DS_STRUCTURE, SubjectSubfolders

class Command(DriveCommandTemplate):

    def execute_drive_command(self, drive):
        if os.path.exists(DS_STRUCTURE):
            print("Subjects were created successfully")
        else:
            self.drive = drive
            self.end_points = []

            subjects_drive_structure = commons.load_data_from_json_file(
                DS_STRUCTURE
            )

            parent_name = subjects_drive_structure['name']
            parent_id = create_drive_folder_and_get_id(
                drive = self.drive, 
                title = parent_name
            )

            self.create_drive_structure_recursive(
                parent_id, 
                parent_name,
                subjects_drive_structure
            )

            print(self.end_points)
            SubjectSubfolders.save_subject_subfolders(self.end_points)

    def create_drive_structure_recursive(self, parent_id, path, parent_folder):

        childs = parent_folder['childs']

        if childs:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                for child in childs:

                    title = child['name']

                    print("Creating folder with name {0} and root id of {1}"
                        .format(title, parent_id)
                    )

                    folder_id = create_drive_folder_and_get_id(
                        drive = self.drive,
                        title = title,
                        parent_id = parent_id
                    )

                    new_path = path + '/' + title

                    args = (folder_id, new_path, child)

                    executor.submit(
                        self.create_drive_structure_recursive,
                        *args
                    )
        else:
            self.end_points.append((path, parent_id))
