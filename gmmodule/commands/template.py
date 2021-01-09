import pyperclip
from core.commands_templates import CommandTemplate, Utils3Exception
import core.settings as settings

class Command(CommandTemplate):

    def execute_command(self):

        normal_email = "Estimad{0!s} profesor{1!s},\n\n" \
        "El siguiente correo tiene como propósito {2!s}" \
        "\n\n<body>\n\nAtentamente {3!s}"

        is_male = self.params['male']

        char_sex = 'o' if is_male else 'a'
        char_sex_2 = '' if is_male else 'a'

        try:
            gmail_user = settings.get_setting('gmail_user')
        except Utils3Exception:
            gmail_user = '<user>'
        
        baked_email = ''
        if self.params['type'] == 'normal':
            baked_email = normal_email.format(
                char_sex,
                char_sex_2,
                self.params['purpose'],
                gmail_user
            )
        
        print(baked_email)
        pyperclip.copy(baked_email)