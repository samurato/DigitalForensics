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
BootImage = f.read()
print(BootImage)
print("\n")

print("<====================CPU details=====================>")
f = open('/proc/cpuinfo', 'r')
cpu = f.read()
print(cpu)
print("\n")

print("<====================Memory Manage=====================>")
f = open('/proc/meminfo', 'r')
MemoryManage = f.read()
print(MemoryManage)
print("\n")

##Spit logs into Text file
print("\n ")
writeLog = open('evidences/nonVolatile.txt', "w+")
writeLog.write("\n************* Non Volatile Evidence logs ******************\n")
writeLog.write("\n******************* Boot Image **************\n")
writeLog.write(BootImage)
writeLog.write("\n")
writeLog.write("\n****************** CPU Details *********************\n")
writeLog.write(cpu)
writeLog.write("\n")
writeLog.write("\n***************** Memory Manage ************************\n")
writeLog.write(MemoryManage)
writeLog.write("\n")
writeLog.close()

# #ERROR COPYING
# print("COPYING ALL THE LOGS")
# cwd = os.getcwd()
# print("\n Copying /proc/cmdline to ", cwd + "/nonVolLogs")
# shutil.copy('/proc/cmdline', cwd + "/nonVolLogs")

# print("\n Copying /proc/cpuinfo to ", cwd + "/nonVolLogs")
# shutil.copy('/proc/cpuinfo', cwd + "/nonVolLogs")

# print("\n Copying /proc/meminfo to ", cwd + "/nonVolLogs")
# shutil.copy('/proc/meminfo', cwd + "/nonVolLogs")



