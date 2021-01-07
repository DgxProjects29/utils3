from core.commands_templates import Utils3Exception
import dsmodule.commons as commons

DS_USER_SUBJECS = 'data/dsmodule_data/ds-subjects.json'
DS_STRUCTURE = 'data/dsmodule_data/ds-structure.json'
DS_SUBJECT_SUBFOLDERS = 'data/dsmodule_data/ds-subfolders-id.json'

class UserSubject:

    def __init__(self):
        
        self.subjects = commons.load_data_from_json_file(DS_USER_SUBJECS)

    def get_subjects_names(self):
        return [subject['name'] for subject in self.subjects]

    def get_subject_name_by_id(self, subject_id):
        subjects_lenght = len(self.subjects)
        if subject_id > subjects_lenght or subject_id < 1:
            raise Utils3Exception("Subject was not found")
        return self.subjects[subject_id - 1]["name"]


class SubjectSubfolders:

    def __init__(self):

        self.subject_sub_folders = commons.load_data_from_json_file(
            DS_SUBJECT_SUBFOLDERS
        )

    def get_subject_subfolders(self, subject_name):
        return self.subject_sub_folders[subject_name]

    def get_class_id(self, subject_name, part):
        subject_classes = self.subject_sub_folders[subject_name]['classes']
        if part in subject_classes:
            return subject_classes[part]
        else:
            raise Utils3Exception("Part was not found")

    def get_class_ids(self, subject_name, parts):
        class_ids = []
        for part in parts:
            class_ids.append(self.get_class_id(subject_name, part))
        return class_ids

    def get_all_classes(self, subject_name):
        subject_classes = self.subject_sub_folders[subject_name]['classes']
        return list(subject_classes.values())

    @staticmethod
    def save_subject_subfolders(end_points):
        
        subject_subfolders = {}
        for end_point_pair in end_points:

            path = end_point_pair[0]
            folder_id = end_point_pair[1]

            slipted_path = path.split('/')

            subject_name = slipted_path[1]
            n_corte = (slipted_path[2].split('-'))[1]

            folder_section = slipted_path[3]
            
            if subject_name not in subject_subfolders:
                subject_subfolders[subject_name] = {
                    'classes': {},
                    'assigments': {},
                    'documents': {},
                }

            subject_subfolders[subject_name][folder_section].update(
                {n_corte: folder_id}
            )
        
        commons.write_json_from_dict(DS_SUBJECT_SUBFOLDERS, subject_subfolders)

    
