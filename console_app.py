from user_class import Courseclass
import os
import re


#sending email:
def send_email(eml):
    address = eml
    print(f"email sent to {address} successfully")




# user registering with course Python:
def edit_menu():
    print("press 1 for editing id")
    print("press 2 for editing email")
    print("press 3 for editing password")
    print("press 4 for editing name")
    print("press 5 for editing contact")

# The menu Displayed at the beginning
def menu_app():
    print(" + + + + + + + + Insight Workshop Academy + + + + + + + + + + + + + + + + + ")
    print("Press 1 for Registration")
    print("Press 2 for editing your record")
    print("Press 3 for Deleting your record")
    print("Press 4 for showing all the records")
    print('Press 5 for deleting the file as a whole')
    print(" + + + + + + + + + + + + + + + + + + + + + + + + + ")

items =[1,2,3,4]
user_choice = 'y'

while user_choice  == 'y':
    # creating the instance of the class from file user_class.py
    course = Courseclass("Python")
    # calling display menu for the app
    menu_app()

    # taking input from the user for multiple choices of operation
    user_input = input("Enter your choice of operation").strip()
    #conditional statements for the choices entered by the user
    #1 means registration
    if user_input == "1":
        user_id = input("Enter an id ")
        user_email = input("Enter your email")
        user_password = input("Enter your password")
        user_name = input("Enter your name")
        user_number = input("Enter your contact")
        course.all_user_info.append([user_id,user_email,user_password,user_name,
                                     user_number])
        data = course.data_log()
        send_email(user_email)
        # pushing the enter value to a file
        f = open('datafile.txt', 'a')
        for items in data:
            for strs in items:
                f.write(strs + " ")
            f.write("\n")
        f.close()


    #2 means editing the existing records
    elif user_input == "2":
        char = " "
        f = open("datafile.txt", 'r')
        previous_data = f.readlines()
        length = len(previous_data)
        new_data = []
        edit_choice = input("enter the id of record to be edited")
        edit_menu()
        for indval in previous_data:
            print(indval[0])
            if indval[0] == edit_choice:
                index_spaces = [u.start() for u in re.finditer(char, indval)]
                ed_choice = int(input("enter according to the menu"))
                while True:
                    # slice for id indval[0:index_spaces[0]]
                    if ed_choice == 1:
                            replace_string = indval[0:index_spaces[0]]
                            new_val = input("enter the new value")
                            indval = indval.replace(replace_string, new_val)


                    # slice for email indval[2:index_spaces[1]]
                    elif ed_choice == 2:
                            replace_string = indval[2:index_spaces[1]]
                            new_val = input("enter the new value")
                            indval = indval.replace(replace_string, new_val)


                    # slice for password indval[(index_spaces[1]+1): index_space[2])
                    elif ed_choice == 3:
                            replace_string = indval[(index_spaces[1] + 1):index_spaces[2]]
                            new_val = input("enter the new value")
                            indval = indval.replace(replace_string, new_val)


                    # slice for name indval[(index_spaces[2]+1): index_space[3])
                    elif ed_choice == 4:
                            replace_string = indval[(index_spaces[2] + 1): index_spaces[3]]
                            new_val = input("enter the new value")
                            indval = indval.replace(replace_string, new_val)


                    # slice for contact indval[(index_spaces[3]+1): index_space[4])
                    elif ed_choice == 5:
                            replace_string = indval[(index_spaces[3] + 1): index_spaces[4]]
                            new_val = input("enter the new value")
                            indval = indval.replace(replace_string, new_val)

                    break

                else:
                    print("value error")

            new_data.append(indval)

        f.close()
        # Writing the obtained changes in the file
        print(new_data)
        f = open("datafile.txt", 'w')
        f.writelines(new_data)
        f.close()


    #3 mean deleting the desired record
    elif user_input == "3":
        f = open("datafile.txt", 'r')
        og_data = f.readlines()
        temp1 =og_data
        del_choice = input("enter the id of the data you want to delete")
        for evralue in temp1:
            if evralue[0] == del_choice:
                 while evralue in temp1:
                     temp1.remove(evralue)
            else:
                print("there's no such record")
        f.close()
        f = open("datafile.txt", 'w')
        f.writelines(temp1)
        f.close()

    # reading all the records entered in the file
    elif user_input == "4":
        f = open("datafile.txt", 'r')
        data = f.readlines()
        for line in data:
            print(line)

    # flushing the file to restart everything
    elif user_input == "5":
        os.remove("datafile.txt")

    elif user_input not in items:
        print("Please insert the valid choice")

    #condition update for the while loop
    print('do you wish to continue')
    user_choice = input('enter y for continue and n for ending')
    user_choice = user_choice.lower()




