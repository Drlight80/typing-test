import Notepad

class show_farsi:
    def __init__(self , txt):
        self.txt = txt

    def show(self):
        Notepad.sh(self.txt)