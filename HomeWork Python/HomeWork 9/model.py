from copy import deepcopy


class Contact:
    def __init__(self, name: str, phone: str, comment: str):
        self.name = name
        self.phone = phone
        self.comment = comment

    def to_str(self):
        return f'{self.name} {self.phone} {self.comment}'.lower()

    def to_list(self):
        return [self.name, self.phone, self.comment]

    def show(self, max_n: int, max_p: int, max_c: int):
        return f'{self.name: <{max_n}} {self.phone: <{max_p}} {self.comment: <{max_c}}'

class PhoneBook:

    def __init__(self, phone_book: dict[int, Contact] = None, path: str = 'phones.txt'):
        if phone_book is None:
            self.phone_book = {}
            self.id = 1
        else:
            self.phone_book = phone_book
            self.id = max(self.phone_book) + 1
        self.path = 'phones.txt'
        self.original_pg = {}

    def open_file(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            contacts = file.readlines()
        for contact in contacts:
            uid, name, phone, comment = contact.strip().split(';')
            self.phone_book[int(uid)] = Contact(name, phone, comment)
        self.id = max(self.phone_book) + 1
        self.original_pg = deepcopy(self.phone_book)

    def save_file(self):
        with open(self.path, 'w', encoding='UTF-8') as file:
            contacts = []
            for uid, contact in self.phone_book.items():
                contacts.append(';'.join([str(uid), *contact]))
            contacts = '\n'.join(contacts)
            file.write(contacts)
        self.original_pg = deepcopy(self.phone_book)

    def add_contact(self, new: list[str]):
        self.phone_book[self.id] = Contact(*new)
        self.id += 1

    def search(self, word: str) -> dict[int, Contact]:
        result = {}
        for uid, contact in self.phone_book.items():
            if word.lower() in contact.to_str():
                result[uid] = contact
        return result

    def change(self, uid: int, new: list[str]) -> str:
        contact = self.phone_book.get(uid).to_list()
        for i in range(len(contact)):
            if new[i] != '':
                contact[i] = new[i]
        self.phone_book[uid] = Contact(*contact)
        return contact[0]

    def delete(self, uid: int) -> str:
        return self.phone_book.pop(uid).name

    def max_len(self):
        result = [[], [], []]
        for contact in self.phone_book.values():
            for i, item in enumerate(contact.to_list()):
                result[i].append(item)
        return tuple(map(lambda x: len(max(x, key=len)), result))
