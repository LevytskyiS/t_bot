from address_book import address_book


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact doesn't exist, please try again."
        except ValueError:
            return "Number must contain only numbers/the number is too short/the date is incorrect."
        except IndexError:
            return "Wrong format. Must be '{command} {name} {value}'."
        except TypeError:
            return "Unknown command or parameters, please try again."
        except AttributeError:
            return "Wrong format of date."
        except StopIteration:
            return "There are no other numbers in the book."

    return inner


def help_func(*_) -> str:
    pass


def add_func(args: list) -> str:
    pass


def add_phone_func(args: list) -> str:
    pass


def change_phone_func(args: list) -> str:
    pass


def phone_func(args: list) -> str:
    pass


def del_phone_func(args: list) -> str:
    pass


def show_all_func(*_) -> str:
    pass


def add_birth_func(args: list) -> str:
    pass


def change_birth_func(args: list) -> str:
    pass


def days_to_birth_func(*_) -> str:
    pass


def all_birth_func(args: list) -> str:
    pass


def add_note_func(args: list) -> str:
    pass


def change_note_func(args: list) -> str:
    pass


def del_note_func(args: list) -> str:
    pass


def add_tag_func(args: list) -> str:
    pass


def find_tag_func(args: list) -> str:
    pass


def find_func(args) -> str:
    pass


def sort_func(args) -> str:
    pass


def exit_func(*_)-> str:
    """
    The function close bot.
    """
    return "Good bye!"

#Importantly! The more words in the bot command, the higher they are in the dictionary.
FUNCTIONS = {
    "days to birth": days_to_birth_func,
    "add phone": add_phone_func,
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