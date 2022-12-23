import os
from address_book import address_book
from record import Record
from sort import sort_files


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact doesn't exist, please try again."
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return "Wrong format. Must be '{command} {name} {value}'."
        except TypeError:
            return "Unknown command or parameters, please try again."
        except AttributeError:
            return "Wrong format of date."
        except StopIteration:
            return "There are no other numbers in the book."

    return inner

@input_error
def help_func(*_) -> str:
    pass

@input_error
def add_func(args: list) -> str:
    record = Record(args[0])
    if record.name.value not in address_book.keys():
        record.add_phone(args[1])
        return address_book.add_record(record)
    else:
        return f"The contact with the name {args[0]} already exists in the AB."

@input_error
def delete_record_func(args: list) -> str:
    contact_name = args[0]
    if contact_name in address_book.keys():
        return address_book.delete_record(contact_name)
    return f"Name '{contact_name}' doesn't exist in your book."

@input_error
def add_phone_func(args: list) -> str:
    record = address_book[args[0]]
    return record.add_phone(args[1])


@input_error
def change_phone_func(args: list) -> str:
    '''Змінює номер телефону контакту {name}'''
    
    name, old_phone, new_phone = args   # Розпаковуємо аргументи
    record = address_book.data.get(name)   # Знаходимо {record} контакту {name}

    return record.change_phone(old_phone, new_phone)
   

@input_error
def phone_func(args: list) -> str:
    pass

@input_error
def del_phone_func(args: list) -> str:
    '''Видаляє існуючий номер телефону'''

    name, phone = args    
    record = address_book.data.get(name)
    
    return record.delete_phone(phone)

@input_error
def add_mail_func(args: list) -> str:
    pass

@input_error
def change_mail_func(args: list) -> str:
    pass

@input_error
def delete_mail_func(args: list) -> str:
    pass

@input_error
def show_all_func(*_) -> str:
    pass

@input_error
def add_birth_func(args: list) -> str:
    record = address_book[args[0]]
    if record:
        return record.add_birthday(args[1])
    else:
        return f'The name {args[0]} is not exist. Please add first'


@input_error
def change_birth_func(args: list) -> str:
    record = address_book[args[0]]
    if record:
        return record.change_birthday(args[1])
    else:
        return f'The name {args[0]} is not exist. Please add first'

@input_error
def days_to_birth_func(args: list) -> str:
    record = address_book[args[0]]
    if record:
        return record.days_to_birthdays()
    else:
        return f'The name {args[0]} is not exist. Please add first'


@input_error
def all_birth_func(args: list) -> str:
    pass

@input_error
def add_note_func(args: list) -> str:
    pass

@input_error
def change_note_func(args: list) -> str:
    pass

@input_error
def del_note_func(args: list) -> str:
    pass

@input_error
def add_tag_func(args: list) -> str:
    pass

@input_error
def find_tag_func(args: list) -> str:
    pass

@input_error
def find_func(args) -> str:
    pass

@input_error
def sort_func(*_) -> str:
    user_input = input(
        'Enter "1" if you want to sort files in the current folder.\n'
        'Enter "2" if you want to choose another folder.\n'
    )
    if user_input == '1':
        return sort_files(os.getcwd())
    elif user_input == '2':
        user_path = input('Enter a path: ')
        return sort_files(user_path)
    else:
        return f'You have to enter "1" or "2".'

@input_error
def exit_func(*_)-> str:
    """
    The function close bot.
    """
    return "Good bye!"

#Importantly! The more words in the bot command, the higher they are in the dictionary.
FUNCTIONS = {
    "days to birth": days_to_birth_func,
    "add phone": add_phone_func,
    "del contact": delete_record_func,
    "change phone": change_phone_func,
    "del phone": del_phone_func,
    "show all": show_all_func,
    "add birth": add_birth_func,
    "change birth": change_birth_func,
    "all births": all_birth_func,
    "add note": add_note_func,
    "change note": change_note_func,
    "del note": del_note_func,
    "add tag": add_tag_func,
    "find tag": find_tag_func,
    "good bye": exit_func,
    "exit": exit_func,
    "close": exit_func,
    "add": add_func,
    "help": help_func,
    "sort": sort_func,
    "find": find_func,
    "phone": phone_func
    }

@input_error
def handler(input_string: str) -> list:
    """
    The function separates the command word for the bot, and writes all other data into a list, where the first value is the name
    """
    command = input_string
    data = ""
    for key in FUNCTIONS:
        if input_string.strip().lower().startswith(key):
            command = key
            data = input_string[len(command):]
            break

    if not input_string.strip().lower().startswith(key):
        raise ValueError("This command is wrong.")

    if data:        
        args = data.strip().split(" ")
        return FUNCTIONS[command](args)
    
    return FUNCTIONS[command]()


def main():
    """
   The user enters through a space:
        - a command for the bot;
        - command, contact name, phone number or date of birth, email address, notes, tags,
    The function returns the bot's response and prints them.
    The bot terminates after the words "good bye" or "close" or "exit"
    """
    try: 
        print("")
        print("\033[1m\033[34m{}\033[0m".format("Hello, I am Bot-contacts:)"))
        print("")
        #print("Type 'help' to see all commands")
        help_str = "\033[34m{}\033[0m".format("help")
        print(f"Type {help_str} to see all commands")
        
        while True:
            print("")
            input_string = input("Input command, please: ")
            get_command = handler(input_string)
            print(get_command)
            if get_command == "Good bye!":
                exit()

    finally:
        address_book.save_address_book()           


if __name__ == '__main__':
    main()
