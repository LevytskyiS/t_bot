from fields_for_record import Name

class Record:
    
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
    
    def add_new_phone(self, phone) -> str:
        pass

    def change_phone(self, old_phone, new_phone) -> str:
        pass

    def delete_phone(self, phone) -> str:
        pass

    def add_mail(self, mail) -> str:
        pass

    def change_mail(self, new_mail) -> str:
        pass

    def delete_mail(self, mail) -> str:
        pass

    def add_note(self, note) -> str:
        pass

    def change_note(self) -> str:
        pass

    def delete_note(self) -> str:
        pass

    def add_birthday(self, birthday) -> str:
        pass

    def change_birthday(self, new_birthday) -> str:
        pass

    def days_to_birthdays(self) -> str:
        pass