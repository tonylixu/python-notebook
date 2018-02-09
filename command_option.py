from notebook import Notebook
from note import Note
import sys

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

    def run(self):
        '''
        Display the menu and respond to choices.
        '''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(str(choice))
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        '''
        Display all notes
        '''
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("Note {0}: Tags:{1}\nMemo: {2}".format(note.id, note.tags, note.memo))

    def search_notes(self):
        '''
        Search notes that contains a given string
        '''
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        '''
        Add a new note
        '''
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")

    def modify_note(self):
        note_id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(note_id, memo)
        if tags:
            self.notebook.modify_tags(note_id, tags)

    def quit(self):
        print("Thanks for using notebook today")
        sys.exit(0)

if __name__ == '__main__':
    Menu().run()