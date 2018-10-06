import os
import sys
import subprocess
import shutil

print("\n <===================USERS LOGGED ON THIS COMPUTER ==========================>")
script = "cat /etc/passwd | grep bash"
user = subprocess.call(script, shell=True)
print("\n")

print("\n <=================== Users Sessions ==========================>")
script = "last root"
session = subprocess.call(script, shell=True)
print("\n")

print("\n <=================== Userss Group==========================>")
script = "last group"
group = subprocess.call(script, shell=True)
print("\n")

print("\n <===================System Reboots==========================>")
script = "last reboot"
reboot = subprocess.call(script, shell=True)
print("\n")

print("\n <===================System Reboots Last 20 days==========================>")
script = "last -x -n 20"
twentyReboot = subprocess.call(script, shell=True)
print("\n")

print("\n <===================Find Log Enteries==========================>")
script = " cat /var/log/auth.log | grep gdm"
entries = subprocess.call(script, shell=True)
print("\n")

print("\n <===================GDM Local Manager==========================>")
script = " cat /var/log/auth.log | grep sshd"
GDM = subprocess.call(script, shell=True)
print("\n")

print("\n <===================Find the Log Enteries==========================>")
script = "cat /var/log/syslog | grep -i dhcpoffer"
Entries = subprocess.call(script, shell=True)
print("\n")

print("\n <===================Find the Log Enteries PreInit==========================>")
script = "cat /var/log/syslog | grep -i -A1 perinit"
Preinit = subprocess.call(script, shell=True)
print("\n")

writingLogs = open('evidences/userLogons.txt', "w+")
writingLogs.write("***************User Logon information ********************")
writingLogs.write("\n************USERS LOGGED ON THIS COMPUTER : ***********\n")
writingLogs.write(user)
writingLogs.write("\n********Users Sessions: ***********\n")
writingLogs.write(session)
writingLogs.write("\n********Users Group: ***********\n")
writingLogs.write(group)
writingLogs.write("\n********System Reboots: ***********\n")
writingLogs.write(reboot)
writingLogs.write("\n********=System Reboots Last 20 days: ***********\n")
writingLogs.write(twentyReboot)
writingLogs.write("\n********Log Entries ***********\n")
writingLogs.write(entries)
writingLogs.write("\n********GDM Local Manager **********\n")
writingLogs.write(GDM)
writingLogs.write("\n********Find Log Entries ***********\n")
writingLogs.write(Entries)
writingLogs.write("\n********Find Log Entries PerInt ***********\n")
writingLogs.write(Preinit)
writingLogs.write("\n*************End of Investigator information ******************\n")
writingLogs.close()
