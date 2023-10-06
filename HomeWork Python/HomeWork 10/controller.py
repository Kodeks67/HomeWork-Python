import view
import text
import model


def search_note():
    word = view.input_data(text.search_word)
    result = model.NotesRedactor(search(word))
    view.show_notes(result, text.not_found(word))
    return result


def start():
    main_nt = model.NotesRedactor
    while True:
        user_select = view.show_menu(text.main_menu)
        match user_select:
            case 1:
                main_nt.open_file()
                view.print_msg(text.load_successful)
            case 2:
                main_nt.save_file()
                view.print_msg(text.save_successful)
            case 3:
                view.show_notes(main_nt, text.empty_book)
            case 4:
                new = view.note_input(text.new_note)
                main_nt.add_note(new)
                view.print_msg(text.added_successful(new[0]))
            case 5:
                search_note()
            case 6:
                if search_note():
                    uid = view.input_note(text.change_note)
                    new = view.note_input(text.rename_note)
                    name = main_nt.change(uid, new)
                    view.print_msg(text.renamed_successful(name))
            case 7:
                if search_note():
                    uid = view.input_note(text.input_del_contact)
                    name = main_nt.delete(uid)
                    view.print_msg(text.deleted_successful(name))
            case 8:
                break