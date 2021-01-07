from core.commands_templates import CommandTemplate
from dsmodule.subjects import UserSubject

class Command(CommandTemplate):

    def execute_command(self):
        
        user_subject = UserSubject()
        subject_names = user_subject.get_subjects_names()

        print("--- Start of the list ---")

        for subject_id, subject_name in enumerate(subject_names, start = 1):
            print(f"ID: {subject_id} Name: {subject_name}")
        
        print("--- End of the list ---")
