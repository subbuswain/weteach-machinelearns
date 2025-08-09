phonebook = [{'name': "ABC", 'phone': 453454675, 'city': "AAA"},
             {'name': "XYZ", 'phone': 987676554, 'city': "BBB"}]

def addContact(contact):
    phonebook.append(contact)

def searchContact(name):
    for contact in phonebook:
        if contact['name'] == name:
            return contact
    return None

def displayAll():
    for contact in phonebook:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, City: {contact['city']}")