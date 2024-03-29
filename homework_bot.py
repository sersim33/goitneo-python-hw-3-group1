
from homerwork1 import AddressBook
from collections import UserDict,defaultdict
from datetime import datetime, timedelta
from homerwork1 import Record



# class AddressBook(UserDict):
#     pass

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Index out of range."

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book):
    if len(args) < 2:
        return "Please provide both - username and phone number."
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    # book[name] = phone
    book.add_record(record)
    return "Contact added."

@input_error
def change_contact(args, book):
    if len(args) < 2:
        return "Please provide both - username and phone number."
    username, phone = args
    if username in book:
        record = book.get(username)
        current_phone = record.phones[0].value
        record.edit_phone(current_phone, phone)
        return f"Phone updated for {username}."
    else:
        return f"Contact {username} does not exist."

    
@input_error    
def show_phone(args, book):
    username = args[0]
    if username in book:
        phone = book[username]
        if len(phone) == 10 and phone.isdigit():
            return phone
        else:
            return "Invalid phone number format."
    else:
         return "Name was not found."
    
@input_error    
def all_contacts(book):
    if not book:
        return "No contacts found."
    
    result = ""
    for name, phone in book.items():
        result += f"{name}: {phone}\n"
    
    return result  

@input_error
def add_birthday(args, book):
    if len(args) < 2:
        return "Please provide both - username and birthday (in DD.MM.YYYY format)."
    username, birthday_str = args
    try:
        birthday = datetime.strptime(birthday_str, "%d.%m.%Y").date()
    except ValueError:
        return "Invalid date format. Please use DD.MM.YYYY."
    
    if username in book:
        contact = book[username]
        contact.add_birthday(birthday)
        book.add_record(contact)  # Update the record in the address book
        return f"Birthday added for {username}."
    else:
        return f"Contact {username} does not exist." 
    
@input_error
def show_birthday(args, book):
    username = args[0]
    if username in book:
        contact = book[username]
        if hasattr(contact, 'birthday'):
            return f"{username}'s birthday is {contact.birthday}"
        else:
            return f"{username} does not have a recorded birthday."
    else:
        return f"Contact '{username}' not found." 
    
@input_error    
def get_birthdays_per_week(args, book):
    return book.get_birthdays_per_week()
    

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book)) 
        elif command == "show_phone":
            print(show_phone(args,book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(get_birthdays_per_week(args,book))
        elif command == "all":
            print(all_contacts(book))         
        else:
            print("Invalid command.")
    return book


if __name__ == "__main__":
    main()