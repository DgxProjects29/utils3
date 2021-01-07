from core.commands_templates import CommandTemplate
import core.settings as settings 

class Command(CommandTemplate):

    def execute_command(self):
        
        settings.set_setting('sync_folder', self.params['folder_id'])