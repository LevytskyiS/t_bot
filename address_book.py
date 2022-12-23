from collections import UserDict


class AddressBook(UserDict):

    def __init__(self):
        super().__init__()
        self.load_address_book()

    def __str__(self) -> str: # допишу як тільки будуть функції додавання контактів

        headers = ("Name", "Phone", "Birthday", "Email", "Tags", "Notes")
        columns = "\n" + "|{:^10}|{:^25}" * (len(headers) // 2) + "|"
        header = columns.format(*headers)
        header += "\n|" + "-" * (37 * (len(headers) // 2) - 1) + "|"
        header = "\033[34m{}\033[0m".format(header)

        for name, record in self.data.items():
            for phone in record.phones:
                header += columns.format(
                    name.value,
                    phone.value,
                    "1988.09.12",
                    # record.email,
                    "123",
                    "tags",
                    "notes")
                    # str(record.notes[0]),
                    # record.notes[1])

                name = ""

        return header

    def add_record(self) -> str:
        '''Додає ім'я як ключ та об'єкт класу Рекорд як значення.'''
        pass

    def search_by_name(self) -> str:
        '''Шукає телефон по імені.'''
        pass

    def search_in_contact_book(self, data) -> str:
        '''Шукає співпадіння по цифрі в телефоні, по букві в імені, мейлу.'''
        
        output_book = AddressBook()

        for name, record in self.data.items():
            for phone in record.phones:
                if data in name.value or\
                    data in phone.value or\
                    data in record.email:

                    output_book.add_record(record)
        
        return output_book        

    def get_all_records(self) -> list:
        '''Повертає список всіх контактів із їхніми даними.'''
        pass

    def all_birthdays(self) -> list:
        '''Повертає список всіх днів народжень за проміжок днів заданих користувачем.'''
        pass

    def delete_record(self) -> str:
        '''Видаляє контакт повністю.'''
        pass

    def save_address_book(self) -> str:
        '''Зберігає адресну книгу'''
        pass

    def load_address_book(self) -> str:
        '''Завантажує адресну книгу.'''
        pass

    def iterator(self) -> list:
        '''Повертає кількість сторінок, вказаних користувачем.'''
        pass

address_book = AddressBook()    