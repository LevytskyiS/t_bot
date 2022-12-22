import re


class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    def __str__(self):
        return f'{self.__value}'


class Name(Field):
    pass


class Phone(Field):
    pass


class Email(Field):

    @Field.value.setter
    def value(self, email: str):

        new_email = re.search(r".+@.+", email)

        if not new_email:
            return "Email is not valid."

        self._value = new_email.group()
        

class Note(Field):
    pass


class Tag(Field):
    pass


class Birthday(Field):
    pass
