import text
from model import NotesRedactor


def print_msg(msg: str):
    print('\n' + '=' * len(msg))
    print(msg)
    print('=' * len(msg) + '\n')


def show_menu(menu: list[str]) -> int:
    for i, item in enumerate(menu):
        if i != 0:
            print(f'{i}. {item}')
        else:
            print(item)
    input_select = input('Выберите пункт меню: ')
    while True:
        if input_select.isdigit() and 0 < int(input_select) < len(menu):
            return int(input_select)
        input_select = input(text.menu_error)


def show_notes(book: NotesRedactor, msg: str):
    max_count = [0, 0]
    if book:
        max_t, max_n = book.max_len()
        print('\n' + '=' * (sum(book.max_len()) + 7))
        print(f'{"ID": >2}. {"Заголовок": <{max_t}>} '
              f"{'Описание': <{max_n}>}")
        for i, note in book.note.items():
            print(f'{i: >2}. {note.show(max_t, max_n)}')
        print('=' * (sum(book.max_len()) + 7) + '\n')
    else:
        print_msg(msg)


def note_input(input_fields: list[str]) -> list[str]:
    note = []
    for field in input_fields:
        note.append(input(field))
    return note


def input_data(msg: str) -> str:
    return input(msg)


def input_note(msg: str) -> int:
    while True:
        number = input(msg)
        if number.isdigit():
            return int(number)
        print(text.number_error)
