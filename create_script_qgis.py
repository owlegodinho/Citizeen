import os


def write_script(orig_dir,layer_path):
    os.chdir(orig_dir)
    with open('python_qgis.py', 'w') as f:
        f.writelines(['from PyQt5.QtCore import QFileInfo\n',
                      'from PyQt5.QtCore import QUrl\n',
                      'from qgis.core import *\n',
                      'import os\n',
                      'import qgis.utils\n',
                      'from qgis.utils import iface\n',
                      'import requests\n\n',
                      'layer_path = ' +'"'+ str(layer_path) + '"\n\n',
                      '# Add layer to QGIS\n',
                      'source = layer_path\n',
                      'raster_layer = QgsRasterLayer(source, "NDVI Raster Layer")\n',
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
                      'path_to_qml = "C:/Users/Illya Grytsayev/Desktop/OWL/cassini/cropped/ndvi_map_style.qml"\n',
                      'assert raster_layer.loadNamedStyle(path_to_qml)\n\n',
                      'extent = raster_layer.extent()\n',
                      'width, height = raster_layer.width(), raster_layer.height()\n',
                      'renderer = raster_layer.renderer()\n',
                      'provider = raster_layer.dataProvider()\n',
                      'crs = raster_layer.crs().toWkt()\n',
                      'pipe = QgsRasterPipe()\n',
                      'pipe.set(provider.clone())\n',
                      'pipe.set(renderer.clone())\n',
                      'file_writer = QgsRasterFileWriter("C:/Users/Illya Grytsayev/Desktop/OWL/cassini/cropped/rendered_test.tif")\n',
                      'file_writer.writeRaster(pipe, width, height, extent, raster_layer.crs())\n'])