from address_book import address_book


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
                break

    finally:
        address_book.save_address_book()           


if __name__ == '__main__':
    main()    