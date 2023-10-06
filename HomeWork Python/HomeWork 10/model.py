from copy import deepcopy


class Notes:
    def __int__(self, title: str, notes: str):
        self.title = title
        self.notes = notes

    def to_str(self):
        return f'{self.title} {self.notes}'.lower()

    def to_list(self):
        return [self.title, self.notes]

    def show(self, max_t: int, max_n: int):
        return f'{self.title: <{max_t}>} {self.notes: <{max_n}>}'


class NotesRedactor:
    def __init__(self, note: dict[int, Notes] = None, path: str = 'notes.txt'):
        if note is None:
            self.note = {}
            self.id = 1
        else:
            self.note = note
            self.id = max(self.note) + 1
        self.path = 'notes.txt'
        self.original_nt = {}

    def open_file(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            notes = file.readline()
        for note in notes:
            uid, title, notes = note.strip().split(';')
            self.note[int(uid)] = Notes(title, notes)
        self.id = max(self.note) + 1
        self.original_nt = deepcopy(self.note)

    def save_file(self):
        with open(self.path, 'w', encoding='UTF-8') as file:
            notes = []
            for uid, note in self.note.items():
                notes.append(';'.join([str(uid), *note]))
            notes = '\n'.join(notes)
            file.write(notes)
        self.original_nt = deepcopy(self.note)

    def add_note(self, new: list[str]):
        self.note[self.id] = Notes(*new)
        self.id += 1

    def search(self, word: str) -> dict[int, Notes]:
        result = {}
        for uid, note in self.note.items():
            if word.lower() in note.to_str():
                result[uid] = note
        return result

    def change(self, uid: int, new: list[str]) -> str:
        note = self.note.get(uid).to_list()
        for i in range(len(note)):
            if new[i] != '':
                note[i] = new[i]
        self.note[uid] = Notes(*note)
        return note[0]

    def delete(self, uid: int) -> str:
        return self.note.pop(uid).title

    def max_len(self):
        result = [[], []]
        for note in self.note.values():
            for i, item in enumerate(note.to_list()):
                result[i].append(item)
        return tuple(map(lambda x: len(max(x, key=len)), result))
