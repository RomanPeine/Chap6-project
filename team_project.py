def menu():
    #menu accepts no arguments
    #prompts the user to choose an option
    #returns the users choice
    print("1) Add contact\n2) Search contact\n3) Edit contact\n4) Delete contact\n5) Display contacts")
    return input("\nEnter your choice: ")
    
def main():
    #accepts no arguments
    #runs the contact program
    #calls all other programs
    keep_going = "y"
    while keep_going.lower() == "y" or keep_going.lower() == "yes":
        choice = menu()
        if choice == "1":
            add_contact()
        if choice == "2":
            search_contact()
        if choice == "3":
            edit_contact()
        if choice == "4":
            delete_contact()
        if choice == "5":
            display_contact()
        keep_going = input("\nDo you want to use the menu again if so enter y or yes: ")
    
def add_contact():
    #accepts no arguements
    #adds a contact to the contact list
    contacts = open("contact.txt", "a")
    contacts.write(input("Name: ") + "\n")
    contacts.write(input("Street Address: ") + "\n")
    contacts.write(input("Phone Number: ") + "\n")
    contacts.write(input("Email Adress: ") + "\n")
    contacts.close()
    
import os
    
def search_contact():
    #accepts no arguements
    #searches and pulls info for a specific contact
    #displays the info
    found = False
    
    search = input('Enter a contact to search for: ')
    
    try:
        contact_file = open('contact.txt', 'r')
        
        name = contact_file.readline()
        
        while name!= '':
            street = contact_file.readline()
            phone = contact_file.readline()
            email = contact_file.readline()
            
            
            name = name.rstrip('\n')
            
            if name.lower() == search.lower():
                print('\nContact Found!')
                print('\nName: ', name.rstrip())
                print('Street Address: ', street.rstrip())
                print('Phone Number: ', phone.rstrip())
                print('Email Address: ', email.rstrip())
                found = True
                
            
            name = contact_file.readline()
        
        contact_file.close()
        
        if not found:
            print('\n--- The contact was not found ---\n')
                    
    except Exception as e:
        print('ERROR: Error reading file')
        



   

def edit_contact():
    #accepts no arguements
    #edits a contacts info
    found = False
    
    search = input('Enter the contact description to modify: ')
    option_street = input('Do you want to change your street address(y/n): ')
    option_phone = input('Do you want to change your phone number(y/n): ')
    option_email = input('Do you want to change your email address(y/n): ')
    changes = 0
    
    
    if option_street.lower() == 'y':
        new_street = input('Enter new street address: ')
        changes = 1
        
    if option_phone.lower() == 'y':
        new_phone = input('Enter new phone number: ')
        changes = 1
        
    if option_email.lower() == 'y':
        new_email = input('Enter new email address: ')
        changes = 1
       
    if changes == 0:
        print("No changes made")
    
    try:
        contact_file = open('contact.txt', 'r')
        temp_file = open('temp.txt', 'w')
        
        name = "yes"
        
        while name != '':
            name = contact_file.readline()
            street = contact_file.readline()
            phone = contact_file.readline()
            email = contact_file.readline()
            
            name = name.rstrip('\n')
            street = street.rstrip('\n')
            phone = phone.rstrip('\n')
            email = email.rstrip('\n')
            
            if search.lower() == name.lower():
                temp_file.write(name + '\n')
                found = True
                if option_street.lower() == 'y':
                    temp_file.write(new_street + '\n')
                else:
                    temp_file.write(street + '\n')
                    
                if option_phone.lower() == 'y':
                    temp_file.write(new_phone + '\n')
                else:
                    temp_file.write(phone + '\n')
                    
                if option_email.lower() == 'y':
                    temp_file.write(new_email + '\n')
                else:
                    temp_file.write(email + '\n')
                    
            else:
                temp_file.write(name + '\n')
                temp_file.write(street + '\n')
                temp_file.write(phone + '\n')
                temp_file.write(email + '\n')

                
                
        name = contact_file.readline()
    except Exception as e:
        print('ERROR: Error reading file')
        
    contact_file.close()
    temp_file.close()
    
    os.remove('contact.txt')
    
    os.rename('temp.txt', 'contact.txt')
    
    if found == False:
        print('\nContact not found.')
    else:
        print('The information has been changed.')
  

def delete_contact():
    #accepts no arguements
    #deletes a contact
    found = False
    search = input("Enter the contact you want to delete: ")
    try:
        contact_file = open('contact.txt', 'r')
        temp_file = open('temp.txt', 'w')
        
        name = contact_file.readline()
        
        while name != '':
            street = contact_file.readline()
            phone = contact_file.readline()
            email = contact_file.readline()
            
            name = name.rstrip('\n')
            street = street.rstrip('\n')
            phone = phone.rstrip('\n')
            email = email.rstrip('\n')
            
                    
            if name.lower() != search.lower():
                temp_file.write(name + '\n')
                temp_file.write(street + '\n')
                temp_file.write(phone + '\n')
                temp_file.write(email + '\n')    
            name = contact_file.readline()
    except Exception as e:
        print('ERROR: Error reading file')
        
    contact_file.close()
    temp_file.close()
    
    os.remove('contact.txt')
    
    os.rename('temp.txt', 'contact.txt')
    
    if found == True:
        print('\nContact not found.')
    else:
        print('The information has been changed.')

   

def display_contact():
    #accepts no arguements
    #displays all contacts
    contacts = open("contact.txt", "r")
    line1 = contacts.readline().rstrip("\n")
    print("")
    while line1 != '':
        line2 = contacts.readline().rstrip("\n")
        line3 = contacts.readline().rstrip("\n")
        line4 = contacts.readline()
        print(line1)
        print(line2)
        print(line3)
        print(line4)
        line1 = contacts.readline().rstrip('\n')             
    contacts.close()