from core.commands_templates import CommandTemplate
import core.settings as settings

class Command(CommandTemplate):

    def execute_command(self):

        settings.set_setting('gmail_user', self.params['gmail_user'])
        print("Gmail user register as ", self.params['gmail_user'])