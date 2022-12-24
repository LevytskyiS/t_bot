from fields_for_record import Name, Birthday, Phone, Email, Note, Tag
from datetime import datetime


class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.tag = ""
        self.note = ""
        self.notes =[]

    def add_phone(self, phone) -> str:
        '''Додає телефону до списку телефонів контакту.'''
        self.phones.append(Phone(phone))
        return f'The phone was added.'

    def change_phone(self, new_phone) -> str:
        '''Міняє існуючий телефон контакту.'''
        
        if self.phones:
            new_phone = Phone(new_phone)
            phones = [phone.value for phone in self.phones]
            showing = dict(enumerate(phones, 1))
            while True:
                try:
                    print(f"What phone you want to change? {showing}")
                    choosing = input("Choose № of this phone (skip it if you don't want)>>> ")
                    if not choosing:
                        return f"You didn't change any phone of < {self.name.value.title()} >"
                    choosing = int(choosing)
                    if choosing > 0:
                        self.phones[choosing-1] = new_phone
                        return f"Phone < {showing[choosing]} > of < {self.name.value.title()} > changed to the < {new_phone.value} >"
                    else:
                        raise KeyError
                    break
                except ValueError:
                    print(f"{choosing} is not a number!")
                except KeyError:
                    print(f"{choosing} is out of range!")
                except IndexError:
                    print(f"{choosing} is out of range!")

        else:
            raise ValueError(f"Phones list of < {self.name.value.title()} > is empty")

   
    def delete_phone(self) -> str:
        '''Видаляє існуючий телефон.'''
        
        if self.phones:
            phones = [phone.value for phone in self.phones]
            showing = dict(enumerate(phones, 1))
            while True:
                try:
                    print(f"What phone you want to remove? {showing}")
                    choosing = input("Choose № of this phone (skip it if you don't want)>>> ")
                    if not choosing:
                        return f"You didn't remove any phone of < {self.name.value.title()} >"
                    choosing = int(choosing)
                    if choosing > 0:
                        self.phones.pop(choosing-1)
                        return f"Phone < {showing[choosing]} > of < {self.name.value.title()} > removed"
                    else:
                        raise KeyError
                    break
                except ValueError:
                    print(f"{choosing} is not a number!")
                except KeyError:
                    print(f"{choosing} is out of range!")
                except IndexError:
                    print(f"{choosing} is out of range!")

        else:
            raise ValueError(f"Phones list of < {self.name.value.title()} > is empty")

    def add_mail(self, mail) -> str:
        '''Додає мейл до контакту.'''
        self.email = Email(mail)
        return f'The email < {mail} > was added to the contact < {self.name.value.title()} >.'

    def change_mail(self, new_mail) -> str:
        '''Міняє існуючий мейл.'''
        old_mail = self.email.value
        self.email = Email(new_mail)
        return f'The email < {old_mail} > of contact < {self.name.value.title()} > was changed into < {new_mail} >.'

    def delete_mail(self) -> str:
        '''Видаляє існуючий мейл.'''
        deleted_mail = self.email.value
        self.email = None
        return f'The email < {deleted_mail} > of contact < {self.name.value.title()} > was deleted.'

    def add_note(self, list_note) -> str:
        '''Додає нотатку.'''
        note = ""
        for item in list_note:
            note += f"{item} "  
        self.note = Note(note)

        return f"The note < {note[:-1]} > was added to the contact < {self.name.value.title()} >."

    def change_note(self, list_new_note) -> str:
        '''Міняє нотатку.'''
        new_note = ""
        for item in list_new_note:
            new_note += f"{item} "
        old_note = self.note.value
        note = old_note + new_note   
        self.note = Note(note)

        return f"The note < {new_note[:-1]} > was added to the contact < {self.name.value.title()} >."

    def delete_note(self) -> str:
        '''Видаляє нотатку.'''
        pass

    def add_tag(self, tag) -> str:
        '''Додає тег.'''  
        self.tag = Tag(tag)

        return f"The tag < {tag} > was added to the contact < {self.name.value.title()} >."

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


    def days_to_birthdays(self):
        '''Повертає кількість днів, яка залишилась до ДН конкретної людини.'''
        if self.birthday:
            current_year = datetime.now().year
            current_day = datetime.now()
            this_year_birthday = datetime(year=current_year, month=self.birthday.value.month, day=self.birthday.value.day)
            if (this_year_birthday - current_day).days >= 0:
                next_birth = this_year_birthday - current_day
                return next_birth.days
            else:
                next_birth = datetime(year=current_year + 1, month=self.birthday.value.month, day=self.birthday.value.day)
                return (next_birth - current_day).days
        else:
            return f'The birthday hasn`t been added yet for this contact'

