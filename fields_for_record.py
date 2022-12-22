import re
from datetime import datetime


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    def __str__(self):
        return f'{self._value}'


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
    ''' Класс Birthday створює дату народження.
     Вираховує кількість днів до наступного дня нарождення від поточної дати
    Робить перевірку на корректність введених данних
    '''
    @classmethod
    def range_control(cls, variable, left_range, right_range):
        if left_range <= variable <= right_range:
            return variable
        else:
            raise ValueError(f'Your data {variable} shall be in range from {left_range} up to {right_range}')

    @Field.value.setter
    def value(self, birthday_str):
        birth_list = birthday_str.split('.')
        if (len(birth_list) < 3) or (len(birth_list) > 3):
            print('Please type birthday in format "year.month.day"')
        year = [num for num in birth_list if len(num) == 4]
        year_index_in_list = birth_list.index(year[0])
        index_day = [2 if year_index_in_list == 0 else 0]

        year = self.range_control(int(year[0]), 1920, 2022)
        month = self.range_control(int(birth_list[1]), 1, 12)
        day = self.range_control(int((birth_list[index_day[0]])), 1, 31)

        self._value = datetime(year=year, month=month, day=day).date()

    def day_to_next_birthday(self):
        current_year = datetime.now().year
        current_day = datetime.now()
        this_year_birthday = datetime(year=current_year, month=self._value.month, day=self._value.day)
        if (this_year_birthday - current_day).days >= 0:
            next_birth = this_year_birthday - current_day
            return f'Days to birthday is {next_birth.days}'
        else:
            next_birth = datetime(year=current_year + 1, month=self._value.month, day=self._value.day)
            return f'Days to birthday is {(next_birth - current_day).days}'


