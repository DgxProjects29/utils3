from core.commands_templates import Utils3Exception
import core.settings as settings
import pyautogui
from dsmodule.drive_utilites import (CurrentClassFileUploader,
                                     DriveCommandTemplate)

SREENSHOT_DATA_FOLDER = 'data/dsmodule_data/last_screenshot.png'

class Command(DriveCommandTemplate):

    def execute_drive_command(self, drive):
        
        if self.params['region']:
            settings.set_setting('boundries', self.params['region'])
        elif self.params['reset']:
            settings.set_setting('boundries', [])
        else:
            try:
                boundries = settings.get_setting('boundries')
            except Utils3Exception:
                boundries = None
            
            pyautogui.hotkey('alt', 'tab')
            pyautogui.time.sleep(0.5)
            if boundries:
                pyautogui.screenshot(
                    SREENSHOT_DATA_FOLDER, 
                    region = boundries
                )
            else:
                pyautogui.screenshot(SREENSHOT_DATA_FOLDER)

            pyautogui.hotkey('alt', 'tab')

            curret_class_id = settings.get_setting('current_class')
            file_uploader = CurrentClassFileUploader(curret_class_id)
            file_uploader.set_tags(self.params['tags'])
            file_uploader.upload_file_from_path(
                drive = drive,
                path = SREENSHOT_DATA_FOLDER,
                ext = '.png'
            )

            title = file_uploader.get_title()
            print(f"file with title {title} was uploaded")
            # Back to the terminal
