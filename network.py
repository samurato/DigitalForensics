#!/usr/bin/python
import os
import sys
import subprocess
print("<=======================Network Forensics==================>")
#w = whois.whois('ifconfig.me/ip')
#print(w)
some="$(curl -s ifconfig.me/ip)"
currentIp = "ifconfig.me/ip"
userIp=subprocess.call(["curl", currentIp])
# sendIp = "$("+ str(userIp) +")"
# subprocess.call (["whois ", sendIp])
print("\n ")
writeLog = open('evidences/final.txt', "w+")
writeLog.write("\n************* Network Evidence logs ******************\n")
writeLog.write(str(userIp))
#TODO: Whois data
writeLog.close()
