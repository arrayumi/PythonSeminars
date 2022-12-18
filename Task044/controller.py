import view
import model

def run():
  action = view.choose_action()
  if action:
      model.add_contact(view.input_contact_to_add())
  else:
      view.print_result(model.find_contact(view.input_contact_to_find()))