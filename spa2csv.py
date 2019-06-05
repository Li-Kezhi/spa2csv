#!/usr/bin/python

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.


#This is a simple app to convert Thermo SPA file into plain text format (csv)
#To use this app just provide it with SPA file as an argument
#Like so: ruby spa2csv spectrum.spa --> CHANGED!
#It will create text file containing your data in text format
#named like this: spectrum.spa.csv.
#Hope this app will be of some usage
#Written by ne0dim
#While using the code please keep the comments and the author's name


##########
#This file is tranformed into Python by Kezhi LI

#To use this app just provide it with SPA file as an argument
#Like so: python spa2csv spectrum.spa
#It will create text file containing your data in text format
#named like this: spectrum.spa.csv.


import struct
# import numpy as np
from sys import argv

#Opening datafile in binary mode provided as 1 argument
if not len(argv) == 1:
    filename = argv[1]
else:
    raise Exception('No file provided!')

# filename = 'series00020000.spa'

spectrum_spa_binary_string = open(filename, "rb").read()

#Searching for spectrum offset which is stored as 16bit
#unsigned number marked by x00x00x00x03x00
spectrum_offsets = spectrum_spa_binary_string.split(b'\x00\x00\x00\x03\x00')[1]

#Saving spectrum offset
spectrum_offset = struct.unpack('H', spectrum_offsets[0:2])[0]

#Spectrum end offset is stored after x00x00
spectrum_end_offset = struct.unpack('H', spectrum_offsets[4:6])[0]

#Searching for spectrum range and unpacking it as float 32bit numbers.
#Couldn't find its offset anywhere in the file, so we search for it by pattern
#x00x00x00x03x00x00x00. Not sure that it will work for every spectra but with
#mine it works OK
spectrum_from_values = spectrum_spa_binary_string.split(b"\x00\x00\x00\x03\x00\x00\x00")[1]

#Storing from and values for spectrum to get X axis coordinates
spectrum_from_value = struct.unpack('f', spectrum_from_values[12:16])[0]
spectrum_to_value = struct.unpack('f', spectrum_from_values[16:20])[0]

#Unpacking spectrum using the offset found earlier.
#The spectrum is just 32bit floats
spectrum = spectrum_spa_binary_string[spectrum_offset:(spectrum_offset+spectrum_end_offset)]

spectrum_float = []
while len(spectrum) > 0:
    spectrum_float.append(struct.unpack('f', spectrum[0:4])[0])
    spectrum = spectrum[4:]
# spectrum_float = np.array(spectrum_float)

#Calculating X axis step. Maybe it's also somewhere in the file, just couldn't find it right away
spectrum_step = (spectrum_from_value - spectrum_to_value)/(len(spectrum_float)-1)

#Filling up the xaxis array
spectrum_xaxis = []
for i in range(len(spectrum_float)):
    spectrum_xaxis.append(spectrum_from_value - spectrum_step*i)
# spectrum_xaxis = np.array(spectrum_xaxis)

#Prepare the final array
# spectrum_full_array = np.vstack((spectrum_xaxis, spectrum_float)).T

#Save the results
# np.savetxt(filename + '.csv', spectrum_full_array, delimiter=',')
f = open(filename + '.csv', 'w')
for i in range(len(spectrum_xaxis)):
    f.write(str(spectrum_xaxis[i]) + ',' + str(spectrum_float[i]) + '\n')
f.close()

print('Successfully transformed!')