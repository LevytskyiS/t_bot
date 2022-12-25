from fields_for_record import Name, Birthday, Phone, Email, Note, Tag
from datetime import datetime
from copy import copy


class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.emails = []
        self.tag = None
        self.note = None
        self.notes =[]

    def add_phone(self, phone) -> str:
        '''Adds a phone to the contact's list of phones.'''
        added_phone = Phone(phone)
        self.phones.append(added_phone)
        return f"The phone '{added_phone.value}' was added to the '{self.name.value.title()}'."

    def change_phone(self, new_phone) -> str:
        '''Changes an existing phone.'''
        if self.phones:
            new_phone = Phone(new_phone)
            phones = [phone.value for phone in self.phones]
            showing = dict(enumerate(phones, 1))
            
            while True:
                
                try:
                    print(f"What phone you want to change? {showing}\n")
                    choosing = input("Choose № of this phone (skip it if you don't want)>>> ")
                    
                    if not choosing:
                        return f"You didn't change any phone in your list: {self.name.value.title()}."
                    choosing = int(choosing)
                    
                    if choosing > 0:
                        self.phones[choosing-1] = new_phone
                        return f"Phone '{showing[choosing]}' of '{self.name.value.title()}' changed to '{new_phone.value}'."
                    else:
                        raise KeyError

                except ValueError:
                    print(f"{choosing} is not a number!")
                except KeyError:
                    print(f"{choosing} is out of range!")
                except IndexError:
                    print(f"{choosing} is out of range!")

        else:
            raise ValueError(f"Phone list of '{self.name.value.title()}' is empty")
   
    def delete_phone(self) -> str:
        '''Deletes an existing phone.'''
        if self.phones:
            phones = [phone.value for phone in self.phones]
            showing = dict(enumerate(phones, 1))
            
            while True:
                
                try:
                    print(f"What phone you want to remove? {showing}")
                    choosing = input("Choose № of this phone (skip it if you don't want)>>> ")
                    
                    if not choosing:
                        return f"You didn't remove any phone of '{self.name.value.title()}'."
                    choosing = int(choosing)
                    if choosing > 0:
                        self.phones.pop(choosing-1)
                        return f"Phone '{showing[choosing]}' of '{self.name.value.title()}' removed."
                    else:
                        raise KeyError
       
                except ValueError:
                    print(f"{choosing} is not a number!")
                except KeyError:
                    print(f"{choosing} is out of range!")
                except IndexError:
                    print(f"{choosing} is out of range!")

        else:
            raise ValueError(f"Phones list of '{self.name.value.title()}' is empty.")

    def add_mail(self, mail) -> str:
        '''Add an email to the contact.'''
        added_email = Email(mail)
        self.emails.append(added_email)
        return f"The email '{added_email.value}' was added to '{self.name.value.title()}'."

    def change_mail(self, new_mail) -> str:
        '''Changes the phone.'''
        if self.emails:
            new_mail = Email(new_mail)
            emails = [email.value for email in self.emails]
            showing = dict(enumerate(emails, 1))
            
            while True:
                
                try:
                    print(f"What email you want to change? {showing}")
                    choosing = input("Choose № of this email (skip it if you don't want)>>> ")
                    
                    if not choosing:
                        return f"You didn't change any email of '{self.name.value.title()}'."
                    choosing = int(choosing)
                    
                    if choosing > 0:
                        self.emails[choosing-1] = new_mail
                        return f"Email < {showing[choosing]} > of < {self.name.value.title()} > changed to the < {new_mail.value} >"
                    else:
                        raise KeyError

                except ValueError:
                    print(f"{choosing} is not a number!")
                except KeyError:
                    print(f"{choosing} is out of range!")
                except IndexError:
                    print(f"{choosing} is out of range!")

        else:
            raise ValueError(f"Emails list of '{self.name.value.title()}' is empty.")

    def delete_mail(self) -> str:
        '''Removes an email.'''
        if self.emails:
            emails = [email.value for email in self.emails]
            showing = dict(enumerate(emails, 1))
            
            while True:
                
                try:
                    print(f"What email you want to remove? {showing}")
                    choosing = input("Choose № of this email (skip it if you don't want)>>> ")
                   
                    if not choosing:
                        return f"You didn't remove any email of '{self.name.value.title()}'."
                    choosing = int(choosing)
                    
                    if choosing > 0:
                        self.emails.pop(choosing-1)
                        return f"Email '{showing[choosing]}' of '{self.name.value.title()}' removed."
                    else:
                        raise KeyError

                except ValueError:
                    print(f"{choosing} is not a number!")
                except KeyError:
                    print(f"{choosing} is out of range!")
                except IndexError:
                    print(f"{choosing} is out of range!")

        else:
            raise ValueError(f"Emails list of '{self.name.value.title()}' is empty.")

    def add_note(self, list_note) -> str:
        '''Add only one note at all.'''
        if not self.note:
            note = ""
            for item in list_note:
                note += f"{item} "
            self.note = Note(note)
        else:
            return f"Note exists. Choose the 'edit note' command to correct the note."

        return f"The note '{note[:-1]}' was added to the contact '{self.name.value.title()}'."

    def change_note(self, list_new_note) -> str:
        '''Corrects the note.'''
        new_note = ""
        for item in list_new_note:
            new_note += f"{item} "
        old_note = self.note.value
        note = old_note + new_note   
        self.note = Note(note)

        return f"The note '{new_note[:-1]}' was added to the contact '{self.name.value.title()}'."

    def delete_note(self) -> str:
        '''Deletes the note.'''
        deleted_note = self.note.value
        self.note = None
        return f"The note '{deleted_note}' of contact '{self.name.value}' was deleted."

    def add_tag(self, list_tag) -> str:
        '''Creates and adds tags to the contact's list of tags.'''
        if not list_tag:
            return f"There are no tags in the input, please type again"
        elif not self.tag:
            tag_list2 = []
            for tag in list_tag:
                tag_list2.append(tag)
            self.tag = Tag(tag_list2)
            return f"The tag '{tag_list2}' was added to the contact '{self.name.value}'."
        else:
            return f"Tag is existed. Cannot be added."

    def change_tag(self, new_tag_list):
        '''Adds new tahs to the list.'''
        old_tag = self.tag
        if self.tag:
            self.tag = Tag(old_tag.value + new_tag_list)
            print(f"The new tag {new_tag_list} has been added to old one {old_tag.value}.")
        else:
            print(f"The tag has been added yet for this contact. Add first.")

    def delete_tags(self) -> str:
        '''Deletes all tags.'''
        deleted_tag = self.tag
        self.tag = None
        return f"The tag < {deleted_tag.value} > of contact < {self.name.value} > was deleted"

    def del_tag(self):
        '''Deletes only that tag which is chosen by a user.'''
        if self.tag:
            old_tags =copy(self.tag.value)
            tags = [tag for tag in self.tag.value]
            showing = dict(enumerate(tags, 1))
            
            while True:
                try:
                    print(f"What tag do you want to remove? {showing}")
                    choosing = input("Choose № of this tags (skip it if you  want press enter)>>> ")
                    
                    if not choosing:
                        print( f"You didn't remove any tags of '{self.tag.value}'.")
                    choosing = int(choosing)
                    self.tag.value.pop(choosing - 1)
                    return f"Tag '{showing[choosing]}' from '{old_tags}' was removed."
                
                except ValueError:
                    print(f"{choosing} is not a number!")
                except KeyError:
                    print(f"{choosing} is out of range!")
                except IndexError:
                    print(f"{choosing} is out of range!")
        else:
            return f"Tag {self.tag} is empty."


    def add_birthday(self, birthday) -> str:
        '''Add a birthday.'''
        self.birthday = Birthday(birthday)
        return f"Birthday was successfully added."

    def change_birthday(self, new_birthday) -> str:
        '''Changes a birthday.'''
        if self.birthday:
            self.birthday = Birthday(new_birthday)
            return f"Birthday has been changed successfully."
        else:
            return f"The birthday hasn't been added yet for this contact. Add first."

    def days_to_birthdays(self):
        '''Returns a quantity of days until contact's birthday.'''
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
            return f"The birthday hasn`t been added yet for this contact."
    
    def delete_birthday(self):
        '''Deletes a birthday.'''
        self.birthday = None
        return f"The birhdays was deleted successfully."