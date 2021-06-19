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
        with rio.open(os.path.join(save_dir, filename), 'w', **kwargs) as dst:
            reproject(
                source=rio.band(src, 1),
                destination=rio.band(dst, 1),
                src_transform=src.transform,
                src_crs=src.crs,
                dst_transform=transform,
                dst_crs=crs,
                resampling=Resampling.nearest
            )
    pass


def get_bounds(filepath):

    """Takes a .tif file
    and extracts its extent"""

    with rio.open(filepath, 'r') as src:
        bounds = src.bounds
        corrected_bounds = np.array([bounds[0], bounds[1], bounds[2], bounds[3]])
    return corrected_bounds


file_path = "D:/Startup_Voucher/Projetos/202106_MORADIA_CBD/_base/NDMI/dados_brutos/Cropped_NDMI_2020-01-10.tif"
# convert_crs(file_path, 'C:/Users/Eduardo Godinho/Desktop')
# img_bounds = get_bounds(file_path)
# print(img_bounds)