def print_menu():
    print('1. Look up a number')
    print('2. Set an entry')
    print('3. Remove a Phone Number')
    print('4. List all entries')
    print ('5. Save all entries')
    print ('6. Restore saved entries')
    print('7. Quit')

numbers = { "Alice": {
  'number': '451-1222',
  'email': 'alice@gmail.com',
  'website': 'www.alice.com',
  },

    'Bob': {
      'number': '1234-567',
      'email': 'bob@bob.com',
      'website': 'www.bob.com'
    },

    'Alex': {
      'number': '456-1923',
      'email': 'alex@hotmail.com',
      'website': 'www.alex.com'
    },
}



print type(numbers)
print numbers.keys

menu_choice = 0
print_menu()
while menu_choice != 7:
    menu_choice = int(input("Type in a number (1-7): "))
    if menu_choice == 1:
        open ('phonebook.txt', -r)
        name = raw_input("What is their name? ")
        if name in numbers:
            print 'Phone Number = ', numbers[name]['number']
            print 'E-Mail = ', numbers[name]['email']
            print 'Website = ', numbers[name]['website']
        else:
            print(name, "was not found")
    elif menu_choice == 2:
        print("Add Contact Info")
        name = 'name: ' + raw_input("Name: ")
        phone = 'number: ' + raw_input("Number: ")
        email = 'email: ' + raw_input('Email: ')
        website = 'website: ' + raw_input('Website: ')
        numbers[name] = phone, email, website
    elif menu_choice == 3:
        print("Remove Name and Number")
        name = raw_input("Name: ")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "was not found")
    elif menu_choice == 4:
        print numbers
        print()
    elif menu_choice == 5:
        save = open("phonebook.txt","w")
        save.write(str(numbers))
        save.close()
    elif menu_choice == 6:
        with open('phonebook.txt','r') as inf:
            numbers = eval(inf.read())
        print "Restore saved entries"
    elif menu_choice == 7:
        print "Bye!"
        break
    elif menu_choice != 7:
        print_menu()
