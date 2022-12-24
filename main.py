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
            return "Can't find information about this contact."
        except StopIteration:
            return "There are no other numbers in the book."

    return inner

@input_error
def help_func(*_) -> str:
    options_bot_str = {

    "add Natally": "I will save the friend's name",
    "show all 3/showll all": "I will show the entire list of contacts / all contacts",
    "del contact Natally": "I will delete the contact",
    
    "add phone Natally 096-45-34-876": "I will add a number to your contact",
    "change phone Natally 0995456743 0986754325": "I will change your friend's phone number",
    "phone Natally": "I will show your friend's phone, just enter the name",
    "del phone Natally 096-45-34-876": "I will delete your contact's phone number",
    
    "add mail Vasya vasiliy007@gmail.com": "I will add email to your contact",
    "change mail Vasya new_mail_vasya@gmail.com": "I will change email of your contact",
    "del mail Vasya": "I will delete email of your contact",
    
    "add birth Natally 1999.12.23": "I will add the birthday of your friend so that you do not forget to congratulate",
    "change birth Natally 1999.12.23": "I will change your friend's date of birth",
    "all births 50": "I will show the birthdays of all your friends in the next 50 days",
    "days to birth Leo": "I will tell you the number of days until my friend's birthday",

    "add note Natally str. Peremogy, house 76.": "I will add notes to the contact",
    "change note Natally str. Gagarina, h.126.": "I will change the contact notes",
    "del note Natally": "I will delete contact notes",

    "add tag Natally #address #favorite": "I will add tags",
    "find tag #favorite": "I will show notes with such tags",
    "del tag": "I will delete a note's tag",
    
    "help": "I will tell you about my possibilities",
    "sort": "I will sort all the files in the folder you choose",
    "find mi": "I will find all record, which contains 'mi'",
    f"{EXIT_COMMANDS}": "Enter one of these word and I will finisg my work",
    
    }

    table_options_bot = ""
    header_table = "| {:<51} | {:<80}".format("Example command", "Command description") # в наст. рядку header_table повертає строку на початку якої ще є текст "\x1b[1m\x1b[34m", тому ширина перщої колонки 25 символів
    header_table = "\033[1m\033[34m{}\033[0m".format(header_table)  
    table_options_bot += f"\n{header_table}\n\n"
    
    for key, value in options_bot_str.items():
        key = "\033[34m{}\033[0m".format(key)
        row = "| {:<60} | {:<80}".format(key, value)
        table_options_bot += f"{row}\n"

    return table_options_bot    

@input_error
def add_func(args: list) -> str:
    record = Record(args[0])
    if record.name.value not in address_book.keys():
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
    contact_name = args[0]
    phone = args[1]
    if contact_name in address_book.keys() and phone not in [p.value for p in address_book[contact_name].phones]:
        return address_book[contact_name].add_phone(phone)
    else:
        return f"There is no '{contact_name}' in your AB or the {phone} already exists in the list."
        

@input_error
def change_phone_func(args: list) -> str:
    '''Змінює номер телефону контакту {name}'''
    
    name, old_phone, new_phone = args
    record = address_book.data.get(name)

    return record.change_phone(old_phone, new_phone)
   

@input_error
def phone_func(args: list) -> str:
    name = args[0]
    record = address_book.data.get(name)
    if record:
        phones_list = [phone.value for phone in record.phones]
        return f"{record.name.value.title()} has this phones {phones_list}"
    return f"I didn't find any < {name} > in your Address Book."

@input_error
def del_phone_func(args: list) -> str:
    '''Видаляє існуючий номер телефону'''

    name, phone = args    
    record = address_book.data.get(name)
    
    return record.delete_phone(phone)

@input_error
def add_mail_func(args: list) -> str:

    record = address_book[args[0]]

    return record.add_mail(args[1])

@input_error
def change_mail_func(args: list) -> str:

    name, new_mail = args
    record = address_book.data.get(name)

    return record.change_mail(new_mail)

@input_error
def delete_mail_func(args: list) -> str:

    name = args[0]
    record = address_book.data.get(name)

    return record.delete_mail()


@input_error
def show_all_func(*_) -> str:
    return address_book


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
        return f"{args[0].title()}'s birthday will be in {record.days_to_birthdays()} days."
    else:
        return f'The name {args[0].title()} is not exist. Please add first'


@input_error
def all_birth_func(*_) -> str:
    return address_book.all_birthdays()

@input_error
def add_note_func(args: list) -> str:

    record = address_book[args[0]]

    return record.add_note(args[1:])

@input_error
def change_note_func(args: list) -> str:
    name, *new_note = args 
    record = address_book.data.get(name)

    return record.change_note(new_note)

@input_error
def del_note_func(args: list) -> str:
    name = args[0]
    record = address_book.data.get(name)

    return record.delete_note()

@input_error
def add_tag_func(args: list) -> str:

    record = address_book[args[0]]
    
    return record.add_tag(args[1:])

@input_error
def find_tag_func(args: list) -> str:
    pass

@input_error
def find_func(args) -> str:
    return address_book.search_in_contact_book(args)

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
    """The function close bot."""
    return exit("Good bye!")

@input_error
def what_is_command(commands: list|dict, user_input: str) -> str:
    count = 0
    command_out = ""

    for command in commands:

        i = 0

        for char_in, char_comm in zip(user_input, command):

            if char_in == char_comm:
                i += 1

        if i > count:
            count = i
            command_out = command

    return command_out


#Importantly! The more words in the bot command, the higher they are in the dictionary.
FUNCTIONS = {
    "days to birth": days_to_birth_func,
    "add phone": add_phone_func,
    "add mail": add_mail_func,
    "del contact": delete_record_func,
    "change phone": change_phone_func,
    "change mail": change_mail_func,
    "del phone": del_phone_func,
    "del mail": delete_mail_func,
    "show all": show_all_func,
    "add birth": add_birth_func,
    "change birth": change_birth_func,
    "all births": all_birth_func,
    "add note": add_note_func,
    "change note": change_note_func,
    "del note": del_note_func,
    "add tag": add_tag_func,
    "find tag": find_tag_func,
    "add": add_func,
    "help": help_func,
    "sort": sort_func,
    "find": find_func,
    "phone": phone_func
    }
    
EXIT_COMMANDS = ("good bye", "exit", "close", "quit", "bye", "q")

@input_error
def handler(input_string: str) -> list:
    """
    The function separates the command word for the bot, and writes all other data into a list, where the first value is the name
    """
    command = ""
    perhaps_command = what_is_command(FUNCTIONS, input_string)
    data = ""
    input_string = input_string.strip().lower()
    for key in FUNCTIONS:
        if input_string.startswith(key):
            command = key
            data = input_string[len(command):]
            break

    if not command and \
        input(f"If you mean '{perhaps_command}' enter 'y': ") == "y":

        command = perhaps_command
        input_string = input_string.split()[len(command.split()):]
        data = " ".join(input_string)
        print(f"data: {data}")


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
    The bot terminates after the words "good bye", "exit", "close", "quit", "bye"
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
            #print(address_book.data.keys())
            input_string = input("Input command, please: ")
            if input_string.lower() in EXIT_COMMANDS:
                exit_func()
            get_command = handler(input_string)
            print(get_command)
            

    finally:
        address_book.save_address_book()           


if __name__ == '__main__':
    main()

