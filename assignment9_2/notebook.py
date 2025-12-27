class Notebook:

    def __init__(self, name):
        self.__name = name
        self.__notes = {}

    def get_name(self):
        return self.__name

    def add_or_update_note(self, title, body):
        self.__notes[title] = body

    def delete_note(self, title):
        if title not in self.__notes:
            return False
        del self.__notes[title]
        return True

    def delete_all_notes(self):
        self.__notes = {}

    def search_by_title(self, search_term):
        notes = []
        for title in self.__notes:
            if search_term in title:
                notes.append(title)
        return notes

    def search_by_body(self, search_term):
        notes = []
        for title in self.__notes:
            body = self.__notes[title]
            if search_term in body:
                notes.append(title)
        return notes

    def get_note_str(self, title):
        if title not in self.__notes:
            return ""
        note_str  = '\n# '+ title + '\n'
        note_str += self.__notes[title]
        note_str += '\n'
        return note_str

    def __str__(self):
        notebook_str = "\n"
        notebook_str += f"Notebook / {self.__name}\n"
        for title in self.__notes:
            notebook_str += self.get_note_str(title)
        if len(self.__notes) == 0:
            notebook_str += "\n(the notebook is empty)\n"
        return notebook_str

