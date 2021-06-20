import rasterio as rio
from rasterio.warp import calculate_default_transform, reproject, Resampling
import numpy as np
import os


def convert_crs(filepath, save_dir, crs='EPSG:3763'):

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

        filename = os.path.basename(filepath)[:-4]+'_'+crs.replace(':', '_')+'.tif'
        # print(filename+'\n')
        converted_crs_path = os.path.join(save_dir, filename)
        print(save_dir)
        with rio.open(converted_crs_path, 'w', **kwargs) as dst:
            reproject(
                source=rio.band(src, 1),
                destination=rio.band(dst, 1),
                src_transform=src.transform,
                src_crs=src.crs,
                dst_transform=transform,
                dst_crs=crs,
                resampling=Resampling.nearest
            )
        src.close()
    return converted_crs_path


def get_bounds(filepath):

    """Takes a .tif file
    and extracts its extent"""

    with rio.open(filepath, 'r') as src:
        bounds = src.bounds
        corrected_bounds = np.array([bounds[0], bounds[1], bounds[2], bounds[3]])
    return corrected_bounds

