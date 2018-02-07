from .note import Note

class Notebook:
    '''
    Represent a collection of notes that can be tagged, modified
    and searched.
    '''

    def __init__(self):
        '''Initialize a empty notebook list'''
        self.notes = []

    def new_note(self, memo, tags=''):
        '''
        Create a new note and append to the list.

        :param memo: Memo in string format
        :param tags: tags in string format
        :return None
        '''
        note = Note(memo, tags)
        self.notes.append(note)

    def modify_memo(self):
        pass

    def modify_tags(self):
        pass

    def search(self):
        pass