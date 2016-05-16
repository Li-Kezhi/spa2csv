#!/usr/bin/python
#coding=utf-8

'''
To transform Thermo Scientific .spa files to .csv
    By calling ne0dim's code (written in Ruby)
'''  

import os

rubyCodePosition = "E:\\SkyDrive\\Codes\\Ruby\\spa2csv\\spa2csv-0.1.rb"
filesPosition = "E:\\Downloads\\likzIR\\20160510_Mn75Fe25\\7_300_C\\"
prefix = "series00120"                            # Eg. series00120001.spa
numFiles = 19

################################

errorNum = 0
for index in xrange(numFiles):
    if(os.system("ruby " + rubyCodePosition + " " + filesPosition + prefix + "%03d" % index + ".spa") == 0):
        print("File No. %03d completed!\n" % index)
    else:
        errorNum += 1

print("")
print("============================")
print(str(errorNum) + " error(s) occured!")
print("============================\n")