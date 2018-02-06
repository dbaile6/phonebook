def print_menu():
    print('1. Look up a number')
    print('2. Set an entry')
    print('3. Remove a Phone Number')
    print('4. List all entries')
    print('5. Quit')

class Contact():
    def __init__(self, first, last, number):
        self.first = first
        self.last = last
        self.number = number
    def greet(self):
        print 'Hi, i\'m %s' % self.first

dylan = Contact('Dylan', 'Bailey', '123-6512')
jennifer = Contact('Jennifer', 'Opert', '651-1025')

print dylan.greet()

contacts = [
{'name': 'Dylan', 'last': 'Bailey', 'number': '123-6512'},
{'name': 'Jennifer', 'last': 'Opert', 'number': '651-1025'}
]

def getFirstName(c):
    return c['first']

def getSortable(c):
    return (c['name'], c['last'], c['number'])

sortedContacts = sorted(contacts, reverse=True, key=getSortable)

menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = int(input("Type in a number (1-5): "))
    if menu_choice == 1:
        print("Telephone Numbers")
        name = raw_input("Name: ")
        if name in contacts:
            print("The number is", Contact(number))
        else:
            print(name, "was not found")
    elif menu_choice == 2:
        print("Add Name and Number")
        name = raw_input("Name: ")
        phone = raw_input("Number: ")
        contacts[name] = phone
        print "Entry stored for ", name
    elif menu_choice == 3:
        print("Remove Name and Number")
        name = raw_input("Name: ")
        if name in contacts:
            del contacts[name]
            print name, " was deleted"
        else:
            print(name, "was not found")
    elif menu_choice == 4:
        print sortedContacts
        print()
    elif menu_choice != 5:
        print_menu()
