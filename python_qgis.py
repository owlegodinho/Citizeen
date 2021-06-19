from PyQt5.QtCore import QFileInfo
from PyQt5.QtCore import QUrl
from qgis.core import *
import qgis.utils
from qgis.utils import iface
import requests


# Layer path
layer_path = ''
# Add layer to QGIS
cropped/Cropped_NDVI__20210504T112111.tif
source = 'D:/Project/202101_Myhome/dados_satelite/NDVI/Cropped_NDVI_2021-06-06.tif'
raster_layer = QgsRasterLayer(source, "NDVI Raster Layer")
assert raster_layer.isValid()
my_project = QgsProject.instance()
my_project.addMapLayer(raster_layer)

# Correct Position
canvas = iface.mapCanvas()
selectedcrs="EPSG:3994"
target_crs = QgsCoordinateReferenceSystem()
target_crs.createFromUserInput(selectedcrs)
canvas.setDestinationCrs(target_crs)