from fields_for_record import Name, Birthday, Phone, Email, Note, Tag
from datetime import datetime
from copy import copy


class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.tag = None
        self.note = None
        self.notes =[]

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
        '''Додає нотатку. Один раз'''
        if not self.note:
            note = ""
            for item in list_note:
                note += f"{item} "
            self.note = Note(note)
        else:
            return f'Note is existed. Cannot be added'

        return f"The note < {note[:-1]} > was added to the contact < {self.name.value}.title() >."

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
        deleted_note = self.note.value
        self.note = Note('')
        return f'The note < {deleted_note} > of contact < {self.name.value} > was deleted.'

    def add_tag(self, tag) -> str:
        '''Створює теги. Один Раз при виклику '''
        if not self.tag:
            self.tag = Tag(tag)
            return f"The tag < {tag} > was added to the contact < {self.name.value} >."
        else:
            return f'Tag is existed. Cannot be added'

    def change_tag(self, new_tag_list):
        '''Додає теги до існуючиго списку тегів.'''
        old_tag = self.tag
        if self.tag:
            self.tag=Tag(old_tag.value + new_tag_list)
            print(f'The new tag {new_tag_list} has been added to old one {old_tag.value}')
        else:
            print(f'The tag has been added yet for this contact. Add first')

    def delete_tags(self) -> str:
        '''Видаляє всі тег.'''
        deleted_tag = self.tag
        self.tag = Tag('')
        return f"The tag < {deleted_tag.value} > of contact < {self.name.value} > was deleted"

    def del_tag(self):
        '''Видаляє існуючий тег зі списку.'''
        if self.tag:
            old_tags =copy(self.tag.value)
            tags = [tag for tag in self.tag.value]
            showing = dict(enumerate(tags, 1))
            while True:
                try:
                    print(f"What tag do you want to remove? {showing}")
                    choosing = input("Choose № of this tags (skip it if you  want press enter)>>> ")
                    if not choosing:
                        print( f"You didn't remove any tags of < {self.tag.value} >")
                    choosing = int(choosing)
                    self.tag.value.pop(choosing - 1)
                    print( f"Tag < {showing[choosing]} > from < {old_tags} > was removed")
                    break
                except ValueError:
                    print(f"{choosing} is not a number!")
                except KeyError:
                    print(f"{choosing} is out of range!")
                except IndexError:
                    print(f"{choosing} is out of range!")
        else:
            return f' Tag {self.tag} is empty '


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

