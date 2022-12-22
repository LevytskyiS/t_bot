from address_book import address_book


def exit_func():
    return "Good bye!"


def notes_func(args):
    return    


FUNCTIONS = {
    "exit": exit_func,
    "notes": notes_func
    }


def handler(input_string: str) -> list:
    """
    The function separates the command word for the bot, and writes all other data into a list, where the first value is the name
    """
    command = input_string
    data = ""
    data_list = []
    for key in FUNCTIONS:
        if input_string.strip().lower().startswith(key):
            command = key
            data = input_string[len(command):]
            break

    if not input_string.strip().lower().startswith(key):
        raise ValueError("This command is wrong.")

    if data:
        name, *args = data.strip().split(" ")
        args = " ".join(args)
        data_list.append(name)
        data_list.append(args)
        return FUNCTIONS[command](data_list)
    
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
                break

    finally:
        address_book.save_address_book()           


if __name__ == '__main__':
    main()    