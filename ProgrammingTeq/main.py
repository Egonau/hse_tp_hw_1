class Contact:
    def __init__(self, full_name, phone_number, email):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        pass

    def __str__(self):
        return "{0}, {1}, {2}".format(self.full_name, self.phone_number, self.email)


def DBInterpretator(file_name):
    file = open(file_name, "r", encoding='utf-8')
    contacts_data = file.read().split("\n")
    contacts_list = []
    for i in contacts_data:
        a = i.split(",")
        contacts_list.append(Contact(a[0], a[1], a[2]))
    return contacts_list


def searchByPhoneNumber(phone_num, list):
    for i in list:
        if str(i.phone_number).__contains__(phone_num):
            print(i)


def searchByEmail(email, list):
    for i in list:
        if str(i.email).__contains__(email):
            print(i)


def searchByName(name, list):
    for i in list:
        if str(i.full_name).__contains__(name):
            print(i)


def editContact(list):
    print("Choose one contact")
    for i in range(0, len(list)):
        print(i, list[i])
    print(len(list), "Exit")
    num_of_selected = int(input())
    if num_of_selected == len(list):
        return
    print(list[num_of_selected])
    print("Choose variable: name(0), phone(1), email(2), exit(3)")
    variable = input()
    if int(variable) == 0:
        list[num_of_selected].full_name = input("New name:")
    elif int(variable) == 1:
        list[num_of_selected].phone_number = input("New phone:")
    elif int(variable) == 2:
        list[num_of_selected].email = input("New email:")
    else:
        return


def upload(list):
    f = open(file_name, 'w', encoding='utf-8')
    f.seek(0)
    for i in range(0, len(list) - 1):
        f.write(str(list[i]) + '\n')
    f.write(str(list[-1]))
    print("Done")


def showEmpty(phone, email, list):
    if phone and email:
        for i in list:
            if len(str(i.phone_number)) == 0 or len(str(i.email)) == 0:
                print(i)
    elif not phone and not email:
        for i in list:
            if len(str(i.phone_number)) == 0 and len(str(i.email)) == 0:
                print(i)
    elif phone and not email:
        for i in list:
            if len(str(i.phone_number)) == 0:
                print(i)
    else:
        for i in list:
            if len(str(i.email)) == 0:
                print(i)


print("Enter file name:")
file_name = input()
list_of_contacts = DBInterpretator(file_name)
print("Need help? Just enter: help")
while True:
    print("Enter your command:")
    i = input()
    if i.__contains__("+"):
        searchByPhoneNumber(i, list_of_contacts)
    elif i.__contains__("@"):
        searchByEmail(i, list_of_contacts)
    elif i == "show no phone and no email":
        showEmpty(False, False, list_of_contacts)
    elif i == "show no phone or no email":
        showEmpty(True, True, list_of_contacts)
    elif i == "show no phone":
        showEmpty(True, False, list_of_contacts)
    elif i == "show no email":
        showEmpty(False, True, list_of_contacts)
    elif i == "edit":
        editContact(list_of_contacts)
    elif i == "upload":
        upload(list_of_contacts)
    elif i == 'help':
        print("Commands: \n 1) Enter phone number with '+' to get all the references \n 2) Enter email with '@' to "
              "get all the references \n 3) Enter your name to get all the references \n 4) Enter 'edit' to edit "
              "contacts \n 5) Enter 'upload' to upload your changes to file \nOther commands: \n"
              " a) show no phone and no email \n"
              " b) show no phone or no email \n"
              " c) show no phone \n"
              " d) show no email \n")
    else:
        searchByName(i, list_of_contacts)
