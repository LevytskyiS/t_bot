import re


class Field:
    pass


class Email(Field):

    @Field.value.setter
    def value(self, email: str):

        new_email = re.search(r".+@.+", email)

        if not new_email:
            return "Email is not valid."

        self._value = new_email.group()
        