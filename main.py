import os
import socket
from bounds import get_bounds,convert_crs
from mapDeployment import map_app
from indexes import ndvi
from crop import cropping
import subprocess as sub

if socket.gethostname() == 'DESKTOP-K8VPKQJ':
    os.chdir('C:/Users/Eduardo Godinho/Desktop/cassini')
elif socket.gethostname() == 'DESKTOP-K8VPKQJ': # corre apenas esta linha num print para saberes qual é
    os.chdir('C:/Users/Illya Grytsayev/Desktop/cassini')
# crs, imagePath = ndvi('S2A_MSIL2A_20210504T112111_N0300_R037_T29TNE_20210504T143002'
#      '/S2A_MSIL2A_20210504T112111_N0300_R037_T29TNE_20210504T143002.SAFE/'
#      'GRANULE/L2A_T29TNE_A030636_20210504T112445/IMG_DATA/R10m', 'processed')

# cropping('processed/NDVI__20210504T112111.tif','jardim_bot.geojson', 'corrected_crs')
# map_app('C:/Users/Eduardo Godinho/Desktop/cassini', 0, 'database.csv')
qgis_call = [r'C:/OSGeo4W64/OSGeo4W.bat', 'qgis']
sub.Popen(qgis_call, stdout=sub.PIPE, stderr=sub.PIPE)