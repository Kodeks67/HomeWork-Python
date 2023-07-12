# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать контакты
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

#
# Панфилов Кирилл;89094512021;Семнарист GB
# Роберт Адамян;888-999-777;DJ на семинарах

def open_file():
    try:
        with open(r'file_phonebook.txt', 'r', encoding='UTF-8') as file:
            phonebook = file.readlines()
    except FileNotFoundError:
        phonebook = []
    return phonebook


def save_file_phonebook(phonebook):
    with open(r'file_phonebook.txt', 'w', encoding='UTF-8') as file:
        file.writelines(phonebook)


def show_contacts(phonebook):
    if not phonebook:
        print('Справочник пуст.')
    else:
        print('Контакты: ')
        for contacts in phonebook:
            print(contacts.strip())


def add_contact(phonebook):
    full_name = input('Введите ФИО: ')
    phone_number = input('Введите номер телефона: ')
    description = input('Напишиет описание контакту: ')
    contact = f"ФИО: {full_name} Телефон: {phone_number} Описание: {description}\n"
    phonebook.append(contact)
    print('Контакт добавлен.')


def show_contact(phonebook):
    query = input('Введите фамилию или имя контакта: ')
    found_contacts = []
    for contact in phonebook:
        if query.lower() in contact.lower():
            found_contacts.append(contact)
    if found_contacts:
        print('Найденные контакты: ')
        for contact in found_contacts:
            print(contact.strip())
    else:
        print('Контакты не найдены.')


def update_contact(phonebook):
    query = input('Введите имя или фамилию контакта для изменения: ')
    found_contacts = []
    for contact in phonebook:
        if query.lower() in contact.lower():
            found_contacts.append(contact)
    if found_contacts:
        print('Найденные контакты: ')
        for index, contact in enumerate(found_contacts):
            print(f'{index + 1}. {contact.strip()}')
        choice = input('Выберите номер контакта для изменения: ')
        if choice.isdigit() and 1 <= int(choice) <= len(found_contacts):
            contact = found_contacts[int(choice) - 1]
            print(f'Выбран контакт:\n{contact.strip()}')
            new_phone_number = input('Введите новый номер телефона (оставьте пустым, если не нужно изменять): ')
            new_description = input("Введите новое описание (оставьте пустым, если не нужно изменять): ")
            if new_phone_number:
                contact = contact.replace(contact.split(':')[2], f' {new_phone_number} ')
            if new_description:
                contact = contact.replace(contact.split(':')[3], f' {new_phone_number}')
            phonebook.remove(found_contacts[int(choice) - 1])
            phonebook.append(contact)
            print('Контакты успешно изменен.')
        else:
            print('Неверный выбор контакта.')
    else:
        print("Контакты не найдены.")


def delete_contact(phonebook):
    query = input('Введите имя или фамилию контакта для изменения: ')
    found_contacts = []
    for contact in phonebook:
        if query.lower() in contact.lower():
            found_contacts.append(contact)
    if found_contacts:
        print('Найденные контакты: ')
        for index, contact in enumerate(found_contacts):
            print(f'{index + 1}. {contact.strip()}')
        choice = input('Выберите номер контакта для удаления: ')
        if choice.isdigit() and 1 <= int(choice) <= len(found_contacts):
            contact = found_contacts[int(choice) - 1]
            print(f'Выбран контакт для удаления: \n{contact.strip()}')
            phonebook.remove(found_contacts[int(choice) - 1])
            print('Контакт успешно удален.')
        else:
            print('Неверный выбор контакта.')
    else:
        print('Контакт не найден')


def main():
    phonebook = open_file()

    while True:
        print('1. Открыть файл')
        print('2. Сохранить файл')
        print('3. Показать контакты')
        print('4. Добавить контакт')
        print('5. Найти контакт')
        print('6. Изменить контакт')
        print('7. Удалить контакт')
        print('8. Выход')

        choice = input('Выберите номер действия: ')

        if choice == '1':
            phonebook = open_file()
            print("Файл успешно открыт.")
        elif choice == '2':
            save_file_phonebook(phonebook)
            print("Файл успешно сохранен.")
        elif choice == '3':
            show_contacts(phonebook)
        elif choice == '4':
            add_contact(phonebook)
        elif choice == '5':
            show_contact(phonebook)
        elif choice == '6':
            update_contact(phonebook)
        elif choice == '7':
            delete_contact(phonebook)
        elif choice == '8':
            break
        else:
            print("Неверный выбор действия. Пожалуйста, выберите номер от 1 до 8.")


if __name__ == '__main__':
    main()
