import json
import tkinter as tk
from tkinter import filedialog

running = True
changes = False
file_name = ['phonebook.json']

#------------------------------------------------------------------------------
# Never use real phone/fax numbers for tests. Use 555 numbers: 
# https://en.wikipedia.org/wiki/555_(telephone_number)
phone_book = [
{"name": "Nazar", "surname": "Nazarenko", "age": 50, "phone_number":"+18005550102", "email":"1@gmail.com"},
{"name": "Mariia", "surname": "Mariychuk", "age": 15, "phone_number":"+18505550112", "email":"2@gmail.com"},
{"name": "Mariia2", "surname": "Mariychuk2", "age": 20, "phone_number":"+18505550112", "email":"3@gmail.com"},
{"name": "Mariia3", "surname": "Mariychuk3", "age": 31, "phone_number":"+18505550112", "email":"4@gmail.com"},
{"name": "Mariia4", "surname": "Mariychuk4", "age": 20, "phone_number":"+18505550112", "email":"5@gmail.com"},
]


#------------------------------------------------------------------------------
def print_entry(number, entry):
    print("--[ %s ]--------------------------" % number)
    print("| Surname: %20s |" % entry["surname"])
    print("| Name:    %20s |" % entry["name"])
    print("| Age:     %20s |" % entry["age"])
    print("| Phone:   %20s |" % entry["phone_number"])
    print("| Email:   %20s |" % entry["email"])


#------------------------------------------------------------------------------
def print_phonebook():
    print()
    print()
    print("#########  Phone book  ##########")
    print()

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1


#------------------------------------------------------------------------------
def add_entry_phonebook():
    global changes
    surname = input("Enter surname: ")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    phone_number = input("Enter phone num.: ")

    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    entry["phone_number"] = phone_number
    phone_book.append(entry)
    changes = True


#------------------------------------------------------------------------------
def print_error(message):
    print("ERROR: %s" % message)


#------------------------------------------------------------------------------
def print_info(message):
    print("INFO: %s" % message)


#------------------------------------------------------------------------------
def find_entry_name_phonebook():
    name = input("Enter name: ")
    idx = 1
    found = False

    for entry in phone_book:
        if entry["name"] == name:
            print_entry(idx, entry)
            idx += 1
            found = True

    if not found:
        print_error("Not found!")


#------------------------------------------------------------------------------
def find_entry_age_phonebook():
    age = int(input("Enter age: "))
    idx = 1
    found = False

    for entry in phone_book:
        if entry["age"] == age:
            print_entry(idx, entry)
            idx += 1
            found = True

    if not found:
        print_error("Not found!")


#------------------------------------------------------------------------------
def find_entry_email_phonebook():
    email = input("Enter email: ")
    idx = 1
    found = False

    for entry in phone_book:
        if entry["email"] == email:
            print_entry(idx, entry)
            idx += 1
            found = True

    if not found:
        print_error("Not found!")


#------------------------------------------------------------------------------
def delete_entry_name_phonebook():
    global changes

    name = input("Enter name to delete: ")
    phone_book_copy = phone_book.copy()
    found = False

    for entry in phone_book_copy:
        if entry["name"] == name:
            phone_book.pop(phone_book.index(entry))
            found = True
            changes = True

    if not found:
        print_error("Not found!")


#------------------------------------------------------------------------------
def count_all_entries_in_phonebook():
    print("Total number of entries: ", len(phone_book))


#------------------------------------------------------------------------------
def print_phonebook_by_age():
    sorted_phone_book = sorted(phone_book, key=lambda entry: entry['age'])
    idx = 1
    for entry in sorted_phone_book:
        print_entry(idx, entry)
        idx += 1


#------------------------------------------------------------------------------
def increase_age():
    global changes

    years_to_add = int(input("Enter the number to increase the age: "))

    for entry in phone_book:
        entry['age'] += years_to_add

    changes = True

#------------------------------------------------------------------------------
def avr_age_of_all_persons():
    average_age = sum(entry['age'] for entry in phone_book) / len(phone_book)

    print(f'Average age of all persons: {average_age}')


#------------------------------------------------------------------------------
def change_email_by_name():
    global changes

    name = input("Enter name: ")
    phone_book_copy = phone_book.copy()
    found = False

    for entry in phone_book_copy:
        if entry["name"] == name:
            new_email = input("Enter email: ")
            entry["email"] = new_email
            changes = True
            found = True

    if not found:
        print_error("Not found!")


#------------------------------------------------------------------------------
def save_to_file():
    global file_name

    user_response = input(
        "Do you want to save to a new file or an existing one? (n/ex): "
    )

    if user_response == 'n':
        window = tk.Tk()
        window.withdraw()

        file_path = filedialog.asksaveasfilename(
            defaultextension=".json", filetypes=[("JSON files", "*.json")]
        )

        if file_path:
            with open(file_path, "w") as file:
                json.dump(phone_book, file)
                print("Phone book saved to new file")
            file_name.append(file_path)
        else:
            print("Phone book not saved")

    elif user_response == 'ex':

        window = tk.Tk()
        window.withdraw()

        file_path = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json")]
        )

        if file_path:
            user_response = input("File will be overwritten. Continue? (y/n): ")

            if user_response == 'y':
                with open(file_path, "w") as file:
                    json.dump(phone_book, file)
                    print(f"Phone book saved to existing file: {file_path}")
            else:
                print("Phone book not saved")
        else:
            print("Phone book not saved")
    else:
        print("Invalid option")


#------------------------------------------------------------------------------
def load_from_file():
    global phone_book

    if changes:
        user_response = input("Would you like to save changes? (y/n): ")

        if user_response == 'y':
            save_to_file()

    window = tk.Tk()
    window.withdraw()

    file_path = filedialog.askopenfilename(
        filetypes=[("JSON files", "*.json")]
    )

    if file_path:
        with open(file_path, "r") as file:
            phone_book = json.load(file)
            print("Data loaded from file:", phone_book)
            return phone_book

    else:
        print("File has not been selected")


#------------------------------------------------------------------------------
def exit_phonebook():
    global running

    if changes:
        save_to_file()

    running = False


#------------------------------------------------------------------------------
def print_prompt():
      print()
      print()
      print()
      print("~ Welcome to phonebook ~")
      print("Select one of actions below:")
      print("     1 - Print phonebook entries")
      print("     2 - Print phonebook entries (by age)")
      print("     3 - Add new entry")
      print("     4 - Find entry by name")
      print("     5 - Find entry by age")
      print("     5e - Find entry by email")
      print("     6 - Delete entry by name")
      print("     7 - The number of entries in the phonebook")
      print("     8 - Avr. age of all persons")
      print("     9 - Increase age by num. of years")
      print("     9e - Change_email_by_name")
      print("-----------------------------")
      print("     s - Save to file")
      print("     l - Load from file")
      print("     0 - Exit")
      print()


#------------------------------------------------------------------------------
def main():

    while running:
        try:
            menu = {
                  '1':  print_phonebook,
                  '2':  print_phonebook_by_age,
                  '3':  add_entry_phonebook,
                  '4':  find_entry_name_phonebook,
                  '5':  find_entry_age_phonebook,
                  '5e': find_entry_email_phonebook,
                  '6':  delete_entry_name_phonebook,
                  '7':  count_all_entries_in_phonebook,
                  '8':  avr_age_of_all_persons,
                  '9':  increase_age,
                  '9e': change_email_by_name,

                  '0':  exit_phonebook,
                  's':  save_to_file,
                  'l':  load_from_file,
            }

            print_prompt()
            user_input = input("phonebook> ")
            menu[user_input]()

        except Exception as ex:
            print_error("Something went wrong. Try again...")


#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
