from main import *

FUNC_1_LIST = ("Add new contact", "Change information about contact", "Show all book")
FUNC_2_LIST = ("Add", "Change", "Del")
ATTRIBUTES_LIST = ("Phone", "Birthday", "Email", "Tag", "Note")

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
                print(f"\nThe contact '{new_contact_name}' successfully added ♥")
            else:
                print(f"\nThe contact with the name '{new_contact_name}' already exists in the AB -_- ")
        
        elif choosing == "2":
            pass
        
        elif choosing == "3":
            print(address_book)
        
        else:
            print(f"What is it < {choosing} >??? (o_O)?")

def main_comands():
    pass

def main_atributes():
    pass

boris()




    





