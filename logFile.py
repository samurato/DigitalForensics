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
cwd = os.getcwd()
print("\n Copying /var/log/auth.log to ", cwd + "/logfiles")
shutil.copy('/var/log/auth.log', cwd + "/logfiles")

print("<=======================Copying Mail Log==================>")
cwd = os.getcwd()
selectedFile = Path("/var/log/mail.log")
if selectedFile.is_file():
    print("\n Copying /var/log/mail.log to ", cwd + "/logfiles")
    shutil.copy('/var/log/mail.log', cwd + "/logfiles")
else:
    print("\n /var/log/mail.log doesn't exist")