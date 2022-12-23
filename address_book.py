from collections import UserDict
import pickle
from record import Record


class AddressBook(UserDict):

    def __init__(self):
        super().__init__()
        self.load_address_book()

    def add_record(self, record: Record) -> str:
        '''Додає ім'я як ключ та об'єкт класу Рекорд як значення.'''
        self.data[record.name.value] = record
        return f'New contact was added successfuly.'

    def search_by_name(self) -> str:
        '''Шукає телефон по імені.'''
        pass

    def search_in_contact_book(self) -> str:
        '''Шукає співпадіння по цифрі в телефоні, по букві в імені, мейлу.'''
        pass

    def get_all_records(self) -> list:
        '''Повертає список всіх контактів із їхніми даними.'''
        pass

    def all_birthdays(self) -> list:
        '''Повертає список всіх днів народжень за проміжок днів заданих користувачем.'''
        pass

    def delete_record(self, name_to_del) -> str:
        '''Видаляє контакт повністю.'''
        for key in self.data.keys():
            if name_to_del.name.value == key:
                self.data.pop(key)
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