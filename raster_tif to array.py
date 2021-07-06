# -*- coding: utf-8 -*-
"""

@author: maria
"""

from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt

#import os

#directory = r'C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2019_12/ET/'

# for filename in os.listdir(directory):
# while filename.endswith(".tif") :

# ECOSTRESS ET

# Open .tif file raster dataset
ETds = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2019_10/ET/Reprojected05ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2019278212715_aid0001.tif")
ETds2 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/ET/Reprojected06ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020158200712_aid0001 (1).tif")
ETds3 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/ET/Reprojected07ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020159191919_aid0001 (1).tif")
ETds4 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/ET/Reprojected08ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020160183141_aid0001 (1).tif")
ETds5 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/ET/Reprojected10ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020162015111_aid0001 (1).tif")
ETds6 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/ET/Reprojected14ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020166001632_aid0001 (1).tif")
ETds7 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/ET/Reprojected14ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020166001724_aid0001 (1).tif")
ETds8 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/ET/Reprojected17ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020169224145_aid0001 (1).tif")
ETds9 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/ET/Reprojected17ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020169224237_aid0001 (1).tif")
ETds10 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/ET/Reprojected17ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020169224329_aid0001 (1).tif")
ETds11 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/ET/Reprojected18ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020170152315_aid0001 (1).tif")
ETds12 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/ET/Reprojected19ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020171143523_aid0001 (1).tif")
ETds13 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/ET/Reprojected21ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020173143637_aid0001 (1).tif")
ETds14 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/ET/Reprojected21ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020173210829_aid0001 (1).tif")
ETds15= gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/ET/Reprojected25ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020177130156_aid0001 (1).tif")
ETds16 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/ET/Reprojected25ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020177193205_aid0001 (1).tif")
ETds17 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/ET/Reprojected25ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020177193349_aid0001 (1).tif")


ETds18 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_01/ET/Clipped (mask)Reprojected29ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020029224753_aid0001 (1).tif")
ETds19 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_01/ET/Clipped (mask)Reprojected30ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020030220024_aid0001 (1).tif")
ETds20 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_02/ET/Reprojected13ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020044172119_aid0001 (1).tif")
ETds21 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_03/ET/ReprojectedReprojected29ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020089223739_aid0001.tif")
ETds22 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_03/ET/ReprojectedReprojected31ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020091223937_aid0001 (1).tif")
ETds23 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_04/ET/Reprojected01ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020092215211_aid0001 (1).tif")
ETds24 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_04/ET/Reprojected15ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020106235114_aid0001 (1).tif")
ETds25 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_04/ET/Reprojected16ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020107163209_aid0001 (1).tif")
ETds26 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_04/ET/Reprojected23ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020114204412_aid0001 (1).tif")
ETds27 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_04/ET/Reprojected23ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020114204504_aid0001 (1).tif")
ETds28 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_05/ET/Reprojected01ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020122173543_aid0001 (1).tif")
ETds29 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_05/ET/Reprojected01ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020122173635_aid0001 (1).tif")
ETds30 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_05/ET/Reprojected26ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020147005046_aid0001 (1).tif")
ETds31 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_05/ET/Reprojected27ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020148000255_aid0001 (1).tif")
ETds32 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_05/ET/Reprojected30ECO3ETPTJPL.001_EVAPOTRANSPIRATION_PT_JPL_ETdaily_doy2020151222828_aid0001 (1).tif")



#ETfile = 'C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2019_08/ET/' + filename
# ETds = gdal.Open(ETfile)
# geotransform ET
geotET = ETds.GetGeoTransform()

# projection ET
projET = ETds.GetProjection()

# band, should be 1
bandET = ETds.GetRasterBand(1)
arrayET = bandET.ReadAsArray()



bandET2 = ETds2.GetRasterBand(1)
arrayET2 = bandET2.ReadAsArray()
bandET3 = ETds3.GetRasterBand(1)
arrayET3 = bandET3.ReadAsArray()
bandET4 = ETds4.GetRasterBand(1)
arrayET4 = bandET4.ReadAsArray()
bandET5 = ETds5.GetRasterBand(1)
arrayET5 = bandET5.ReadAsArray()
bandET6 = ETds6.GetRasterBand(1)
arrayET6 = bandET6.ReadAsArray()
bandET7 = ETds7.GetRasterBand(1)
arrayET7 = bandET7.ReadAsArray()
bandET8 = ETds8.GetRasterBand(1)
arrayET8 = bandET8.ReadAsArray()
bandET9 = ETds9.GetRasterBand(1)
arrayET9 = bandET9.ReadAsArray()
bandET10 = ETds10.GetRasterBand(1)
arrayET10 = bandET10.ReadAsArray()
bandET11 = ETds11.GetRasterBand(1)
arrayET11 = bandET11.ReadAsArray()
bandET12 = ETds12.GetRasterBand(1)
arrayET12 = bandET12.ReadAsArray()
bandET13 = ETds13.GetRasterBand(1)
arrayET13 = bandET13.ReadAsArray()
bandET14 = ETds14.GetRasterBand(1)
arrayET14 = bandET14.ReadAsArray()
bandET15 = ETds15.GetRasterBand(1)
arrayET15 = bandET15.ReadAsArray()
bandET16 = ETds16.GetRasterBand(1)
arrayET16 = bandET16.ReadAsArray()
bandET17 = ETds17.GetRasterBand(1)
arrayET17 = bandET17.ReadAsArray()



bandET18 = ETds18.GetRasterBand(1)
arrayET18 = bandET18.ReadAsArray()
bandET19 = ETds19.GetRasterBand(1)
arrayET19 = bandET19.ReadAsArray()
bandET20 = ETds20.GetRasterBand(1)
arrayET20 = bandET20.ReadAsArray()
bandET21 = ETds21.GetRasterBand(1)
arrayET21 = bandET21.ReadAsArray()
bandET22 = ETds22.GetRasterBand(1)
arrayET22 = bandET22.ReadAsArray()
bandET23 = ETds23.GetRasterBand(1)
arrayET23 = bandET23.ReadAsArray()
bandET24 = ETds24.GetRasterBand(1)
arrayET24 = bandET24.ReadAsArray()
bandET25 = ETds25.GetRasterBand(1)
arrayET25 = bandET25.ReadAsArray()

bandET26 = ETds26.GetRasterBand(1)
arrayET26 = bandET26.ReadAsArray()
bandET27 = ETds27.GetRasterBand(1)
arrayET27 = bandET27.ReadAsArray()
bandET28 = ETds28.GetRasterBand(1)
arrayET28 = bandET28.ReadAsArray()
bandET29 = ETds29.GetRasterBand(1)
arrayET29 = bandET29.ReadAsArray()
bandET30 = ETds30.GetRasterBand(1)
arrayET30 = bandET30.ReadAsArray()
bandET31 = ETds31.GetRasterBand(1)
arrayET31 = bandET31.ReadAsArray()
bandET32 = ETds32.GetRasterBand(1)
arrayET32 = bandET32.ReadAsArray()


#SIF arrays



# -9e12 is nodata val
plt.figure
plt.imshow(arrayET)
plt.title('ET 06/25/2020 - 3')

SaveETArray = np.asarray(arrayET)
np.savetxt("ET_CA_05_30_2020" +".csv", SaveETArray, delimiter=",")
# else:
#     continue
######---------------------SIF-----------------########

SIFds = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_05/SIF/Clipped (mask)SIF757nm_oco3_LtSIF_200530_B10206r_200709051924s.nc4.tif")
SIFds2 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/SIF/Clipped (mask)SIF757nm_oco3_LtSIF_200606_B10206r_200709055431s.nc4.tif")
SIFds3 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/SIF/Clipped (mask)SIF757nm_oco3_LtSIF_200607_B10206r_200709055431s.nc4.tif")
SIFds4 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/SIF/Clipped (mask)SIF757nm_oco3_LtSIF_200608_B10206r_200709055433s.nc4.tif")
SIFds5 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/SIF/Clipped (mask)SIF757nm_oco3_LtSIF_200610_B10206r_200713163602s.nc4.tif")
SIFds6 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/SIF/Clipped (mask)SIF757nm_oco3_LtSIF_200614_B10206r_200713163603s.nc4.tif")
SIFds7 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/SIF/Clipped (mask)SIF757nm_oco3_LtSIF_200614_B10206r_200713163603s.nc4.tif")
SIFds8 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/SIF/Clipped (mask)SIF757nm_oco3_LtSIF_200617_B10206r_200713163608s.nc4.tif")
SIFds9 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/SIF/Clipped (mask)SIF757nm_oco3_LtSIF_200617_B10206r_200713163608s.nc4.tif")
SIFds10 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/SIF/Clipped (mask)SIF757nm_oco3_LtSIF_200617_B10206r_200713163608s.nc4.tif")
SIFds11 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/SIF/Clipped (mask)SIF757nm_oco3_LtSIF_200618_B10206r_200713163608s.nc4.tif")
SIFds12 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/SIF/Clipped (mask)SIF757nm_oco3_LtSIF_200619_B10206r_200713163608s.nc4.tif")
SIFds13 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/SIF/Clipped (mask)SIF757nm_oco3_LtSIF_200621_B10206r_200713163608s.nc4.tif")
SIFds14 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/SIF/Clipped (mask)SIF757nm_oco3_LtSIF_200621_B10206r_200713163608s.nc4.tif")
SIFds15 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/SIF/Clipped (mask)SIF757nm_oco3_LtSIF_200625_B10206r_200713163614s.nc4.tif")
SIFds16 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/SIF/Clipped (mask)SIF757nm_oco3_LtSIF_200625_B10206r_200713163614s.nc4.tif")
SIFds17 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_06/SIF/Clipped (mask)SIF757nm_oco3_LtSIF_200625_B10206r_200713163614s.nc4.tif")



SIFds18 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_01/SIF/Clipped (mask)RasterizedSIF757nm_oco3_LtSIF_200129_B10206r_200709054211s.nc4.tif")
SIFds19 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_01/SIF/Clipped (mask)RasterizedSIF757nm_oco3_LtSIF_200130_B10206r_201221032757s.nc4.tif")


SIFds20 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_01/SIF/Clipped (mask)RasterizedSIF757nm_oco3_LtSIF_200213_B10206r_200709053449s.nc4.tif")

SIFds21 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_03/SIF/Clipped (mask)RasterizedSIF757nm_oco3_LtSIF_200329_B10206r_200709053040s.nc4.tif")
SIFds22 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_03/SIF/Clipped (mask)RasterizedSIF757nm_oco3_LtSIF_200331_B10206r_201222182315s.nc4.tif")

SIFds23 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_04/SIF/Clipped (mask)RasterizedSIF757nm_oco3_LtSIF_200401_B10206r_200709051941s.nc4.tif")
SIFds24 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_04/SIF/Clipped (mask)RasterizedSIF757nm_oco3_LtSIF_200415_B10206r_200709052536s.nc4.tif")
SIFds25 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_04/SIF/Clipped (mask)RasterizedSIF757nm_oco3_LtSIF_200416_B10206r_200709052543s.nc4.tif")
SIFds26 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_04/SIF/Clipped (mask)RasterizedSIF757nm_oco3_LtSIF_200423_B10206r_200709052602s.nc4.tif")
SIFds27 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_04/SIF/Clipped (mask)RasterizedSIF757nm_oco3_LtSIF_200423_B10206r_200709052602s.nc4.tif")



SIFds28 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_05/SIF/Clipped (mask)SIF757nm_oco3_LtSIF_200501_B10206r_200709051841s.nc4.tif")
SIFds29 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_05/SIF/Clipped (mask)SIF757nm_oco3_LtSIF_200501_B10206r_200709051841s.nc4.tif")
SIFds30 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_05/SIF/Clipped (mask)SIF757nm_oco3_LtSIF_200526_B10206r_200709051918s.nc4.tif")
SIFds31 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_05/SIF/Clipped (mask)SIF757nm_oco3_LtSIF_200527_B10206r_200709051919s.nc4.tif")
SIFds32 = gdal.Open(
    "C:/Users/maria/Desktop/JPL/Projects/ECOSTRESS_OCO3/CALIFORNIA_SIF_ET/2020_05/SIF/Clipped (mask)SIF757nm_oco3_LtSIF_200530_B10206r_200709051924s.nc4.tif")

# geotransform ET
geotSIF = SIFds.GetGeoTransform()

# projection ET
projSIF = SIFds.GetProjection()


# band, should be 1
bandSIF = SIFds.GetRasterBand(1)
arraySIF = bandSIF.ReadAsArray()


bandSIF2 = SIFds2.GetRasterBand(1)
arraySIF2 = bandSIF2.ReadAsArray()
bandSIF3 = SIFds3.GetRasterBand(1)
arraySIF3 = bandSIF3.ReadAsArray()
bandSIF4 = SIFds4.GetRasterBand(1)
arraySIF4 = bandSIF4.ReadAsArray()
bandSIF5 = SIFds5.GetRasterBand(1)
arraySIF5 = bandSIF5.ReadAsArray()
bandSIF6 = SIFds6.GetRasterBand(1)
arraySIF6 = bandSIF6.ReadAsArray()
bandSIF7 = SIFds7.GetRasterBand(1)
arraySIF7 = bandSIF7.ReadAsArray()
bandSIF8 = SIFds8.GetRasterBand(1)
arraySIF8 = bandSIF8.ReadAsArray()
bandSIF9 = SIFds9.GetRasterBand(1)
arraySIF9 = bandSIF9.ReadAsArray()
bandSIF10 = SIFds10.GetRasterBand(1)
arraySIF10 = bandSIF10.ReadAsArray()
bandSIF11 = SIFds11.GetRasterBand(1)
arraySIF11 = bandSIF11.ReadAsArray()
bandSIF12 = SIFds12.GetRasterBand(1)
arraySIF12 = bandSIF12.ReadAsArray()
bandSIF13 = SIFds13.GetRasterBand(1)
arraySIF13 = bandSIF13.ReadAsArray()
bandSIF14 = SIFds14.GetRasterBand(1)
arraySIF14 = bandSIF14.ReadAsArray()
bandSIF15 = SIFds15.GetRasterBand(1)
arraySIF15 = bandSIF15.ReadAsArray()
bandSIF16 = SIFds16.GetRasterBand(1)
arraySIF16 = bandSIF16.ReadAsArray()
bandSIF17 = SIFds17.GetRasterBand(1)
arraySIF17 = bandSIF17.ReadAsArray()

bandSIF18 = SIFds18.GetRasterBand(1)
arraySIF18 = bandSIF18.ReadAsArray()
bandSIF19 = SIFds19.GetRasterBand(1)
arraySIF19 = bandSIF19.ReadAsArray()
bandSIF20 = SIFds20.GetRasterBand(1)
arraySIF20 = bandSIF20.ReadAsArray()
bandSIF21 = SIFds21.GetRasterBand(1)
arraySIF21 = bandSIF21.ReadAsArray()
bandSIF22 = SIFds22.GetRasterBand(1)
arraySIF22 = bandSIF22.ReadAsArray()
bandSIF23 = SIFds23.GetRasterBand(1)
arraySIF23 = bandSIF23.ReadAsArray()
bandSIF24 = SIFds24.GetRasterBand(1)
arraySIF24 = bandSIF24.ReadAsArray()
bandSIF25 = SIFds25.GetRasterBand(1)
arraySIF25 = bandSIF25.ReadAsArray()
bandSIF26 = SIFds26.GetRasterBand(1)
arraySIF26 = bandSIF26.ReadAsArray()
bandSIF27 = SIFds27.GetRasterBand(1)
arraySIF27 = bandSIF27.ReadAsArray()
bandSIF28 = SIFds28.GetRasterBand(1)
arraySIF28 = bandSIF28.ReadAsArray()
bandSIF29 = SIFds29.GetRasterBand(1)
arraySIF29 = bandSIF29.ReadAsArray()
bandSIF30 = SIFds30.GetRasterBand(1)
arraySIF30 = bandSIF30.ReadAsArray()
bandSIF31= SIFds31.GetRasterBand(1)
arraySIF31 = bandSIF31.ReadAsArray()
bandSIF32= SIFds32.GetRasterBand(1)
arraySIF32 = bandSIF32.ReadAsArray()






# -9e12 is nodata val
plt.figure
plt.imshow(arraySIF)
plt.title('SIF 06/25/2020 - 3')
plt.xlim([])
plt.ylim([])

SaveSIFArray = np.asarray(arraySIF)
np.savetxt("SIF_CA_05_30_2020" + ".csv", SaveSIFArray, delimiter=",")


## ---------------------------------------  #
#
a = arrayET
b = arraySIF
c = arrayET2
d = arraySIF2
e = arrayET3
f = arraySIF3
g =arrayET4
h =arraySIF4
i =arrayET5
j =arraySIF5
k = arrayET6
l = arraySIF6
m =arrayET7
n =arraySIF7
o =arrayET8
p =arraySIF8
q =arrayET9
r =arraySIF9
s =arrayET10
t =arraySIF10
u =arrayET11
v =arraySIF11
w =arrayET12
x =arraySIF12
y =arrayET13
z =arraySIF13
a2 = arrayET14
b2 = arraySIF14
c2 = arrayET15
d2 = arraySIF15
e2 = arrayET16
f2= arraySIF16
g2 =arrayET17
h2 =arraySIF17

i2 =arrayET18
j2 =arraySIF18
k2 = arrayET19
l2 = arraySIF19
m2 =arrayET20
n2 =arraySIF20
o2 =arrayET21
p2 =arraySIF21
q2 =arrayET22
r2 =arraySIF22
s2 =arrayET23
t2 =arraySIF23
u2 =arrayET24
v2 =arraySIF24
w2 =arrayET25
x2 =arraySIF25
y2 = arrayET26
z2 = arraySIF26
a3 =arrayET27
b3 = arraySIF27
c3 =arrayET28
d3 = arraySIF28
e3 = arrayET29
f3 = arraySIF29
g3 = arrayET30
h3 = arraySIF30
i3 = arrayET31
j3 = arraySIF31
k3 = arrayET32
l3 = arraySIF32


why = b[0,:],d[0,:],f[0,:],h[0,:],j[0,:],l[0,:],n[0,:],p[0,:],r[0,:],t[0,:],v[0,:],x[0,:],z[0,:],b2[0,:],d2[0,:],f2[0,:],h2[0,:],j2[0,:],l2[0,:],n2[0,:],p2[0,:],r2[0,:],t2[0,:],v2[0,:],x2[0,:],z2[0,:],b3[0,:],d3[0,:],f3[0,:],h3[0,:],j3[0,:],l3[0,:]
ex = a[0,:],c[0,:],e[0,:],g[0,:],i[0,:],k[0,:],m[0,:],o[0,:],q[0,:],s[0,:],u[0,:],w[0,:],y[0,:],a2[0,:],c2[0,:],e2[0,:],g2[0,:],i2[0,:],k2[0,:],m2[0,:],o2[0,:],q2[0,:],s2[0,:],u2[0,:],w2[0,:],y2[0,:],a3[0,:],c3[0,:],e3[0,:],g3[0,:],i3[0,:],k3[0,:]


plt.plot((a[0,:],c[0,:]),(b[0,:],d[0,:]), 'o')
#em, bee = np.polyfit(a[0,:],b[0,:], 1)
#plt.plot(a, em*a + bee)
plt.xlim([0,250])
plt.ylim([-0.4,.85])
#plt.xticks([0,50]) 


#plt.xticks([50,100,150,200,250,300,350,400,450])
#plt.xticks([450,500,550,600,650,700,750,800,850, 900,950,1000,1050,1100,1150,1200,1250])
#plt.xticks([50,100,150,200,250,300,350,400,450,500,550,600,650])
#plt.xticks([650,700,750,800,850, 900,950,1000,1050,1100,1150,1200,1250,1300])
#plt.xticks([0,50,100,150,200,250,300,350,400, 450,500,550,600,650,700,750,800,850, 900,950,1000,1050,1100,1150,1200,1255])
#plt.xticks([0,50,100,150,200,250,300,350,400,450])











plt.figure(figsize=(40,10))
#0604
plt.plot(a, b, 'o', color='rosybrown')
#0606
plt.plot(c, d, 'o', color='lightcoral')
#0607
plt.plot(e, f, 'o', color='indianred')
#0608
plt.plot(g, h, 'o', color='brown')
#0610
plt.plot(i, j, 'o', color='firebrick')
#0614
plt.plot(k, l, 'o', color='maroon')
#0614
plt.plot(m, n, 'o', color='red')
#0617
plt.plot(o, p, 'o', color='salmon')
#0617
plt.plot(q, r, 'o', color='tomato')
#0617
plt.plot(s, t, 'o', color='coral')
#0618
plt.plot(u, v, 'o', color='orangered')
#0619
plt.plot(w, x, 'o', color='sienna')
#0621
plt.plot(y, z, 'o', color='chocolate')
#0621
plt.plot(a2, b2, 'o', color='saddlebrown')
#0625
plt.plot(c2, d2, 'o', color='sandybrown')
#0625
plt.plot(e2, f2, 'o', color='peachpuff')
#0625
plt.plot(g2, h2, 'o', color='peru')

#0129
plt.plot(i2, j2, 'o', color='darkgoldenrod')

  #0130
plt.plot(k2, l2, 'o', color='gold')

#0213
plt.plot(m2, n2, 'o', color='green')

#0329
plt.plot(o2, p2, 'o', color='turquoise')
#0331
plt.plot(q2, r2, 'o', color='lightseagreen')


#0401
plt.plot(s2, t2, 'o', color='deepskyblue')
#0415
plt.plot(u2, v2, 'o', color='lightskyblue')
#0416
plt.plot(w2, x2, 'o', color='dodgerblue')
#0423
plt.plot(y2, z2, 'o', color='royalblue')
#0423
plt.plot(a3, b3, 'o', color='blue')


#0501
plt.plot(c3, d3, 'o', color='blueviolet')
#0501
plt.plot(e3, f3, 'o', color='indigo')
#0526
plt.plot(g3, h3, 'o', color='purple')
#0527
plt.plot(i3, j3, 'o', color='magenta')
#0530
plt.plot(k3, l3, 'o', color='orchid')




plt.title('SIF vs. ET 01/2020 - 06/2020')
plt.xlabel('ET (W/m^2)')
plt.ylabel('SIF (W/m^2/um/sr)')


plt.xlim([0,1255])
plt.ylim([-0.4,.85])
#plt.xticks([0,50]) 
#plt.xticks([50,100,150,200,250,300,350,400,450])
#plt.xticks([450,500,550,600,650,700,750,800,850, 900,950,1000,1050,1100,1150,1200,1250])
#plt.xticks([50,100,150,200,250,300,350,400,450,500,550,600,650])
#plt.xticks([650,700,750,800,850, 900,950,1000,1050,1100,1150,1200,1250,1300])
plt.xticks([0,50,100,150,200,250,300,350,400, 450,500,550,600,650,700,750,800,850, 900,950,1000,1050,1100,1150,1200,1255])
#plt.xticks([0,50,100,150,200,250,300,350,400,450])

#---------------------------------------------------------------------------------------------------------------------------------
plt.figure(figsize=(40,10))
plt.plot(a, b, 'o', color='black')
plt.plot(c, d, 'o', color='black')
plt.plot(e, f, 'o', color='black')
plt.plot(g, h, 'o', color='black')
plt.plot(i, j, 'o', color='black')
plt.plot(k, l, 'o', color='black')
plt.plot(m, n, 'o', color='black')
plt.plot(o, p, 'o', color='black')
plt.plot(q, r, 'o', color='black')
plt.plot(s, t, 'o', color='black')
plt.plot(u, v, 'o', color='black')
plt.plot(w, x, 'o', color='black')
plt.plot(y, z, 'o', color='black')
plt.plot(a2, b2, 'o', color='black')
plt.plot(c2, d2, 'o', color='black')
plt.plot(e2, f2, 'o', color='black')
plt.plot(g2, h2, 'o', color='black')


plt.plot(i2, j2, 'o', color='black')
plt.plot(k2, l2, 'o', color='black')
plt.plot(m2, n2, 'o', color='black')
plt.plot(o2, p2, 'o', color='black')
plt.plot(q2, r2, 'o', color='black')
plt.plot(s2, t2, 'o', color='black')
plt.plot(u2, v2, 'o', color='black')
plt.plot(w2, x2, 'o', color='black')
plt.plot(u2, v2, 'o', color='black')
plt.plot(w2, x2, 'o', color='black')
plt.plot(y2, z2, 'o', color='black')
plt.plot(a3, b3, 'o', color='black')
plt.plot(c3, d2, 'o', color='black')
plt.plot(e3, f3, 'o', color='black')
plt.plot(g3, h3, 'o', color='black')
plt.plot(i3, j3, 'o', color='black')
plt.plot(k3, l3, 'o', color='black')

plt.title('SIF vs. ET 01/2020 - 06/2020')
plt.xlabel('ET (W/m^2)')
plt.ylabel('SIF (W/m^2/um/sr)')


plt.xlim([0,425])
plt.ylim([-0.4,.85])
#plt.xticks([0,50]) 
#plt.xticks([50,100,150,200,250,300,350,400,450])
#plt.xticks([450,500,550,600,650,700,750,800,850, 900,950,1000,1050,1100,1150,1200,1250])
#plt.xticks([50,100,150,200,250,300,350,400,450,500,550,600,650])
#plt.xticks([650,700,750,800,850, 900,950,1000,1050,1100,1150,1200,1250,1300])
#plt.xticks([0,50,100,150,200,250,300,350,400, 450,500,550,600,650,700,750,800,850, 900,950,1000,1050,1100,1150,1200,1255])
plt.xticks([0,50,100,150,200,250,300,350,400,425])





