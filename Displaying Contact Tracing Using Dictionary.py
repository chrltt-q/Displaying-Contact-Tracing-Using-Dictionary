print("******** PROGRAMMED BY ********")
print("****** Charlotte Quezada ******")
print("********** BSCOE 2-2 **********")
print("*** Sir Danilo Madrigalejos ***\n")


def menu():
    print("\n***~~~*~*~~*~*~*~*~*~~*~*~*******~*~*~~*~*~*~*~*~~*~*~~~***")
    print("                           Menu                            ")
    print("***~~~*~*~~*~*~*~*~*~~*~*~*******~*~*~~*~*~*~*~*~~*~*~~~***")
    print("\n||  1 Add an item                                  ||"
          "\n||  2 Search an item                               ||"
          "\n||  3 Exit                                         ||\n")


def get_input():
    global key_name
    global age
    global get_age
    global address
    global get_address
    global phone_num
    global get_phone_num
    global email_add
    global get_email_add
    global response_vax
    global get_response_vax
    global response_expo
    global get_response_expo
    global response_contact
    global get_response_contact
    global response_tested
    global get_response_tested

    key_name = input("Please enter your Full Name: ")
    age = "Age"
    get_age = int(input("Please enter your Age: "))
    address = "Address"
    get_address = input("Please enter your Address: ")
    phone_num = "Phone number"
    get_phone_num = int(input("Please enter your Phone Number: "))
    email_add = "Email Address"
    get_email_add = input("Please enter your Email Address: ")
    response_vax = "Have you been vaccinated for COVID-19?"
    get_response_vax = input("Have you been vaccinated for COVID-19? (yes or no): ")
    response_expo = "Have you had exposure to a probable or confirmed case in the last 14 days?"
    get_response_expo = input(
        "Have you had exposure to a probable or confirmed case in the last 14 days? (yes or no): ")
    response_contact = "Have you had in contact with somebody with symptoms?"
    get_response_contact = input(
        "Have you had in contact with somebody with body pains, headache, sore throat, fever,\n"
        "diarrhea, cough, colds, shortness of breath, loss of taste, or loss of smell in the\n"
        "past 7 days? (yes or no): ")
    response_tested = "Have you been tested for Covid-19 in the last 14 days?"
    get_response_tested = input("Have you been tested for Covid-19 in the last 14 days? (yes or no): ")


def search_item():
    for name_key, name_info in main_dict.items():
        print("\nName:", name_key)

        for key in name_info:
            print(key + ":", name_info[key])


def exit_prog():
    print("\nThank you for using this program intended for contact tracing. Goodbye!")
    exit()


while True:
    print("\n* Welcome, this program is intended for contact tracing *\n")
    menu()
    option = int(input("Enter the option you want to choose from the menu (1-3): "))
    if option == 1:
        print("\n               * * * Add an item * * *                   \n")
        get_input()
        print("Item added successfully.")
    elif option == 2:
        while True:
            print("\n              * * * Search an item * * *                  \n")
            search_name = input("Please enter the Full Name you want to search: ")
            main_dict = {key_name: {age: get_age, address: get_address, phone_num: get_phone_num, email_add: get_email_add,
                                    response_vax: get_response_vax, response_expo: get_response_expo,
                                    response_contact: get_response_contact, response_tested: get_response_tested}
                         }
            if search_name in main_dict:
                search_item()
                break
            else:
                print("Invalid name. Please enter a valid full name you have added previously.")
                continue
    elif option == 3:
        print("\n             * * * Exit the Program * * *                 \n")
        exit_prog()