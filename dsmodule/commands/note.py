import tkinter as tk
import core.settings as settings
from dsmodule.drive_utilites import CurrentClassFileUploader, DriveCommandTemplate

class NotePad(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.text_written = ""
        self.textbox = tk.Text(self, height = 15, width = 100)
        self.textbox.pack()
        self.submitbutton = tk.Button(self, 
            text="OK", command=self.showinputtext)
        self.submitbutton.pack()

       
        windowWidth = self.winfo_reqwidth()
        windowHeight = self.winfo_reqheight()

        positionRight = int(self.textbox.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(self.textbox.winfo_screenheight()/2 - windowHeight/2)

        # Positions the window in the center of the page.
        self.geometry("+{}+{}".format(positionRight, positionDown))
        self.mainloop()

    def showinputtext(self):
        self.text_written = self.textbox.get("1.0", "end-1c")
        self.destroy()

class Command(DriveCommandTemplate):

    def execute_drive_command(self, drive):
        
        notepad = NotePad()
        note = notepad.text_written

        if note:
            curret_class_id = settings.get_setting('current_class')
            file_uploader = CurrentClassFileUploader(curret_class_id)
            file_uploader.set_tags(self.params['tags'])
            file_uploader.upload_file_from_text(drive, note)

            title = file_uploader.get_title()
            print(f"file with title {title} was uploaded")
        else:
            print("Nothing to upload")




