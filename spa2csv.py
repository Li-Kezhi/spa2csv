#!/usr/bin/python
#coding=utf-8

'''
To transform Thermo Scientific .spa files to .csv
    By calling ne0dim's code (written in Ruby)
'''  

import os

rubyCodePosition = "E:\\SkyDrive\\Codes\\Ruby\\spa2csv\\spa2csv-0.1.rb"
filesPosition = "E:\\Downloads\\likzIR\\20160509_Mn10Fe0\\1_NH3_ads\\"
prefix = "series00120"                            # Eg. series00120001.spa

################################

numFiles = 0
while True:
    try:
        if(os.system("ruby " + rubyCodePosition + " " + filesPosition + prefix + "%03d" % numFiles + ".spa") == 0):
            print("File No. %03d completed!\n" % numFiles)
        else:
            raise IOError
        numFiles += 1
    except IOError:
        break

print("")
print("============================")
print(str(numFiles) + " file(s) successfully converted!")
print("============================\n")
