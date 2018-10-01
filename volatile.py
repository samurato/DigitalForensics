import os
import sys
import subprocess
from subprocess import call

#Run Date
print("<=======================DATE==================>")
call(["date"])

#IP configurations
print("<=======================IP Configuration==================>")
call(["ifconfig"])

#Network Statistics
print("<=======================Netstat==================>")
call(["netstat"])
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


