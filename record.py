from fields_for_record import Name, Birthday, Phone
from datetime import datetime


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
        self.phones.append(Phone(phone))
        return f'The phone was added.'

    def change_phone(self, old_phone, new_phone) -> str:
        '''Міняє існуючий телефон контакту.'''
        
        phones_values = [phone.value for phone in self.phones]   # Список телефонів для пошуку
        old_phone = Phone(old_phone)   
        new_phone = Phone(new_phone)
        index = phones_values.index(old_phone.value)   #Пошук індексу старого номеру телефону
        self.phones[index] = new_phone   #Змінюємо старий номер телефону на новий за індексом

        return f"Phone number '{old_phone}' changed to '{new_phone}'"

    def delete_phone(self, phone) -> str:
        '''Видаляє існуючий телефон.'''
        
        phone = Phone(phone)
        phones_values = [phone_.value for phone_ in self.phones]
        index = phones_values.index(phone.value)
        self.phones.pop(index)

        return f"The phone number '{phone.value}' has been deleted"

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
        self.birthday = Birthday(birthday)
        return f'Birthday was successfully added'

    def change_birthday(self, new_birthday) -> str:
        '''Міняє день народження.'''
        if self.birthday:
            self.birthday.value = new_birthday
            return f'Birthday has been successfully changed'
        else:
            return f'The birthday hasn`t been added yet for this contact. Add first'


    def days_to_birthdays(self) -> str:
        '''Повертає кількість днів, яка залишилась до ДН конкретної людини.
        Реализовать функцию days_to_birthdays в файле Рекорд. Если имя есть в списке контактов, то возвращает ДР или
        строку наподобие “The birthday hasn`t been added yet for this contact.“ Если такого имени нет в книге контактов,
        то возвращается строка с тем, что такого контакта нет.'''
        if self.birthday:
            current_year = datetime.now().year
            current_day = datetime.now()
            this_year_birthday = datetime(year=current_year, month=self.birthday.value.month, day=self.birthday.value.day)
            if (this_year_birthday - current_day).days >= 0:
                next_birth = this_year_birthday - current_day
                return f'Days to birthday is {next_birth.days}'
            else:
                next_birth = datetime(year=current_year + 1, month=self.birthday.value.month, day=self.birthday.value.day)
                return f'Days to birthday is {(next_birth - current_day).days}'
        else:
            return f'The birthday hasn`t been added yet for this contact'

