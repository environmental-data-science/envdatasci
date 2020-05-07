# modules
import arcpy
from arcpy.sa import *
import os

# paths
ws = "C:/Users/ethan/OneDrive/Desktop/sb_slr"       #unique to wherever you store your files
gdb = ws + "/sb_slr.gdb"                            # our geodatabase
sr = "C:/Users/ethan/OneDrive/Desktop/sb_slr/dem_Carpinteria.tif"   #the first dem we are using, I think Ben's code accounts for the city name and switches the dem for us

# environment
arcpy.env.workspace = ws
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True  

# variables
cities = ["Carpinteria", "SantaBarbara", "Goleta"]
heights = range(1,11)                                   #sets the heights variable, from 1 meters to 10 meters
years_beg = [2010 + 10 * h for h in heights]            
years_end = [2020 + 10 * h for h in heights]            #sets the time periods that the rasters represent, this is a very arbitrary estimate: 1 meter per decade

# iterate over cities
for city in cities:
    dem = "dem_" + city + ".tif"                        #sets dem variable to select the right city

    # create slr_city mosaic to associate time with rasters
    slr_city = "slr_" + city
    gdb_slr_city = gdb + "/" + slr_city                                 #sets variables to use in the raster mosaic
    print("Creating slr_city mosaic: " + slr_city)
    arcpy.CreateMosaicDataset_management(gdb, slr_city, sr, 1, "1_BIT") #adds a mosaic of rasters to the sb_slr_geodatabase
    arcpy.AddField_management(gdb_slr_city, "YearBeg", "SHORT")         
    arcpy.AddField_management(gdb_slr_city, "YearEnd", "SHORT")         #adds the time element to the new rasters in the mosaic

    # iterate over slr heights
    for height in heights:
        slr_city_height = ws + "/slr_" + city + "_" + str(height) + "m.tif"     #defines the workplace and name for each raster
    
        # calculate slr_city_height raster
        if not arcpy.Exists(slr_city_height):                                   #checks to see if the raster exists
            print("  Creating slr_city_height raster: " + os.path.basename(slr_city_height))
            r = Con(Raster(dem) <= height, 1)                                                           #creates a new raster with the specified height
            r.save(slr_city_height)                                                                     #saves the raster
        arcpy.AddRastersToMosaicDataset_management(gdb_slr_city, "Raster Dataset", slr_city_height)     #adds the newly created raster to the mosaic
        
    # update YearBeg & YearEnd in slr_city mosaic
    print("  Updating YearBeg & YearEnd in slr_city mosaic: " + slr_city)
    with arcpy.da.UpdateCursor(gdb_slr_city, ["YearBeg", "YearEnd"]) as cursor:         # "with" statement to update the year of each raster
        for i, row in enumerate(cursor):
            row[0] = years_beg[i]
            row[1] = years_end[i]
            cursor.updateRow(row) 
