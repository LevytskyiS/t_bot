from main import *

FUNC_1_LIST = ("Add new contact", "Change information about contact", \
    "Find information in the book", "Show all book")
FUNC_2_LIST = ("Add information", "Change information", "Delete information", "Remove contact from book")
ATTRIBUTES_LIST = ("Phone", "Birthday", "Email", "Tag", "Note")

@input_error
def boris():
    print("\nDobriy den everybody, I'm Boris Jonson from London ♥ (ʘ‿ʘ) ♥")
    print("Oh, sorry, I'm joking ^▿^ I'm just a cool bot (◕‿◕) ")
    while True:
        print("\nHow can I help you? •௰•")
        print("You always can skip any comand if you want to exit (⌐■_■)\n")
        
        showing = dict(enumerate(FUNC_1_LIST, 1))
        for k, v in showing.items():
            print(f"{k} : {v}")
        choosing = input("\nChoose № >>> ")
        
        if not choosing:
            return "See you later!  ͡° ͜ʖ ͡° "
        
        elif choosing == "1":
            new_contact_name = input("Write name of your new contact >>> ")
            new_record = Record(new_contact_name)
            if new_record.name.value not in address_book.keys():
                address_book.add_record(new_record)
                print(f"\nThe contact '{new_contact_name.title()}' successfully added ♥")
            else:
                print(f"\nThe contact with the name '{new_contact_name}' already exists in the AB (-_-)")
        
        elif choosing == "2":
            name = input("Which contact would you like to change? >>> ")
            name = name.lower()
            search_entry = address_book.data.get(name)
            if search_entry:
                print(f"\nWhat would you like to do with contact '{name.title()}' (° ͜ʖ°)\n")
                main_comands(search_entry, name)
            else:
                print(f"I didn't find any contact with name '{name.title()}' in AB (-_-)")
        
        elif choosing == "3":
            information = input("What are you looking for? >>> ")
            print(address_book.search_in_contact_book(information))
        
        elif choosing == "4":
            print(address_book)
        
        else:
            print(f"\nWhat is it '{choosing}' ??? (o_O)?")


def main_comands(search_entry, name):
    showing = dict(enumerate(FUNC_2_LIST, 1))
    for k, v in showing.items():
        print(f"{k} : {v}")
    
    while True:    
        
        choosing = input("\nChoose № >>> ")
        
        if not choosing:
            break
        
        elif choosing == "1":
            add_main_atributes()
            break
        
        elif choosing == "2":
            change_main_atributes()
            break
        
        elif choosing == "3":
            del_main_atributes()
            break

        elif choosing == "4":
            print(address_book.delete_record(name))
            break
        
        else:
            print(f"\nWhat is it '{choosing}' ??? (o_O)?")


def add_main_atributes():
    showing = dict(enumerate(ATTRIBUTES_LIST, 1))
    for k, v in showing.items():
        print(f"{k} : {v}")
    
    while True:    
        
        choosing = input("\nChoose № >>> ")
        
        if not choosing:
            break
        
        elif choosing == "1":
            pass
        
        elif choosing == "2":
            pass
        
        elif choosing == "3":
            pass

        elif choosing == "4":
            pass

        elif choosing == "5":
            pass
        
        else:
            print(f"\nWhat is it '{choosing}' ??? (o_O)?")


def change_main_atributes():
    showing = dict(enumerate(ATTRIBUTES_LIST, 1))
    for k, v in showing.items():
        print(f"{k} : {v}")
    
    while True:    
        
        choosing = input("\nChoose № >>> ")
        
        if not choosing:
            break
        
        elif choosing == "1":
            pass
        
        elif choosing == "2":
            pass
        
        elif choosing == "3":
            pass

        elif choosing == "4":
            pass

        elif choosing == "5":
            pass
        
        else:
            print(f"\nWhat is it '{choosing}' ??? (o_O)?")


def del_main_atributes():
    showing = dict(enumerate(ATTRIBUTES_LIST, 1))
    for k, v in showing.items():
        print(f"{k} : {v}")
    
    while True:    
        
        choosing = input("\nChoose № >>> ")
        
        if not choosing:
            break
        
        elif choosing == "1":
            pass
        
        elif choosing == "2":
            pass
        
        elif choosing == "3":
            pass

        elif choosing == "4":
            pass

        elif choosing == "5":
            pass
        
        else:
            print(f"\nWhat is it '{choosing}' ??? (o_O)?")

boris()




    





