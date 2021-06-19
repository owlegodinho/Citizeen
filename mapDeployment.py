import branca.element
import folium
from folium.raster_layers import ImageOverlay
import base64
import os
import webbrowser
from PIL import Image
import pandas as pd
from bounds import get_bounds


def map_app(satImages, popupImgDatabase, galileo_position=(40.2059, -8.4241), size=(150, 130)):

    m = folium.Map(location=[40.205217, -8.422927],
                   zoom_start=17
                   )
    googleMaps = folium.TileLayer(tiles='http://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}',
                                  attr='Google Hybrid Tiles',
                                  name='Google Maps')

    df = pd.read_csv(popupImgDatabase, delimiter=';')
    for i in range(0, df.shape[0]):
        im = Image.open(str(df['Image Name'][i]))
        new_img = im.resize(size)
        new_img.save(df['Image Name'][i], optimize=True)
        encoded = base64.b64encode(open(df['Image Name'][i], 'rb').read())
        html_photo = '<p style="font-family:Arial; font-size: 15px"><b>Date:</b> {}</p>' \
                     '<p style="font-family:Arial; font-size: 15px"><b>Rating:</b> {}</p>' \
                     '<center><img src="data:image/jpeg;base64,{}"></center>'.format
        iframe = branca.element.IFrame(html_photo(df['Dates'][i], df['Rating'][i], encoded.decode('UTF-8')),
                                       width=180, height=180)
        popup = folium.Popup(iframe, max_width=1000, parse_html=True)
        folium.Marker(location=[df['Lat'][i], df['Long'][i]],
                      icon=folium.Icon(color='blue', icon='camera', prefix='fa'),
                      popup=popup).add_to(m)
    folium.features.LatLngPopup().add_to(m)
    m.add_child(googleMaps)

    html_position = '<center><p style="font-family:Arial; font-size: 12px"> You are here!</p></center>'
    iframe_position = branca.element.IFrame(html_position,width=105, height=34)
    popup_position = folium.Popup(iframe_position, parse_html=True)
    folium.Marker(location=galileo_position,
                  icon=folium.Icon(color='red', icon='crosshairs', prefix='fa'),
                  popup=popup_position).add_to(m)
    bottom, left, top, right = get_bounds(satImages[0])
    m.add_child(ImageOverlay(image=satImages[0], opacity=0.7,
                             bounds=[[left, bottom], [right, top]],
                             name='NDVI 04/05/2021')

                )

    folium.LayerControl().add_to(m)
    colormap = branca.colormap.linear.RdYlGn_09.scale(-0.2, 1)
    colormap = colormap.to_step(index=[-0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1])
    colormap.caption = 'NDVI'
    colormap.add_to(m)

    m.save('citizeen.html')
    print('aqui')
    webbrowser.open('citizeen.html')


os.chdir('C:/Users/Eduardo Godinho/Desktop/cassini')