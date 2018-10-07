#!/usr/bin/python
import os
import sys
import subprocess
print("<=======================Network Forensics==================>")
script = "cat /var/log/syslog | grep -i dhcpoffer"
Entries = subprocess.call(script, shell=True)
script = "cat /var/log/syslog"
print(Entries)

#TODO: Whois data

