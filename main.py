import os
import sys
import subprocess
f =open('init_screen.txt', 'r')
file_contents =f.read()
print(file_contents)

userName  = input("Please Enter your full name: ")
userId = input("Please Enter your id/Badge no.: ")
userOrganisation = input("Please Enter the Organisation Name: ")
EvidenceId = input("Please Enter the Evidence Name and Tracking ID: ")
#TODO Hashing
print("\nNeeds Super User Access to Run this tool\n")

investigate = open('evidences/final.txt', "w+")
investigate.write("***************First Responder Information ********************")
investigate.write("\nInvestigator Name: "+userName)
investigate.write("\nInvestigator ID: "+userId)
investigate.write("\nInvestigator Organisation: "+userOrganisation)
investigate.write("\nEvidence Name or ID:  "+EvidenceId)
investigate.write("\n*************End of Investigator information ******************\n")
investigate.close()

su = input("\n Enter Super user now Y/N : ")
if su == "y" or "Y":
    returncode = subprocess.call(["/usr/bin/sudo", "/usr/bin/id"])
choice = ''
while choice !='6':
    print("Please choose one of the options to investigate below: ")
    print("1. Volatile Evidence ")
    print("2. Non Volatile")
    print("3. Log Files")
    print("4. User Logon informations and Sessions")
    print("5. Network Forensics")
    print("6. Compile and Exit/Log out")


    choice = input("\nOption: ")

    if choice == '1':
        import volatile
        print("\nVolatile Evidence Captured\n")
    elif choice == '2':
        import nonVolatile
        print("\n Non Volatole Evidence Captured\n")
    elif choice == '3':
        import logFile
        print("\n All Log files captured \n")
    elif choice == '4':
        import userLogin
        print("\n User Logons captured\n")
    elif choice == '5':
        import network
        print("\n Ran Network Forensics\n")
    elif choice == '6':
        import evidencelog
        print("\n Compiling Evidence to one file.\n")
    else:
        print("\nI don't understand that choice, please try again.\n")

print("Exiting")


    
