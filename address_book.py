from collections import UserDict


class AddressBook(UserDict):

    def __init__(self):
        super().__init__()

    def add_record(self) -> str:
        pass

    def search_by_name(self) -> str:
        pass

    def search_in_contact_book(self) -> str:
        pass

    def show_all_contact(self) -> list:
        pass

    def all_birthdays(self) -> list:
        pass

    def delete_contact(self) -> str:
        pass

    def save_address_book(self) -> str:
        pass

    def load_address_book(self) -> str:
        pass

    def iterator(self) -> list:
        pass