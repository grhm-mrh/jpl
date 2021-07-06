# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Import numpy -- needed for array creation
# Import netCDF4 -- needed to read .nc4 file
# troubleshooting note: May want to import HDF5 library to read .nc4 file
import numpy as np
import netCDF4 as nc

import os

directory = r'C:/Users/maria/Downloads/'

# Create variable for the .nc4 SIF file to be oopened
for filename in os.listdir(directory):
        if filename.endswith(".nc4") :

            SIF_file = "C:/Users/maria/Desktop/JPL/Projects/OCO3_Files/" + filename
        
  #      else:
  #          continue
        


#Create variable of full SIF file dataset
            SIF_dataset = nc.Dataset(SIF_file)

# I used panoply to get an easier read of my variables

# Create variables of everything we want in the csv.
# In this case it's Daily_SIF_757nm, Latitude, and Longitude
# Note to self : Learn complete gridding process in python using Cartopy

            Daily_SIF_757nm = SIF_dataset['Daily_SIF_757nm']
            SoundingID = SIF_dataset['Metadata/SoundingId']
            Latitude = SIF_dataset['Latitude']
            Longitude = SIF_dataset['Longitude']


#Create an individual csv file for each variable of each SIF file!
#a = np.asarray(Daily_SIF_757nm)
#np.savetxt("SIF757_190806.csv", a, delimiter=",")


#import os

#directory = r'C:/Users/maria/Downloads/'
#for filename in os.listdir(directory):
  #  if filename.endswith(".nc4") :
        #print(os.path.join(directory, filename))
            a =  np.asarray(Longitude)
            b = np.asarray(Latitude)
            c = np.asarray(Daily_SIF_757nm)
     
            np.savetxt("Longitude_" +filename + ".csv", a, delimiter=",")
            np.savetxt("Latitude_" +filename + ".csv", b, delimiter=",")
            np.savetxt("SIF757nm_" +filename + ".csv",c, delimiter=",")

        else:
            continue
#SIF_file.close