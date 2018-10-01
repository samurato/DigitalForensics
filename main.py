import os
import sys

f =open('init_screen.txt', 'r')
file_contents =f.read()
print(file_contents)

userName  = input("Please Enter your full name: ")
userId = input("Please Enter your id/Badge no.: ")
userOrganisation = input("Please Enter the Organisation Name: ")
EvidenceId = input("Please Enter the Evidence Name and Tracking ID: ")
print("Needs Super User Access")
choice = ''
while choice !='6':
    print("Please choose one of the options to investigate below: ")
    print("1. Volatile Evidence ")
    print("2. Non Volatile")
    print("3. Log Files")
    print("4. User Logon informations and Sessions")
    print("5. Network Forensics")
    print("6. Exit/Log out")


    choice = input("\nOption: ")

    if choice == '1':
        print("\nHere's a bicycle. Have fun!\n")
    elif choice == '2':
        print("\nHere are some running shoes. Run fast!\n")
    elif choice == '3':
        print("\nHere's a map. Can you leave a trip plan for us?\n")
    elif choice == '4':
        print("\nHere's a map. Can you leave a trip plan for us?\n")
    elif choice == '5':
        print("\nHere's a map. Can you leave a trip plan for us?\n")
    elif choice == '6':
        print("\nThanks for playing. See you later.\n")
    else:
        print("\nI don't understand that choice, please try again.\n")

print("Exiting")


    