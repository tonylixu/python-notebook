from notebook import Notebook
from note import Note

class Menu:
    '''
    Display a menu and respond to choices when run.
    '''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def display_menu(self):
        print('''
        1. Show all notes
        2. Search notes
        3. Add note
        4. Modify note
        5. Quit
        ''')

