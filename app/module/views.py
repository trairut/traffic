from django.http import HttpResponse
from django.shortcuts import render
from .models import location, focus, statistics
import folium

def show(request):
    trail_coordinates = [
        (13.75042, 100.56781),
        (13.74924, 100.55788),
    ]

    # Point of Interest (POI)
    poi = focus.objects.filter(show=True)
    if poi:
        start_coords = (poi[0].latitude, poi[0].longitude)
        map = folium.Map(start_coords, zoom_start=14)
        folium.PolyLine(trail_coordinates, tooltip="Coast").add_to(map)
        folium.Circle(radius=5000, location=[poi[0].latitude, poi[0].longitude], color='crimson', fill=False,).add_to(map)
    else:
        start_coords = (13.76495, 100.53829)
        map = folium.Map(start_coords, zoom_start=14)

    # Show all locations
    data = location.objects.filter(group=1)
    for x in data:
        folium.Marker(location=[x.latitude, x.longitude], popup=folium.Popup(x.description, max_width=400,min_width=300), tooltip=folium.Tooltip(permanent=True, text=x.name)).add_to(map)
        # folium.Marker(location=[x.latitude, x.longitude], popup=folium.Popup(x.description, max_width=400,min_width=300), tooltip=x.name).add_to(map)
        # folium.Marker(location=[x.latitude, x.longitude], popup=folium.Popup(x.description, max_width=400,min_width=300), tooltip='<h1>'+x.name+'</h1>').add_to(map)

    # Tile Layer
    # folium.raster_layers.TileLayer('CartoDB positron').add_to(map)
    # folium.raster_layers.TileLayer('CartoDB dark_matter').add_to(map)
    folium.LayerControl().add_to(map)

    # statistic = statistics.objects.last()
    # for x in statistic:
        # temperature = x.temperature

    temperature = 40.0
    pm = 92.0
    rainfall = 10.0

    map = map._repr_html_()
    context = {
        'map': map,
        'temperature': temperature,
        'pm': pm,
        'rainfall': rainfall,

    }

    return render(request,"maps.html", context)