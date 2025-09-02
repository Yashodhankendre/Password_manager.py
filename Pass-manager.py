import json
import os
import random
import pandas as pd

File_name = 'Pass_manager.json'

def load_data():
    if not os.path.exists(File_name):
        return {}
    with open(File_name,'r') as f:
        return json.load(f)

def save_data(data):
    with open(File_name,'w')as f:
        return json.dump(data,f,indent =4)

def generate_password(length):

    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_+{}|?/"

    password = ""  

    for i in range(length):
        password += random.choice(characters)  

    return password
  
def add_details():
    details = load_data()
    
    name_input = input('Enter your Name : ').capitalize()
    email_input = input('Enter the email e.g. xyz1234@gmail.com: ')

#  EMAIL TYPO CHECK SYSTEM   
    domains = [
         '@gmail.com',
         '@googlemail.com',
         '@company.com',
         '@ngo.org',
         '@brand.co',
         '@school.edu',
         '@university.ac.uk',
         '@agency.gov',
         '@city.gov.uk',
         '@gov.in',
         '@gov.au',
         '@Yahoo.com'
        ]
    parts = email_input.split('@')
    if len(parts)!=2:
        print('enter the valid email ')

    name_part = parts[0]
    domain_part = '@' + parts[1]

    if domain_part not in domains:
        print('Please enter a valid domain name e.g @gmail.com ')
        return
    
    for user, info in details.items():
        if info["Email"] == email_input:
            print("Email already exists, cannot create duplicate.")
            return

# PASSWORD SECTION
    print(f'SUGGESTION → {generate_password(12)}')

    password_input = input('Enter the password: ')

# STORE DATA SECTION
    details[f'{name_input}'] = {
        "Email": email_input,
        "Password": password_input
    }

    save_data(details)
    print('Data saved ✅')


def update_password():
    details = load_data()
    name_input = input('Enter your Name : ').capitalize()
    email_input = input('Enter the email to change its password : ')
    update_input = input('Enter New password : ')

    details[f'{name_input}'] = {
        "Email": email_input,
        "Password": update_input
    }
    if name_input  not in details:
        print('Enter the correct name ')
        return
    if email_input in details:
        details['Password'] = update_input
    else:
        print('enter the correct email address.')
        return

    save_data(details)
    print('updated')

def view_details():
    details = load_data()
    name_input = input('Enter your Name : ').capitalize()
    email_input = input('Enter the email : ')
    for user,info in details.items():
        print(f'Name{name_input},\n Email:{info['Email']},\n password:{info['Password']}')

def delete_details():
    pass

def main():
    print(f'\n WELCOME TO PASSWORD MANAGER \n')
    while True:
        print('1.ADD Email And Password ')
        print('2.Update password ')
        print('3.View Password' )
        print('4.Delete Password and Email')
        print('5.Exit the APP\n')
        try:
            choice_input = int(input('Enter the option- '))
        except ValueError:
            print('Invalid choice input correct option')
        if choice_input == 1:
            add_details()
        elif choice_input == 2:
            update_password()
        elif choice_input == 3:
            view_details()
        elif choice_input == 4:
            delete_details()
        elif choice_input == 5:
            print('\nExiting the app...')
            break

if __name__ == '__main__':
    main()


