from core.commands_templates import CommandTemplate
import dsmodule.commons as commons
from dsmodule.subjects import DS_USER_SUBJECS, DS_STRUCTURE


class Command(CommandTemplate):

    def execute_command(self):

        rootname = self.params['rootname']
    
        if not rootname:
            rootname = 'uninorte-semester-3'
        
        ds_structure = {
            'name': rootname,
            'childs': []
        }

        subjects = commons.load_data_from_json_file(
            self.params['subjects_file']
        )

        for subject in subjects:
            ds_structure['childs'].append(
                {
                    'name': subject["name"],
                    'childs': self.get_subject_structure(subject["parts"])
                }
            )

        commons.write_json_from_dict(DS_STRUCTURE, ds_structure)
        commons.write_json_from_dict(DS_USER_SUBJECS, subjects)

        print("Ds Structure created, run create command to upload folders to drive")

    def get_part_structure(self):

        folders_of_part = ['classes', 'assigments', 'documents']
        childs_of_part = []

        for folder in folders_of_part:
            childs_of_part.append(
                {
                    'name': folder,
                    'childs': []
                }
            )

        return childs_of_part

    def get_subject_structure(self, n_parts):
        childs_of_subjects = []
        part_structure = self.get_part_structure()
        for i in range(1, n_parts + 1):
            childs_of_subjects.append(
                {
                    'name': 'part-{0}'.format(i),
                    'childs': part_structure
                }
            )
        return childs_of_subjects
