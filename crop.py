import glob
from fiona.crs import from_epsg
import geopandas
import rasterio
import fiona
import rasterio.mask
import os


def crop_image(save_directory, AOI_path, crs, images):
    data_proj_path = glob.glob(AOI_path + '/*.geojson')

    data = geopandas.read_file(data_proj_path[0])
    data_proj = data.copy()
    data_proj['geometry'] = data_proj['geometry'].to_crs(epsg=crs)
    data_proj.crs = from_epsg(crs)
    out_path = AOI_path + '/Corrected_crs_AOI.geojson'

    # Save to disk
    data_proj.to_file(out_path)

    with fiona.open(out_path, "r") as shapefile:
        shapes = [feature["geometry"] for feature in shapefile]

    for f in range(0, len(images)):
        with rasterio.open(images[f]) as src:
            out_image, out_transform = rasterio.mask.mask(src, shapes, crop=True)
            out_meta = src.meta

        out_meta.update({"driver": "GTiff",
                         "height": out_image.shape[1],
                         "width": out_image.shape[2],
                         "transform": out_transform,
                         "nodata":-999})
        filepath = save_directory + 'Cropped_' + os.path.basename(images[f])                     # ALTERAR DEPENDENDO DA FONTE DOS DADOS ---> API 51: -----> qgis 55:
        with rasterio.open(filepath, "w", **out_meta) as dest:
            dest.write(out_image)




# crop_image('D:/Startup_Voucher/Projetos/One_year_test/Cropped', 'D:/Startup_Voucher/Projetos/One_year_test', 32629, )
