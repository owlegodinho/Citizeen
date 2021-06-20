from PyQt5.QtCore import QFileInfo
from PyQt5.QtCore import QUrl
from qgis.core import *
import os
import qgis.utils
from qgis.utils import iface
import requests

layer_path = "C:/Users/Illya Grytsayev/Desktop/OWL/cassini/cropped/Cropped_NDVI__20210504T112111.tif"

# Add layer to QGIS
source = layer_path
raster_layer = QgsRasterLayer(source, "NDVI Raster Layer")
assert raster_layer.isValid()
my_project = QgsProject.instance()
my_project.addMapLayer(raster_layer)

# Correct Position
canvas = iface.mapCanvas()
selectedcrs = "EPSG:3994"
target_crs = QgsCoordinateReferenceSystem()
target_crs.createFromUserInput(selectedcrs)
canvas.setDestinationCrs(target_crs)
# Apply style
path_to_qml = "C:/Users/Illya Grytsayev/Desktop/OWL/cassini/cropped/ndvi_map_style.qml"
assert raster_layer.loadNamedStyle(path_to_qml)

extent = raster_layer.extent()
width, height = raster_layer.width(), raster_layer.height()
renderer = raster_layer.renderer()
provider = raster_layer.dataProvider()
crs = raster_layer.crs().toWkt()
pipe = QgsRasterPipe()
pipe.set(provider.clone())
pipe.set(renderer.clone())
file_writer = QgsRasterFileWriter("C:/Users/Illya Grytsayev/Desktop/OWL/cassini/cropped/rendered_test.tif")
file_writer.writeRaster(pipe, width, height, extent, raster_layer.crs())
