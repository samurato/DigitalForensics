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
#Copy non-volatile log files
print("<=======================Copying Authentication Log==================>")
f =open('/var/log/auth.log', 'r')
AuthLog = f.read()
print(AuthLog)
# selectedFile = Path("/var/log/auth.log")
# if selectedFile.is_file():
#     print("\nCopying /var/log/auth.log to ", cwd )
#     shutil.copy('/var/log/auth.log', cwd )
# else:
#     print("\n /var/log/auth.log doesn't exist")

print("<=======================Copying Mail Log==================>")

f =open('/var/log/mail.log', 'r')
mailLog = f.read()
print(mainLog)
# selectedFile = Path("/var/log/mail.log")
# if selectedFile.is_file():
#     print("\nCopying /var/log/mail.log to ", cwd)
#     shutil.copy('/var/log/mail.log', cwd )
# else:
#     print("\n /var/log/mail.log doesn't exist")

print("<=======================mysql Log==================>")
f =open('/var/log/mysql.log', 'r')
sqlLog = f.read()
print(sqlLog)

# selectedFile = Path("/var/log/mysql.log")
# if selectedFile.is_file():
#     print("\nCopying /var/log/mysql.log to ", cwd )
#     shutil.copy('/var/log/mysql.log', cwd)
# else:
#     print("\n /var/log/mysql.log doesn't exist")

print("<=======================line printer Log==================>")
f =open('/var/log/lpr.log', 'r')
lprLog = f.read()
print(lprLog)
# cwd = os.getcwd()
# selectedFile = Path("/var/log/lpr.log")
# if selectedFile.is_file():
#     print("\nCopying /var/log/lpr.log to ", cwd)
#     shutil.copy('/var/log/lpr.log', cwd )
# else:
#     print("\n /var/log/lpr.log doesn't exist")

print("<=======================app Log==================>")

f =open('/var/log/syslog', 'r')
sysLog = f.read()
print(sysLog)
# selectedFile = Path("/var/log/syslog")
# if selectedFile.is_file():
#     print("\nCopying /var/log/syslog to ", cwd )
#     shutil.copy('/var/log/syslog', cwd )
# else:
#     print("\n /var/log/syslog doesn't exist")

##Spit logs into Text file
print("\n ")
writeLog = open('evidences/logs.txt', "w+")
writeLog.write("\n************* Evidence logs ******************\n")
writeLog.write("\n******************* Authentication Log **************\n")
writeLog.write(AuthLog)
writeLog.write("\n")
writeLog.write("\n****************** Mail Log *********************\n")
writeLog.write(mainLog)
writeLog.write("\n")
writeLog.write("\n***************** mysql Log ************************\n")
writeLog.write(sqlLog)
writeLog.write("\n")
writeLog.write("\n***************** line printer Log ************************\n")
writeLog.write(lprLog)
writeLog.write("\n")
writeLog.write("\n***************** app Log ************************\n")
writeLog.write(sysLog)
writeLog.write("\n")
writeLog.close()