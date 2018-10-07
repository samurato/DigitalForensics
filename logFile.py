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

#Copy non-volatile log files
print("<=======================Copying Authentication Log==================>")
cwd = os.getcwd()+ "/evidences" 
selectedFile = Path("/var/log/auth.log")
if selectedFile.is_file():
    print("\nCopying /var/log/auth.log to ", cwd )
    shutil.copy('/var/log/auth.log', cwd )
else:
    print("\n /var/log/auth.log doesn't exist")

print("<=======================Copying Mail Log==================>")

selectedFile = Path("/var/log/mail.log")
if selectedFile.is_file():
    print("\nCopying /var/log/mail.log to ", cwd)
    shutil.copy('/var/log/mail.log', cwd )
else:
    print("\n /var/log/mail.log doesn't exist")

print("<=======================mysql Log==================>")
selectedFile = Path("/var/log/mysql.log")
if selectedFile.is_file():
    print("\nCopying /var/log/mysql.log to ", cwd )
    shutil.copy('/var/log/mysql.log', cwd)
else:
    print("\n /var/log/mysql.log doesn't exist")
    
print("<=======================mysql Log==================>")
selectedFile = Path("/var/log/mysql.log")
if selectedFile.is_file():
    print("\nCopying /var/log/mysql.log to ", cwd )
    shutil.copy('/var/log/mysql.log', cwd )
else:
    print("\n /var/log/mysql.log doesn't exist")

print("<=======================line printer Log==================>")
cwd = os.getcwd()
selectedFile = Path("/var/log/lpr.log")
if selectedFile.is_file():
    print("\nCopying /var/log/lpr.log to ", cwd)
    shutil.copy('/var/log/lpr.log', cwd )
else:
    print("\n /var/log/lpr.log doesn't exist")
    
print("<=======================line printer Log==================>")

selectedFile = Path("/var/log/lpr.log")
if selectedFile.is_file():
    print("\nCopying /var/log/lpr.log to ", cwd )
    shutil.copy('/var/log/lpr.log', cwd)
else:
    print("\n /var/log/lpr.log doesn't exist")

print("<=======================app Log==================>")

selectedFile = Path("/var/log/syslog")
if selectedFile.is_file():
    print("\nCopying /var/log/syslog to ", cwd )
    shutil.copy('/var/log/syslog', cwd )
else:
    print("\n /var/log/syslog doesn't exist")