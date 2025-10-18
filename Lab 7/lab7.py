import arcpy

#assign bands
source = r"C:\DevSource\Hernandez-Online-GEOG676-Fall2025\Lab 7"
band1 = arcpy.sa.Raster(source + r"\band1.tif") #blue
band2 = arcpy.sa.Raster(source + r"\band2.tif") #green
band3 = arcpy.sa.Raster(source + r"\band3.tif") #red
band4 = arcpy.sa.Raster(source + r"\band4.tif") #NIR
combined = arcpy.CompositeBands_management([band1, band2, band3, band4], source + r"\output_combined.tif")

#Hillshade
azimuth = 315
altitude = 45
shadows = 'NO_SHADOWS'
z_factor = 1
hillshade = arcpy.sa.Hillshade(source + r"\dem.tif", azimuth, altitude, shadows, z_factor)
hillshade.save(source + r"\output_Hillshade.tif")

#Slope
output_measurement = "DEGREE"
z_factor = 1
slope = arcpy.sa.Slope(source + r"\dem.tif", output_measurement, z_factor)
slope.save(source + r"\output_Slope.tif")
print("success")

