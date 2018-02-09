from note import Note

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

    def modify_memo(self, note_id, memo):
        '''
        Find the note with the given id and change its
        memo to the given value.

        :param note_id: Integer, note id
        :param memo: Memo in string format
        :return None
        '''
        for note in self.notes:
            if note.id == int(note_id):
                note.memo = memo
                break

    def modify_tags(self, note_id, tags):
        '''
        Find the note with the given id and change its
        tags to the given value.

        :param note_id: Integer, note id
        :param tags: Tags in string format
        :return None
        '''
        for note in self.notes:
            if note.id == int(note_id):
                note.tags = tags
                break

    def search(self, filter):
        '''
        Find all notes that contains the given filter
        '''
        return [note for note in self.notes if note.match(filter)]
