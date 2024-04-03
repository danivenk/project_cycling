import gpxpy
import matplotlib.pyplot as plt
import datetime
from geopy import distance
from math import sqrt, floor
import numpy as np
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
import haversine
import gmplot as gm
import os
import polyline

# Path to current file
PATH = os.path.dirname(os.path.abspath(__file__))

files = os.listdir(PATH + "/Data/")

try:
    loaded = pd.read_csv(PATH + "/Loaded.csv")
    # df = pd.DataFrame(columns=['lon', 'lat', 'alt', 'time','type','file'])
    loadedfiles = []
    coords = []

    for i in range(0, len(loaded['file'])):
        if loaded['file'][i] in loadedfiles:
            pass
        else:
            loadedfiles.append(loaded['file'][i])

    for file in range(0, len(files)):
        if files[file] in loadedfiles:
            print(str(file + 1) + ". " + files[file] + " already loaded")
            for i in range(0, len(loaded)):
                if loaded['file'][i] == files[file]:
                    coords.append([loaded['lat'][i], loaded['lon'][i]])
                else:
                    pass
        else:
            if files[file][-3:] == "gpx":
                1# print("Please load " + files[file] + " with the GPS loader")
except FileNotFoundError:
    print("Nothing is yet loaded\nPlease run the GPS loader first")

print(loadedfiles)

min_lat = min(loaded['lat'])
max_lat = max(loaded['lat'])
min_lon = min(loaded['lon'])
max_lon = max(loaded['lon'])

map_file = PATH + '/map-all.html'
# coords = [[38.5, -120.2], [40.7, -120.9], [43.2, -126.4]]
# coords = [[38.5, 40.7, 43.2], [-120.2, -120.9, -126.4]]
lat, lon = zip(*coords)
# print(polyline.decode(enc_coords))

## Create empty map with zoom level 16
mymap = gm.GoogleMapPlotter(min_lat + (max_lat - min_lat) / 2, min_lon + \
    (max_lon - min_lon) / 2, 16, apikey="AIzaSyAyjorM33q3OJFTVcUOKbddvTTdLxwJZqU")
# mymap.scatter(enc_coords, 'blue', size=1, marker=False)
# for file in range(0, len(loadedfiles)):
mymap.scatter(lat,lon, 'blue', size=1, marker=False)
mymap.draw(map_file)

os.system(map_file)
