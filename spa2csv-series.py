#!/usr/bin/python
#coding=utf-8

'''
To transform Thermo Scientific .spa files to .csv
    By calling ne0dim's code (modified in Python)
'''

import os

pythonCodePosition = "spa2csv.py"
filesPosition = "./"
prefix = "series0002"                            # Eg. series00120000.spa

################################

numFiles = 0
while True:
    try:
        if(os.system("python " + pythonCodePosition + " " + filesPosition + prefix + "%04d" % numFiles + ".spa") == 0):
            print("File No. %04d completed!\n" % numFiles)
        else:
            raise IOError
        numFiles += 1
    except IOError:
        break

print("")
print("============================")
print(str(numFiles) + " file(s) successfully converted!")
print("============================\n")
