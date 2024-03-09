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
def add_contact(args, contacts):
    if len(args) < 2:
        return "Please provide both - username and phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        return "Please provide both - username and phone number."
    username, phone = args
    if username in contacts:
        contacts[username] = phone
        return f"Phone updated for {username}."
    else:
        return f"Contact {username} does not exist."
    
@input_error    
def show_phone(args, contacts):
    #"phone username" За цією командою бот виводить у консоль номер телефону для зазначеного контакту username.
    username = args[0]
    if username in contacts:
        phone = contacts[username]
        return phone
    else:
         return "name was not found" 

@input_error    
def all_contacts(contacts):
    if not contacts:
        return "No contacts found."
    
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    
    return result    

def main():
    contacts = {}
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
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts)) 
        elif command == "show_phone":
            print(show_phone(args,contacts))
        elif command == "all":
            print(all_contacts(contacts))         
        else:
            print("Invalid command.")
    return contacts


if __name__ == "__main__":
    main()