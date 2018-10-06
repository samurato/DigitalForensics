#!/usr/bin/python
import os
import sys
import subprocess
filenames = ['/evidences/evidences', '/evidences/investigator.txt', ...]
with open(r'/evidences', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())