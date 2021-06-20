from osgeo import gdal


def convert_tif_to_png(file, output_name):
    open_gdal = gdal.Open(file)
    driver = gdal.GetDriverByName('PNG')
    driver.CreateCopy(output_name + '.png', open_gdal)

