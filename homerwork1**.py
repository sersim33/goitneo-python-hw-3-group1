from collections import UserDict
from datetime import datetime, timedelta


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass 

class Phone(Field):
    def __init__(self, phone):
        if len(phone) == 10 and phone.isdigit():
            super().__init__(phone)
        else:
            raise ValueError
    

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        for user_phone in self.phones:
            if user_phone == phone:
                self.phones.remove(user_phone)

    def edit_phone(self, old_phone, new_phone):
        self.phones = [new_phone if phone == old_phone else phone for phone in self.phones]
    

    def find_phone(self, phone):
        for user_phone in self.phones:
            if user_phone == phone:
                return user_phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"

    
class AddressBook(UserDict):
    def __init__(self):
        self.data = dict()

    def add_record(self, record):
        name = record.name.value
        self.data[name] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return "No contact found."
        
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return f"Contact '{name}' deleted."
        else:
            return f"Contact '{name}' not found."