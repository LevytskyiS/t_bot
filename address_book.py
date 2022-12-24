from collections import UserDict
import pickle
from record import Record


class AddressBook(UserDict):

    def __str__(self) -> str:

        header = "\n|" + "-" * 117 + "|"
        headers = ("Name", "Phone", "Birthday", "Email", "Tags", "Notes")
        columns = "\n|{:^10}|{:^15}|{:^12}|{:^25}|{:^15}|{:^35}|"
        header += columns.format(*headers)
        header += "\n|" + "-" * 117+ "|"
        header = "\033[34m{}\033[0m".format(header)

        for name, record in self.data.items():

            phone = record.phones[0].value if record.phones else ""
            birthday = record.birthday.value.strftime("%m.%d.%Y") if record.birthday else ""
            email = record.email.value if record.email else ""
            tag = record.tag.value if record.tag else ""
            note = record.note.value if record.note else " "
            note_table = [note[i:i+33] for i in range(0, len(note), 33)]

            header += columns.format(
                name.title(),
                phone,
                birthday,
                email,
                tag,
                note_table[0])

            for i, phone in enumerate(record.phones):

                if i > 0:
                    header += columns.format("", phone.value, "", "", "", note_table[i])

            header += "\n|" + "-" * 117 + "|"

        return header
    
    def add_record(self, record: Record) -> str:
        '''Додає ім'я як ключ та об'єкт класу Рекорд як значення.'''
        self.data[record.name.value] = record                 #.title()
        return f'New contact was added successfuly.'


    def search_in_contact_book(self, data) -> str:
        '''Шукає співпадіння по цифрі в телефоні, по букві в імені, мейлу.'''
        
        output_book = AddressBook()
        data = data[0]        

        for name, record in self.data.items():

            birthday = record.birthday.value.strftime("%m.%d.%Y") if record.birthday else ""
            email = record.email.value if record.email else ""
            tag = record.tag.value if record.tag else ""
            note = record.note.value if record.note else ""

            if data in name or\
                data in birthday or\
                data in email or\
                data in tag or\
                data in note:

                output_book.add_record(record)

            for phone in record.phones:
                if data in phone.value:
                    output_book.add_record(record)                
        
        return output_book        

    def get_all_records(self) -> list:
        '''Повертає список всіх контактів із їхніми даними.'''
        pass

    def all_birthdays(self, range_days) -> list:
        '''Повертає список всіх днів народжень за проміжок днів заданих користувачем.'''
        list_accounts = []
        for record_elem in self.data.values():
            if record_elem.birthday:
                days_to_next_birthday = record_elem.days_to_birthdays()
                if days_to_next_birthday <= range_days:
                    list_accounts.append(record_elem.name.value)
            else:
                continue
        return list_accounts


    def delete_record(self, contact_name: str) -> str:
        '''Видаляє контакт повністю.'''
        self.data.pop(contact_name)
        return f'The contact was deleted successfully.'


    def save_address_book(self) -> str:
        '''Зберігає адресну книгу'''
        with open("address_book.bin", "wb") as file:
            pickle.dump(self.data, file)
    

    def load_address_book(self) -> str:
        '''Завантажує адресну книгу.'''
        try:
            with open("address_book.bin", "rb") as file:     
                self.data = pickle.load(file)
        except FileNotFoundError:
            return "The file does not exist."   
        

    def iterator(self) -> list:
        '''Повертає кількість сторінок, вказаних користувачем.'''
        pass


address_book = AddressBook()
address_book.load_address_book()
