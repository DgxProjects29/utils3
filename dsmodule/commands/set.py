from dsmodule.subjects import SubjectSubfolders, UserSubject
from core.commands_templates import CommandTemplate
import core.settings as settings


class Command(CommandTemplate):

    def execute_command(self):
        
        user_subject = UserSubject()
        subject_name = user_subject.get_subject_name_by_id(
            self.params['subject_id']
        )

        subject_subfolder_id = SubjectSubfolders()
        class_id = subject_subfolder_id.get_class_id(
            subject_name, 
            str(self.params['part'])
        )

        settings.set_setting('current_class', class_id)
        print(f"Current class set to {subject_name} and part {self.params['part']}")