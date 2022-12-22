from fields_for_record import Name
class Record:
    
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.tag = []
        self.notes = ""

    def add_phone(self, phone) -> str:
        '''Додає телефону до списку телефонів контакту.'''
        pass

    def change_phone(self, old_phone, new_phone) -> str:
        '''Міняє існуючий телефон контакту.'''
        pass

    def delete_phone(self, phone) -> str:
        '''Видаляє існуючий телефон.'''
        pass

    def add_mail(self, mail) -> str:
        '''Додає мейл до контакту.'''
        pass

    def change_mail(self, new_mail) -> str:
        '''Міняє існуючий мейл.'''
        pass

    def delete_mail(self, mail) -> str:
        '''Видаляє існуючий мейл.'''
        pass

    def add_note(self, note) -> str:
        '''Додає нотатку.'''
        pass

    def change_note(self) -> str:
        '''Міняє нотатку.'''
        pass

    def delete_note(self) -> str:
        '''Видаляє нотатку.'''
        pass

    def add_birthday(self, birthday) -> str:
        '''Додає день народження.'''
        pass

    def change_birthday(self, new_birthday) -> str:
        '''Міняє день народження.'''
        pass

    def days_to_birthdays(self) -> str:
        '''Повертає кількість днів, яка залишилась до ДН конкретної людини.'''
        pass