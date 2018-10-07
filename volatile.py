import os
import sys
import subprocess
import shutil
from pathlib import Path
from subprocess import call

#Run Date
print("\n")
print("<=======================DATE==================>")
call(["date"])
print("\n")

#IP configurations
print("<=======================IP Configuration==================>")
call(["ifconfig"])
print("\n")

#Network Statistics
print("<=======================Netstat==================>")
call(["netstat"])
print("\n")

#Mount Points
print("<====================Mount Points DF=====================>")
call(["df"])
print("\n")

#Disk Usage
print("<====================Disk Usage DF=====================>")
call(["du"])
print("\n")

#Last Logged in
print("<=======================Last Loggedin==================>")
call(["ps", '-w'])
print("\n")

#running processes
print("<=======================Local Processes==================>")
call(["ps", '-af'])
print("\n")

#running processes
print("<=======================System Processes==================>")
call(["ps", '-Af'])
print("\n")

#Show startup files
print("<=======================Startup Files==================>")
call(["ls", '/etc/init.d'])
print("\n")

#Currently running Services
print ("<==================Current running Services==============>")
call(["service", '--status-all'])
print("\n")

#Copy Essential details
print("<=======================Copying Forensic Interest Files==================>")
cwd = os.getcwd() + "/evidences" 
print("\n Copying /etc/passwd to ", cwd)
shutil.copy('/etc/passwd', cwd)

print("\n Copying /etc/shadow  to ", cwd )
#shutil.copy('/etc/shadow', cwd)

print("\n Copying /etc/init.d to ", cwd )
my_file = Path(" /etc/init.d to")
if my_file.is_file():
    shutil.copy(' /etc/init.d to', cwd )
else:
    print("\n /etc/init.d Doesn't Exist")

print("\n Copying /var/www to ", cwd )
my_file = Path("/var/www")
if my_file.is_file():
    shutil.copy('/var/www ', cwd )
else:
    print("\n /var/www Doesn't Exist")

print("\n Copying /var/log to ", cwd)
src = "/var/log"
dst = cwd
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
print("\n All Logs copied!!")

print("\n Copying /var/lib/mysql  to ", cwd)
my_file = Path("/var/lib/mysql")
if my_file.is_file():
    shutil.copy('/var/lib/mysql', cwd)
else:
    print("\n /var/lib/mysql Doesn't Exist")

print("\n SUCCESS CHECK!!!! \n passwd, shadow, init.d, www, log, mysql in  \n ", cwd)

