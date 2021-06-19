import os

import numpy as np
import rasterio
from rasterio import features
from rasterio import mask
import json
import geopandas as gpd
from fiona.crs import from_epsg
import pycrs
from bounds import convert_crs
os.chdir('C:/Users/Eduardo Godinho/Desktop/cassini/')


def cropping(image, AOI):
    geo = gpd.read_file(AOI)
    coords = getFeatures(geo)
    convert_crs(image, 'corrected_crs', crs='EPSG:4326')
    with rasterio.open('corrected_crs/NDVI__20210504T112111_EPSG_4326.tif', 'r') as src:
        epsg_code = int(src.crs.data['init'][5:])
        out_image, out_transform = rasterio.mask.mask(src, shapes=coords, crop=True)
        out_meta = src.meta.copy()
        out_meta.update({'driver': 'GTiff',
                         'height': out_image.shape[1],
                         'width': out_image.shape[2],
                         'transform': out_transform,
                         'nodata': 0/np.inf,
                        })
    with rasterio.open(os.path.join('cropped','Cropped_'+os.path.basename(image)),'w',**out_meta) as dest:
        dest.write(out_image)
    print(coords)


def getFeatures(gdf):
    """Function to parse features from GeoDataFrame in such a manner that rasterio wants them"""
    import json
    return [json.loads(gdf.to_json())['features'][0]['geometry']]




