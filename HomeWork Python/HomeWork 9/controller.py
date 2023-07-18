import view
import text
import model


def search_contact():
    word = view.input_data(text.search_word)
    result = model.PhoneBook(search(word))
    view.show_contacts(result, text.not_found(word))
    return result


def start():
    main_pb = model.PhoneBook()
    while True:
        user_select = view.show_menu(text.main_menu)
        match user_select:
            case 1:
                main_pb.open_file()
                view.print_msg(text.load_successful)
            case 2:
                main_pb.save_file()
                view.print_msg(text.save_successful)
            case 3:
                view.show_contacts(main_pb, text.empty_book)
            case 4:
                new = view.contact_input(text.new_contact)
                main_pb.add_contact(new)
                view.print_msg(text.added_successful(new[0]))
            case 5:
                search_contact()
            case 6:
                if search_contact():
                    uid = view.input_number(text.change_contact)
                    new = view.contact_input(text.rename_contact)
                    name = main_pb.change(uid, new)
                    view.print_msg(text.renamed_successful(name))
            case 7:
                if search_contact():
                    uid = view.input_number(text.input_del_contact)
                    name = main_pb.delete(uid)
                    view.print_msg(text.deleted_successful(name))
            case 8:
                break
