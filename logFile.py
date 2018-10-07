import os
import sys
import subprocess
import shutil
from pathlib import Path
from subprocess import call

#auth.log files
#print("Logfiles")
#f = open('/var/log/auth.log', 'r')
#file_contents=f.read()
#print(file_contents)
#print("\n")
cwd = os.getcwd()+ "/evidences" 
writeLog = open('evidences/logs.txt', "w+")
writeLog.write("\n************* Evidence logs ******************\n")
#Copy non-volatile log files
print("<=======================Copying Authentication Log==================>")
my_file = Path("/var/log/auth.log")
print(my_file)
if my_file.is_file():
    f =open('/var/log/auth.log', 'r')
    AuthLog = f.read()
    print(AuthLog)
    writeLog.write("\n******************* Authentication Log **************\n")
    writeLog.write(AuthLog)
else:
    print(my_file.is_file())
    print("\n /var/log/auth.log Doesn't Exist")
# selectedFile = Path("/var/log/auth.log")
# if selectedFile.is_file():
#     print("\nCopying /var/log/auth.log to ", cwd )
#     shutil.copy('/var/log/auth.log', cwd )
# else:
#     print("\n /var/log/auth.log doesn't exist")

print("<=======================Copying Mail Log==================>")
my_file = Path("/var/log/mail.log")
if my_file.is_file():
    f =open('/var/log/mail.log', 'r')
    mailLog = f.read()
    print(mainLog)
    writeLog.write("\n")
    writeLog.write("\n****************** Mail Log *********************\n")
    writeLog.write(mainLog)
else:
    print("\n /var/log/mail.log Doesn't Exist")
# selectedFile = Path("/var/log/mail.log")
# if selectedFile.is_file():
#     print("\nCopying /var/log/mail.log to ", cwd)
#     shutil.copy('/var/log/mail.log', cwd )
# else:
#     print("\n /var/log/mail.log doesn't exist")

print("<=======================mysql Log==================>")
my_file = Path("/var/log/mysql.log")
if my_file.is_file():
    f =open('/var/log/mysql.log', 'r')
    sqlLog = f.read()
    print(sqlLog)
    writeLog.write("\n")
    writeLog.write("\n***************** mysql Log ************************\n")
    writeLog.write(sqlLog)
else:
    print("\n /var/log/mysql.log Doesn't Exist")
# selectedFile = Path("/var/log/mysql.log")
# if selectedFile.is_file():
#     print("\nCopying /var/log/mysql.log to ", cwd )
#     shutil.copy('/var/log/mysql.log', cwd)
# else:
#     print("\n /var/log/mysql.log doesn't exist")

print("<=======================line printer Log==================>")
my_file = Path("/var/log/lpr.log")
if my_file.is_file():
    f =open('/var/log/lpr.log', 'r')
    lprLog = f.read()
    print(lprLog)
    writeLog.write("\n")
    writeLog.write("\n***************** line printer Log ************************\n")
    writeLog.write(lprLog)
else:
    print("\n /var/log/lpr.log Doesn't Exist")
# cwd = os.getcwd()
# selectedFile = Path("/var/log/lpr.log")
# if selectedFile.is_file():
#     print("\nCopying /var/log/lpr.log to ", cwd)
#     shutil.copy('/var/log/lpr.log', cwd )
# else:
#     print("\n /var/log/lpr.log doesn't exist")

print("<=======================app Log==================>")
my_file = Path("/var/log/syslog.log")
if my_file.is_file():
    f =open('/var/log/syslog', 'r')
    sysLog = f.read()
    print(sysLog)
    writeLog.write("\n")
    writeLog.write("\n***************** app Log ************************\n")
    writeLog.write(sysLog)
else:
    print("\n /var/log/syslog.log Doesn't Exist")
# selectedFile = Path("/var/log/syslog")
# if selectedFile.is_file():
#     print("\nCopying /var/log/syslog to ", cwd )
#     shutil.copy('/var/log/syslog', cwd )
# else:
#     print("\n /var/log/syslog doesn't exist")

##Spit logs into Text file
print("\n ")
writeLog.write("\n")
writeLog.close()