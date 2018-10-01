import os
import sys
import subprocess
import shutil
from pathlib import Path
from subprocess import call


#Run cmdline boot image
print("\n")
print("<====================Command Line Boot Image=====================>")
f =open('/proc/cmdline', 'r')
file_contents =f.read()
print(file_contents)
print("\n")

print("<====================CPU details=====================>")
f = open('/proc/cpuinfo', 'r')
file_contents = f.read()
print(file_contents)
print("\n")

print("<====================Memory Manage=====================>")
f = open('/proc/meminfo', 'r')
file_contents = f.read()
print(file_contents)
print("\n")

#ERROR COPYING
print("COPYING ALL THE LOGS")
cwd = os.getcwd()
print("\n Copying /proc/cmdline to ", cwd + "/nonVolLogs")
shutil.copy('/proc/cmdline', cwd + "/nonVolLogs")

print("\n Copying /proc/cpuinfo to ", cwd + "/nonVolLogs")
shutil.copy('/proc/cpuinfo', cwd + "/nonVolLogs")

print("\n Copying /proc/meminfo to ", cwd + "/nonVolLogs")
shutil.copy('/proc/meminfo', cwd + "/nonVolLogs")



