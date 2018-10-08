import os
import sys
import subprocess
import shutil
from pathlib import Path
from subprocess import call

cwd = os.getcwd()+ "/evidences" 
writeLog = open('evidences/logs.txt', "w+")
writeLog.write("\n************* Evidence logs ******************\n")
#Copy non-volatile log files
print("<=======================Copying Authentication Log==================>")
my_file = Path("/var/log/")
listOfFile= os.listdir(my_file)
for each_file in listOfFile: 
    print(each_file)
    if each_file == "auth.log":
        f =open(each_file, 'r')
        AuthLog = f.read()
        print(AuthLog)
        writeLog.write("\n******************* Authentication Log **************\n")
        writeLog.write(AuthLog)
    else:
        print(my_file.is_file())
        print("\n /var/log/auth.log Doesn't Exist")

print("<=======================Copying Mail Log==================>")
for each_file in listOfFile: 
    print(each_file)
    if each_file.startswith("mail"):
        f =open(each_file, 'r')
        mailLog = f.read()
        print(mailLog)
        writeLog.write("\n")
        writeLog.write("\n****************** Mail Log *********************\n")
        writeLog.write(mailLog)
    else:
        print("\n /var/log/mail Doesn't Exist")

print("<=======================mysql Log==================>")
for each_file in listOfFile: 
    print(each_file)
    if each_file.startswith("mysql"):
        f =open(each_file, 'r')
        sqlLog = f.read()
        print(sqlLog)
        writeLog.write("\n")
        writeLog.write("\n***************** mysql Log ************************\n")
        writeLog.write(sqlLog)
    else:
        print("\n /var/log/mysql Doesn't Exist")

print("<=======================line printer Log==================>")
for each_file in listOfFile: 
    print(each_file)
    if each_file.startswith("lpr"):
        f =open(each_file, 'r')
        lprLog = f.read()
        print(lprLog)
        writeLog.write("\n")
        writeLog.write("\n***************** line printer Log ************************\n")
        writeLog.write(lprLog)
    else:
        print("\n /var/log/lpr.log Doesn't Exist")

print("<=======================app Log==================>")
for each_file in listOfFile: 
    print(each_file)
    if each_file.startswith("sysLog"):
        f =open(each_file, 'r')    
        sysLog = f.read()
        print(sysLog)
        writeLog.write("\n")
        writeLog.write("\n***************** app Log ************************\n")
        writeLog.write(sysLog)
    else:
        print("\n /var/log/syslog.log Doesn't Exist")
print("\n ")
writeLog.write("\n")
writeLog.close()