phone_book = {}
path = 'phones.txt'


def next_id():
    return max(phone_book) + 1


def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        contacts = file.readlines()
    for contact in contacts:
        uid, name, phone, comment = contact.strip().split(';')
        phone_book[int(uid)] = [name, phone, comment]


def save_file():
    with open(path, 'w', encoding='UTF-8') as file:
        contacts = []
        for uid, contact in phone_book.items():
            contacts.append(';'.join([str(uid), *contact]))
        contacts = '\n'.join(contacts)
        file.write(contacts)


def add_contact(new: list[str]):
    phone_book[next_id()] = new


def search(word: str) -> dict[int, list[str]]:
    result = {}
    for uid, contact in phone_book.items():
        if word.lower() in ''.join(contact).lower():
            result[uid] = contact
    return result


def change(uid: int, new: list[str]) -> str:
    contact = phone_book.get(uid)
    for i in range(3):
        if new[i] != '':
            contact[i] = new[i]
    phone_book[uid] = contact
    return contact[0]


def delete(uid: int) -> str:
    return phone_book.pop(uid)[0]



