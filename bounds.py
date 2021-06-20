import rasterio as rio
from rasterio.warp import calculate_default_transform, reproject, Resampling
import numpy as np
import os


def convert_crs(filepath, crs='EPSG:3763'):

    """The function takes one .tif file and
    converts it to the selected CRS"""

    with rio.open(filepath, 'r') as src:
        transform, width, height = calculate_default_transform(
            src.crs, crs, src.width, src.height, *src.bounds)
        kwargs = src.meta.copy()
        kwargs.update({
            'crs': crs,
            'transform': transform,
            'width': width,
            'height': height
        })

        file_save = 'corrected_crs/'+os.path.basename(filepath)[:-5]+'_'+ crs.replace(':', '_')+'.tif'
        # print(file_save)
        with rio.open(file_save, 'w', **kwargs) as dst:
            reproject(
                source=rio.band(src, 1),
                destination=rio.band(dst, 1),
                src_transform=src.transform,
                src_crs=src.crs,
                dst_transform=transform,
                dst_crs=crs,
                resampling=Resampling.nearest
            )
        dst.close()
    src.close()
    return file_save


def get_bounds(filepath):

    """Takes a .tif file
    and extracts its extent"""

    with rio.open(filepath, 'r') as src:
        bounds = src.bounds
        corrected_bounds = np.array([bounds[0], bounds[1], bounds[2], bounds[3]])
    return corrected_bounds

