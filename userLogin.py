import os
import sys
import subprocess
import shutil

print("\n <===================USERS LOGGED ON THIS COMPUTER ==========================>")
script = "cat /etc/passwd | grep bash"
subprocess.call(script, shell=True)
print("\n")

print("\n <=================== Users Sessions ==========================>")
script = "last root"
subprocess.call(script, shell=True)
print("\n")

print("\n <=================== Userss Group==========================>")
script = "last group"
subprocess.call(script, shell=True)
print("\n")

print("\n <===================System Reboots==========================>")
script = "last reboot"
subprocess.call(script, shell=True)
print("\n")

print("\n <===================System Reboots Last 20 days==========================>")
script = "last -x -n 20"
subprocess.call(script, shell=True)
print("\n")

print("\n <===================Find Log Enteries==========================>")
script = " cat /var/log/auth.log | grep gdm"
subprocess.call(script, shell=True)
print("\n")

print("\n <===================GDM Local Manager==========================>")
script = " cat /var/log/auth.log | grep sshd"
subprocess.call(script, shell=True)
print("\n")

print("\n <===================Find the Log Enteries==========================>")
script = "cat /var/log/syslog | grep -i dhcpoffer"
subprocess.call(script, shell=True)
print("\n")

print("\n <===================Find the Log Enteries PreInit==========================>")
script = "cat /var/log/syslog | grep -i -A1 perinit"
subprocess.call(script, shell=True)
print("\n")