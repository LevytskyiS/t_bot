from main import *
from fields_for_record import Note

FUNC_1_LIST = ("Add new contact", "Check contact", \
    "Find information in the book", "Show all book")
FUNC_2_LIST = ("Add information", "Change information", "Delete information", \
    "Check how many days to birthday", "Remove contact from book")
ATTRIBUTES_LIST = ("Phone", "Birthday", "Email", "Tag", "Note")

@input_error
def boris():
    def fast_adding(new_contact_name, new_record):
            print(f"\nDo you wanna add information about '{new_contact_name.title()}' ? (•¿•)")
            print("1 : Yes")
            print("2 : No")
            new_contact_name = new_contact_name.lower()
            while True:    
                choosing_a = input("\nChoose № >>> ") 
                if not choosing_a:
                    break
                elif choosing_a == "1":
                    add_main_atributes(new_contact_name, new_record)
                    break
                elif choosing_a == "2":
                    break
                else:
                    print(f"\nWhat is it '{choosing_a}' ??? (o_O)?")

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
                fast_adding(new_contact_name, new_record)
            else:
                print(f"\nThe contact with the name '{new_contact_name.title()}' already exists in the AB (-_-)")
        
        elif choosing == "2":
            name = input("Which contact would you like to change? >>> ")
            name = name.lower()
            search_entry = address_book.data.get(name)
            if search_entry:
                print(f"\nWhat would you like to do with contact '{name.title()}' (° ͜ʖ°)\n")
                main_comands(name, search_entry)
            else:
                print(f"I didn't find any contact with name '{name.title()}' in AB (-_-)")
        
        elif choosing == "3":
            information = input("What are you looking for? >>> ")
            print(address_book.search_in_contact_book(information))
        
        elif choosing == "4":
            print(address_book)
        
        else:
            print(f"\nWhat is it '{choosing}' ??? (o_O)?")


@input_error
def main_comands(name, search_entry):
    showing = dict(enumerate(FUNC_2_LIST, 1))
    for k, v in showing.items():
        print(f"{k} : {v}")
    
    while True:    
        
        choosing = input("\nChoose № >>> ")
        
        if not choosing:
            break
        
        elif choosing == "1":
            add_main_atributes(name, search_entry)
            break
        
        elif choosing == "2":
            change_main_atributes(name, search_entry)
            break
        
        elif choosing == "3":
            del_main_atributes(name, search_entry)
            break

        elif choosing == "4":
            print(days_to_birth_func(name))
            break

        elif choosing == "5":
            print(address_book.delete_record(name))
            break
        
        else:
            print(f"\nWhat is it '{choosing}' ??? (o_O)?")

@input_error
def add_main_atributes(name, search_entry):
    showing = dict(enumerate(ATTRIBUTES_LIST, 1))
    for k, v in showing.items():
        print(f"{k} : {v}")
    
    while True:    
        
        choosing = input("\nChoose № >>> ")
        
        if not choosing:
            break
        
        elif choosing == "1":
            value = input(f"Write phone for '{name.title()}' >>> ")
            if value:
                print(add_phone_func([name, value]))
                break
            else:
                break
        
        elif choosing == "2":
            value = input(f"Write birthday for '{name.title()}' >>> ")
            if value:
                print(add_birth_func([name, value]))
                break
            else:
                break
        
        elif choosing == "3":
            value = input(f"Write email for '{name.title()}' >>> ")
            if value:
                print(add_mail_func([name, value]))
                break
            else:
                break

        elif choosing == "4":
            value = input(f"Write one #tag or #tags (separatet by ' ') for '{name.title()}' >>> ")
            if value:
                if not search_entry.tag:
                    print(add_tag_func([name, value]))
                    break
                else:
                    value = value.split(' ')
                    search_entry.change_tag(value)
                    break
            else:
                break

        elif choosing == "5":
            value = input(f"Write note for '{name.title()}' >>> ")
            if value:
                if not search_entry.note:
                    print(add_note_func([name, value]))
                    break
                else:
                    old_note = search_entry.note.value
                    note = old_note + value   
                    search_entry.note = Note(note)
                    print(f"The note < {value} > was added to the contact < {name.title()} >.")
                    break
            else:
                break
        
        else:
            print(f"\nWhat is it '{choosing}' ??? (o_O)?")

    print(f"\nDo you wanna add something else to the '{name.title()}' ? (•¿•)")
    print("1 : Yes")
    print("2 : No")
    while True:    
        
        choosing_2 = input("\nChoose № >>> ")
        
        if not choosing_2:
            break
        
        elif choosing_2 == "1":
            add_main_atributes(name, search_entry)
            break
        
        elif choosing_2 == "2":
            break

        else:
            print(f"\nWhat is it '{choosing_2}' ??? (o_O)?")

@input_error
def change_main_atributes(name, search_entry):
    showing = dict(enumerate(ATTRIBUTES_LIST, 1))
    for k, v in showing.items():
        print(f"{k} : {v}")
    
    while True:    
        
        choosing = input("\nChoose № >>> ")
        
        if not choosing:
            break
        
        elif choosing == "1":
            value = input(f"Write new phone for '{name.title()}' >>> ")
            if value:
                print(change_phone_func([name, value]))
                break
            else:
                break
        
        elif choosing == "2":
            value = input(f"Write new birthday for '{name.title()}' >>> ")
            if value:
                print(change_birth_func([name, value]))
                break
            else:
                break
        
        elif choosing == "3":
            value = input(f"Write new email for '{name.title()}' >>> ")
            if value:
                print(change_mail_func([name, value]))
                break
            else:
                break

        elif choosing == "4":
            value = input(f"Write one #tag or #tags (separatet by ' ') for '{name.title()}' >>> ")
            if value:
                if not search_entry.tag:
                    print(add_tag_func([name, value]))
                    break
                else:
                    value = value.split(' ')
                    search_entry.change_tag(value)
                    break
            else:
                break

        elif choosing == "5":
            value = input(f"Write note for '{name.title()}' >>> ")
            if value:
                if not search_entry.note:
                    print(add_note_func([name, value]))
                    break
                else:
                    old_note = search_entry.note.value
                    note = old_note + value   
                    search_entry.note = Note(note)
                    print(f"The note < {value} > was added to the contact < {name.title()} >.")
                    break
            else:
                break
        
        else:
            print(f"\nWhat is it '{choosing}' ??? (o_O)?")
    
    print(f"\nDo you wanna change something else to the '{name.title()}' ? (•¿•)")
    print("1 : Yes")
    print("2 : No")
    while True:    
        
        choosing_2 = input("\nChoose № >>> ")
        
        if not choosing_2:
            break
        
        elif choosing_2 == "1":
            change_main_atributes(name, search_entry)
            break
        
        elif choosing_2 == "2":
            break

        else:
            print(f"\nWhat is it '{choosing_2}' ??? (o_O)?")

@input_error
def del_main_atributes(name, search_entry):
    showing = dict(enumerate(ATTRIBUTES_LIST, 1))
    for k, v in showing.items():
        print(f"{k} : {v}")
    
    while True:    
        
        choosing = input("\nChoose № >>> ")
        
        if not choosing:
            break
        
        elif choosing == "1":
            print(del_phone_func([name]))
            break
        
        elif choosing == "2":
            pass
        
        elif choosing == "3":
            print(delete_mail_func([name]))
            break

        elif choosing == "4":
            print(f"\nDo you want to remove one or ALL! tags from the '{name.title()}' ? (•¿•)")
            print("1 : Remove only one tag ")
            print("2 : !!! Delete all tags !!! ")
            print("3 : I changed my mind, I don't want to delete anything")
            while True:     
                choosing_t = input("\nChoose № >>> ") 
                if not choosing_t:
                    break  
                elif choosing_t == "1":
                    search_entry.del_tag()
                    break           
                elif choosing_t == "2":
                    print(search_entry.delete_tags())
                    break
                elif choosing_t == "3":
                    break
                else:
                    print(f"\nWhat is it '{choosing_t}' ??? (o_O)?")
            break            

        elif choosing == "5":
            if search_entry:
                deleted_note = search_entry.note.value
                search_entry.note = Note('')
                print(f"The note '{deleted_note}' of contact '{name.title()}' was deleted.")
                break
            else:
                print(f"Note list of '{name.title()}' is already empty.")
                break
        
        else:
            print(f"\nWhat is it '{choosing}' ??? (o_O)?")
    
    print(f"\nDo you want to delete something else in '{name.title()}' ? (•¿•)")
    print("1 : Yes")
    print("2 : No")
    while True:    
        
        choosing_3 = input("\nChoose № >>> ")
        
        if not choosing_3:
            break
        
        elif choosing_3 == "1":
            del_main_atributes(name, search_entry)
            break
        
        elif choosing_3 == "2":
            break

        else:
            print(f"\nWhat is it '{choosing_3}' ??? (o_O)?")

boris()




    





