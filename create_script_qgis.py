import os
import socket
import subprocess as sub


def write_script(layer_path, code_dir, working_dir):
    # os.chdir(code_dir)
    with open(code_dir + 'python_qgis.py', 'w') as f:
        f.writelines(['from PyQt5.QtCore import QFileInfo\n',
                      'from PyQt5.QtCore import QUrl\n',
                      'from qgis.core import *\n',
                      'import os\n',
                      'import qgis.utils\n',
                      'from qgis.utils import iface\n',
                      'import requests\n\n',
                      'layer_path = ' + '"{}"'.format(working_dir + layer_path),
                      '# Add layer to QGIS\n',
                      'raster_layer = QgsRasterLayer(layer_path, "NDVI Raster Layer")\n',
                      'assert raster_layer.isValid()\n',
                      'my_project = QgsProject.instance()\n',
                      'my_project.addMapLayer(raster_layer)\n\n',
                      '# Correct Position\n',
                      'canvas = iface.mapCanvas()\n',
                      'selectedcrs = "EPSG:3994"\n',
                      'target_crs = QgsCoordinateReferenceSystem()\n',
                      'target_crs.createFromUserInput(selectedcrs)\n',
                      'canvas.setDestinationCrs(target_crs)\n',
                      '# Apply style\n',
                      'path_to_qml = "{}" + "ndvi_map_style.qml"\n'.format(code_dir),
                      'assert raster_layer.loadNamedStyle(path_to_qml)\n\n',
                      'extent = raster_layer.extent()\n',
                      'width, height = raster_layer.width(), raster_layer.height()\n',
                      'renderer = raster_layer.renderer()\n',
                      'provider = raster_layer.dataProvider()\n',
                      'crs = raster_layer.crs().toWkt()\n',
                      'pipe = QgsRasterPipe()\n',
                      'pipe.set(provider.clone())\n',
                      'pipe.set(renderer.clone())\n',
                      'file_writer = QgsRasterFileWriter("rendered_test.tif")\n',
                      'file_writer.writeRaster(pipe, width, height, extent, raster_layer.crs())\n'])

#
# write_script('C:/Users/Eduardo Godinho/Desktop/cassini/cropped/Cropped_NDVI__20210504T112111.tif')
#
# qgis_call = ['C:/OSGeo4W64/OSGeo4W.bat', 'qgis', '--nologo', '--code']  # QGIS shell command to run script on PyQgis
# #
#
# # # Working Computer path´s
# if socket.gethostname() == 'DESKTOP-K8VPKQJ':
#     # os.chdir('C:/Users/Eduardo Godinho/Desktop/cassini')
#     qgis_call.append('python_qgis.py')
#
# sub.Popen(qgis_call, stdout=sub.PIPE, stderr=sub.PIPE)