import os
import rasterio
import numpy as np


def ndvi(directory_path, process_path):

    ndvi_path = list()
    bands_4 = list()
    bands_8 = list()
    for root, dirs, files in os.walk(directory_path, topdown=False):
        for name in files:
            if name.endswith('B04_10m.jp2'):                                # ALTERAR DEPENDENDO DA FONTE DOS DADOS ---> qgis 'B04_10m.jp2' -----> API 'B04.jp2'
                bands_4.append(os.path.join(root, name))
            elif name.endswith('B08_10m.jp2'):                              # ALTERAR DEPENDENDO DA FONTE DOS DADOS ---> qgis 'B08_10m.jp2' -----> API 'B08.jp2'
                bands_8.append(os.path.join(root, name))
    print(bands_4, bands_8)
    b4 = rasterio.open(bands_4[0])
    b4_crs = str(b4.crs)
    b4_crs = int(b4_crs[5:])
    b4_profile = b4.profile
    b4_profile.update({"driver": "GTiff",
                       "dtype": "float32"})
    for b in range(0, len(bands_4)):
        b4 = rasterio.open(bands_4[b])
        b8 = rasterio.open(bands_8[b])

        b4 = b4.read()
        b8 = b8.read()
        np.seterr(divide='ignore', invalid='ignore')

        # Calculate NDVI
        ndvi = (b8.astype(np.float32) - b4.astype(np.float32)) / (b8 + b4)
        filedate = bands_4[b][-28:-12]                                  # ALTERAR DEPENDENDO DA FONTE DOS DADOS ---> API -28:-12 -----> qgis -23:-8
        ndvi_path.append(process_path + '/NDVI_' + filedate + '.tif')
        with rasterio.open(ndvi_path[b], "w", **b4_profile) as dest:
            dest.write(ndvi)
    return b4_crs, ndvi_path



def mi(directory_path, process_path):

    mi_path = list()
    bands_11 = list()
    bands_8A = list()
    for root, dirs, files in os.walk(directory_path, topdown=False):
        for name in files:
            if name.endswith('B11_20m.jp2'):                                   # ALTERAR DEPENDENDO DA FONTE DOS DADOS ---> API 'B11_20m.jp2' -----> qgis 'B11.jp2'
                bands_11.append(os.path.join(root, name))
            elif name.endswith('B8A_20m.jp2'):                                 # ALTERAR DEPENDENDO DA FONTE DOS DADOS ---> API 'B8A_20m.jp2' -----> qgis 'B8A.jp2'
                bands_8A.append(os.path.join(root, name))
    b11 = rasterio.open(bands_11[0])
    b11_crs = str(b11.crs)
    b11_crs = int(b11_crs[5:])
    b11_profile = b11.profile
    b11_profile.update({"driver": "GTiff",
                       "dtype": "float64"})
    for b in range(0, len(bands_11)):
        b11 = rasterio.open(bands_11[b])
        b8A = rasterio.open(bands_8A[b])

        b11 = b11.read()
        b8A = b8A.read()
        np.seterr(divide='ignore', invalid='ignore')

        # Calculate NDVI
        mi = (b8A.astype(float) - b11.astype(float)) / (b8A + b11)
        filedate = bands_11[b][-28:-12]                                     # ALTERAR DEPENDENDO DA FONTE DOS DADOS ---> API -28:-12 -----> qgis -23:-8
        mi_path.append(process_path + 'MI_' + filedate + '.tif')
        with rasterio.open(mi_path[b], "w", **b11_profile) as dest:
            dest.write(mi)
    return b11_crs, mi_path



