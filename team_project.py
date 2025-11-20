import io
def menu():
    pass
def main():
    while keep_going.lower() = "y" or keep_going.lower() == "yes":
        choice = menu()
        if choice == 1:
            add_contact()
        if choice == 2:
            search_contact()
        if choice == 3
            edit_contact()
        if choice == 4:
            delete_contact()
        if choice == 5:
            display_contact()
        keep_going == input("\nDo you want to use the menu again if so enter y or yes: ")
def add_contact():
    pass
def search_contact():
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
            
            if desc.lower() == search.lower():
                print('\nContact Found!')
                print('Name: ', name)
                print('Street Address: ', street)
                print('Phone Number: ', phone)
                print('Email Address: ', email)
                found = True
                
            
            name = contact_file.readline()
        
        contact_file.close()
        
        if not found:
            print('\n--- The contact was not found ---\n')
                
    except Exception as e:
        print('ERROR: Error reading file')
        



def edit_contact():
    found = False
    
    search = input('Enter the contact description to modify: ')
    option_street = input('Do you want to change your street address(y/n): ')
    option_phone = input('Do you want to change your phone number(y/n): ')
    option_email = input('Do you want to change your email address(y/n): ')
    
    
    if option_street.lower = 'y':
        new_street = input('Enter new street address: ')
        
    elif option_phone.lower = 'y':
        new_phone = input('Enter new phone number: ')
        
    elif option_email.lower = 'y':
        new_email = input('Enter new email address: ')
       
    else:
        print('No changes made')
    
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
            
            if search.lower() == name.lower():
                temp_file.write(name + '\n')
                if option_street.lower = 'y':
                    temp_file.write(new_street + '\n')
                    
                elif option_street.lower = 'y':
                    temp_file.write(new_phone + '\n')
                    
                elif option_street.lower = 'y':
                    temp_file.write(new_email + '\n')
                    
                    
                if found = True
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
    if search.lower() != name.lower():
        temp_file.write(name + '\n')
                temp_file.write(street + '\n')
                temp_file.write(phone + '\n')
                temp_file.write(email + '\n')
        
    else:
        found = True






def display_contact():
    pass