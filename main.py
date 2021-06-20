import os
import socket
from bounds import get_bounds, convert_crs
from mapDeployment import map_app
from indexes import ndvi
from crop import cropping
from tiff_to_png import convert_tif_to_png
import subprocess as sub
from create_script_qgis import write_script
import time

# orig_directory = os.getcwd()
qgis_call = [r'C:/OSGeo4W64/OSGeo4W.bat', 'qgis', '--nologo', '--code', 'python_qgis.py']  # QGIS shell command to run script on PyQgis

crs, imagePath = ndvi('S2_bands', 'processed')

converted_crs_path = convert_crs(imagePath[0], 'EPSG:4326')

cropped_save_path = cropping(converted_crs_path, 'jardim_bot.geojson', 'corrected_crs')

rendered_path = write_script(cropped_save_path)
sub.Popen(qgis_call, stdout=sub.PIPE, stderr=sub.PIPE)
time.sleep(15)
png_files = convert_tif_to_png(rendered_path, os.path.join('png_files', os.path.basename(converted_crs_path)))
print(os.path.join('png_files', os.path.basename(converted_crs_path)))
map_app([png_files], 'database.csv')



