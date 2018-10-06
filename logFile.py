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
    print("\nCopying /var/log/auth.log to ", cwd + "/logfiles")
    shutil.copy('/var/log/auth.log', cwd + "/logfiles")
else:
    print("\n /var/log/auth.log doesn't exist")

print("<=======================Copying Mail Log==================>")
cwd = os.getcwd()
selectedFile = Path("/var/log/mail.log")
if selectedFile.is_file():
    print("\nCopying /var/log/mail.log to ", cwd + "/logfiles")
    shutil.copy('/var/log/mail.log', cwd + "/logfiles")
else:
    print("\n /var/log/mail.log doesn't exist")

print("<=======================mysql Log==================>")
cwd = os.getcwd()
selectedFile = Path("/var/log/mysql.log")
if selectedFile.is_file():
    print("\nCopying /var/log/mysql.log to ", cwd + "/logfiles")
    shutil.copy('/var/log/mysql.log', cwd + "/logfiles")
else:
    print("\n /var/log/mysql.log doesn't exist")
    
print("<=======================mysql Log==================>")
cwd = os.getcwd()
selectedFile = Path("/var/log/mysql.log")
if selectedFile.is_file():
    print("\nCopying /var/log/mysql.log to ", cwd + "/logfiles")
    shutil.copy('/var/log/mysql.log', cwd + "/logfiles")
else:
    print("\n /var/log/mysql.log doesn't exist")

print("<=======================line printer Log==================>")
cwd = os.getcwd()
selectedFile = Path("/var/log/lpr.log")
if selectedFile.is_file():
    print("\nCopying /var/log/lpr.log to ", cwd + "/logfiles")
    shutil.copy('/var/log/lpr.log', cwd + "/logfiles")
else:
    print("\n /var/log/lpr.log doesn't exist")
    
print("<=======================line printer Log==================>")
cwd = os.getcwd()
selectedFile = Path("/var/log/lpr.log")
if selectedFile.is_file():
    print("\nCopying /var/log/lpr.log to ", cwd + "/logfiles")
    shutil.copy('/var/log/lpr.log', cwd + "/logfiles")
else:
    print("\n /var/log/lpr.log doesn't exist")

print("<=======================app Log==================>")
cwd = os.getcwd()
selectedFile = Path("/var/log/syslog")
if selectedFile.is_file():
    print("\nCopying /var/log/syslog to ", cwd + "/logfiles")
    shutil.copy('/var/log/syslog', cwd + "/logfiles")
else:
    print("\n /var/log/syslog doesn't exist")