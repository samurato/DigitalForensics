#!/usr/bin/python
import os
import sys
import subprocess
from Crypto.Hash import SHA256
# cwd = os.getcwd() + "/evidences"
# script = "cat " + cwd +"/investigator.txt /evidences/networkLog.txt /evidences/nonVolatile.txt"
# writeLog = open('evidences/final.txt', "w+")
# writeLog.write(script)
# writeLog.close()
# print(writeLog)
# subprocess.call (script, shell=True)
# filenames = ['/evidences/investigator.txt', '/evidences/networkLog.txt', '/evidences/nonVolatile.txt']
# with open('/evidence/final.txt', 'w+') as outfile:
#     for fname in filenames:
#         with open(fname) as infile:
#             outfile.write(infile.read())

investigatorA = open('evidences/investigator.txt' , 'r')
investigatorAa = open('evidences/final.txt')
investigatorB = open('evidences/logs.txt' , 'r')
investigatorC = open('nonVolatile.txt','r')
investigatorD = open('evidences/userLogons.txt' , 'r')
writeLog = open('evidences/final.txt', "w+")
writeLog.write(str(investigatorA.read()))
writeLog.write(str(investigatorAa.read()))
writeLog.write(str(investigatorB.read()))
writeLog.write(str(investigatorC.read()))
writeLog.write(str(investigatorD.read()))
writeLog.close()

field = open('evidences/final.txt','r')
hashdata = SHA256.new()
hashdata.update(field)
print (hashdata.hexdigest())