from django.shortcuts import render, redirect
import os
import folium 

# Create your views here.

def home(request):
    shp_dir = os.path.join(os.getcwd(), 'media', 'shp')
    m = folium.Map(location=[-16.22, -71.59], zoom_start=10)

    style_basin = {'fill_color': '#228B22', 'color':'#228B22'}
    style_river = {'color':'blue'}

    folium.GeoJson(os.path.join(shp_dir, 'basin.geojson'), name='basin', 
        style_function=lambda x: style_basin).add_to(m)
    folium.GeoJson(os.path.join(shp_dir, 'rivers.geojson'), name='river', 
        style_function=lambda x: style_river).add_to(m)
    m = m._repr_html_()

    context = {'my_map': m}
    return render(request, 'geoApp/home.html', context)
