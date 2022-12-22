import view
import model


def run():
    mode = view.choose_mode()

    if mode == '1':
        result = model.find_contact(view.input_contact_to_find())
        if result[1] == True:
            view.print_result(result[0])
        else:
            view.contact_not_found()

    elif mode == '2':
        model.add_contact(view.input_contact_to_add())
        view.contact_added()

    elif mode == '3':
        del_contact = view.input_contact_to_delete()
        result = model.find_contact(del_contact)
        if result[1] == True:
            view.print_result(result[0])
            if view.delete_request() == 'да':
                model.delete_contact(del_contact)
                view.contact_deleted()
        else:
            view.contact_not_found()

    elif mode == '4':
        find_contact = view.input_contact_to_edit()
        result = model.find_contact(find_contact)
        if result[1] == True:
            view.print_result(result[0])
            if view.edit_request() == 'да':
                model.edit_contact(find_contact, view.input_contact_to_add())
                view.contact_edited()
        else:
            view.contact_not_found()
    
    else:
        view.mode_error()

