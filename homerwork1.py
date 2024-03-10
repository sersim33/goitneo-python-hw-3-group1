from collections import UserDict,defaultdict
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
    
class Birthday(Field):
    def __init__(self, birthday):
        self.value = birthday
    # def __init__(self, value):
    #     try:
    #         datetime.strptime(value, '%Y-%m-%d')
    #     except ValueError:
    #         raise ValueError("Incorrect date format, should be YYYY-MM-DD")
    #     super().__init__(value)

class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday) if birthday else None

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
            
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)


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
        
    def get_birthdays_per_week(self):
        result_dict = defaultdict(list)
        today = datetime.today().date()
        for name, record in self.data.items():
            if record.birthday:
                birthday_date = record.birthday.value
                if today <= birthday_date <= today + timedelta(days=7):
                    weekday = birthday_date.strftime('%A')
                    result_dict[weekday].append(name)
        return result_dict
    

        # today = datetime.today().date()
        # birthday_greet = {}
    
    
        # for user in users:
        #     name = user["name"]
        #     birthday = user["birthday"].date()  # Конвертуємо до типу date*
        #     birthday_this_year = birthday.replace(year=today.year)
        
        # if birthday_this_year < today:
        #     birthday_this_year = birthday.replace(year=today.year + 1)
        # delta_days = (birthday_this_year - today).days

        # if delta_days < 7:
        #     weekday = birthday_this_year.strftime("%A")
        #     if weekday in ["Saturday", "Sunday"]:
        #         birthday_this_year += timedelta(days=(7 - delta_days))

        #     if weekday not in birthday_greet:
        #         birthday_greet[weekday] = [name]
        #     else:
        #         birthday_greet[weekday].append(name)
        
        # formatted_greetings = ""
        # for weekday, names in sorted(birthday_greet.items()):
        #     formatted_greetings += f"{weekday}: {', '.join(names)}\n"
    
        # return formatted_greetings
    



# record1 = Record("John")
# record1.add_phone(Phone("1234567890"))
# record1.add_birthday("2000-05-25")

# record2 = Record("Alice")
# record2.add_phone(Phone("9876543210"))
# record2.add_birthday("1995-10-15")

# # print(record1,record2)

# address_book = AddressBook()
# address_book.add_record(record1)
# address_book.add_record(record2)
# # print(address_book.data)

# upcoming_birthdays = address_book.get_birthdays_per_week()
# print(upcoming_birthdays)
