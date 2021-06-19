import os
import socket
from bounds import get_bounds, convert_crs
from mapDeployment import map_app
from indexes import ndvi
from crop import cropping
from tiff_to_png import convert_tif_to_png
import subprocess as sub

qgis_call = [r'C:/OSGeo4W64/OSGeo4W.bat', 'qgis', '--nologo', '--code']  # QGIS shell command to run script on PyQgis


# Working Computer path´s
if socket.gethostname() == 'DESKTOP-K8VPKQJ':
    os.chdir('C:/Users/Eduardo Godinho/Desktop/cassini')
    qgis_call.append('"D:/Startup_Voucher/Projetos/202112_Citizeen_Cassini/python_qgis.py"')
elif socket.gethostname() == 'DESKTOP-M053QQK': # corre apenas esta linha num print para saberes qual é
    os.chdir('C:/Users/Illya Grytsayev/Desktop/OWL/cassini')
    qgis_call.append('"C:/Users/Illya Grytsayev/PycharmProjects/Citizeen/python_qgis.py"')

# crs, imagePath = ndvi('S2A_MSIL2A_20210504T112111_N0300_R037_T29TNE_20210504T143002'
#      '/S2A_MSIL2A_20210504T112111_N0300_R037_T29TNE_20210504T143002.SAFE/'
#      'GRANULE/L2A_T29TNE_A030636_20210504T112445/IMG_DATA/R10m', 'processed')

# convert_crs('processed/NDVI__20210504T112111.tif', 'corrected_crs', 'EPSG:4326')
# cropping('processed/NDVI__20210504T112111.tif', 'jardim_bot.geojson', 'corrected_crs')
# convert_tif_to_png('cropped/NDVI_20210504_rendered.tif', 'cropped/NDVI_20210504')
map_app(['cropped/NDVI_20210504.png'], 'database.csv')

# sub.Popen(qgis_call, stdout=sub.PIPE, stderr=sub.PIPE)
