import os
import numpy as np
import rasterio
from rasterio import mask
import json
import geopandas as gpd
from bounds import convert_crs


def cropping(image, AOI, corrected_crs):
    geo = gpd.read_file(AOI)
    coords = getFeatures(geo)
    convert_crs(image, corrected_crs, crs='EPSG:4326')
    for root, dirs, files in os.walk(corrected_crs):
        for file in files:
            print(file)
            with rasterio.open(os.path.join(root,file), 'r') as src:

                out_image, out_transform = rasterio.mask.mask(src, shapes=coords, crop=True)
                out_meta = src.meta.copy()
                out_meta.update({'driver': 'GTiff',
                                 'height': out_image.shape[1],
                                 'width': out_image.shape[2],
                                 'transform': out_transform,
                                 'nodata': 0/np.inf,
                                 })
            with rasterio.open(os.path.join('cropped', 'Cropped_'+os.path.basename(image)),'w',**out_meta) as dest:
                dest.write(out_image)
                print(coords)


def getFeatures(gdf):
    """Function to parse features from GeoDataFrame in such a manner that rasterio wants them"""
    import json
    return [json.loads(gdf.to_json())['features'][0]['geometry']]


