#!/usr/bin/python
#coding=utf-8

'''
To transform Thermo Scientific .spa files to .csv
    By calling ne0dim's code (modified in Python)
'''

import os

pythonCodePosition = "spa2csv.py"

################################

numFiles = 0

root = os.getcwd()
filenames = os.listdir(root)

for filename in filenames:
    if filename.endswith('.spa'):
        os.system('python ' + pythonCodePosition + ' ' + filename)
        print("File No. %04d completed!\n" % (numFiles + 1))
        numFiles += 1

print("")
print("============================")
print(str(numFiles) + " file(s) successfully converted!")
print("============================\n")
