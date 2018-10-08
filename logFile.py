import os
import sys
import subprocess
import shutil
from pathlib import Path
from subprocess import call

cwd = os.getcwd()+ "/evidences" 
writeLog = open('evidences/logs.txt', "w+")
writeLog.write("\n************* Evidence logs ******************\n")
print("<=======================Apache Log==================>")
my_file = Path("/var/log/apache2")
listOfFile= os.listdir(my_file)
for each_file in listOfFile: 
    if each_file == "access.log":
        f =open(each_file, 'r')
        AuthLog = f.read()
        writeLog.write("\n******************* Apache Log **************\n")
        writeLog.write(AuthLog)

for each_file in listOfFile: 
    if each_file == "ssl-access.log":
        f =open(each_file, 'r')
        AuthLog = f.read()
        writeLog.write("\n******************* SSL Apache Log **************\n")
        writeLog.write(AuthLog)

#Copy non-volatile log files
print("<=======================Copying Authentication Log==================>")
my_file = Path("/var/log/")
listOfFile= os.listdir(my_file)
for each_file in listOfFile: 
    if each_file == "auth.log":
        f =open(each_file, 'r')
        AuthLog = f.read()
        writeLog.write("\n******************* Authentication Log **************\n")
        writeLog.write(AuthLog)

print("<=======================Copying Mail Log==================>")
for each_file in listOfFile: 
    print(each_file)
    if each_file == "mail.log":
        f =open(each_file, 'r')
        mailLog = f.read()
        writeLog.write("\n")
        writeLog.write("\n****************** Mail Log *********************\n")
        writeLog.write(mailLog)

print("<=======================line printer Log==================>")
for each_file in listOfFile: 
    print(each_file)
    if each_file == "lrp":
        f =open(each_file, 'r')
        lprLog = f.read()
        writeLog.write("\n")  
        writeLog.write("\n***************** line printer Log ************************\n")
        writeLog.write(lprLog)

print("<=======================app Log==================>")
for each_file in listOfFile: 
    print(each_file)
    if each_file == "sys.log"):
        f =open(each_file, 'r')    
        sysLog = f.read()
        writeLog.write("\n")
        writeLog.write("\n***************** app Log ************************\n")
        writeLog.write(sysLog)

print("<=======================mysql Error Log==================>")
my_file = Path("/var/log/mysql")
listOfFile= os.listdir(my_file)
for each_file in listOfFile: 
    print(each_file)
    if each_file == "error.log":
        f =open(each_file, 'r')
        sqlLog = f.read()
        writeLog.write("\n")
        writeLog.write("\n***************** mysql Log ************************\n")
        writeLog.write(sqlLog)

print("\n ")
writeLog.write("\n")
writeLog.close()