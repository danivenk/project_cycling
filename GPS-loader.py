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

# Path to current file
PATH = os.path.dirname(os.path.abspath(__file__))

data = []

files = os.listdir(PATH + "/Data/")

try:
    loaded = pd.read_csv(PATH + "/Loaded.csv", index_col=None, header=0)

    loadi = int(input("from which file whould you like to begin loading? "))
    loadf = int(input("to which file whould you like to load? (Must be " + \
        "bigger than begin) "))

    df = pd.DataFrame(columns=['lon', 'lat', 'alt', 'time','type','file'])
    loadedfiles = []
    
    for i in range(0, len(loaded['file'])):
        if loaded['file'][i] in loadedfiles:
            pass
        else:
            loadedfiles.append(loaded['file'][i])

    print(loadedfiles)

    for file in range(loadi - 1, loadf):
        if files[file] in loadedfiles:
            print(files[file] + " already loaded")
            df.append(loaded[loaded['file'] == files[file]], ignore_index=False, sort=False)
            pass
        else:
            if files[file][-3:] == "gpx":
                gpx_file = open(PATH + "/Data/" + files[file], 'r')
                gpx = gpxpy.parse(gpx_file)

                for i in range(0, len(gpx.tracks)):
                    for j in range(0, len(gpx.tracks[i].segments)):
                        data.append(gpx.tracks[i].segments[j].points)
                        print(gpx.tracks[i].name)
                for i in range(0, len(data)):
                    for point in data[i]:
                        df = df.append({'lon': point.longitude, \
                            'lat': point.latitude, 'alt': point.elevation, \
                                'time': point.time, 'type':point.name, \
                                    'file': files[file]}, ignore_index=True)
            else:
                pass
            print(str(file + 1) + ". " + files[file] + " loaded")

    try:
        print(df)
        df.to_csv(PATH + "/Loaded.csv")
    except NameError:
        pass
except FileNotFoundError:
    df = pd.DataFrame(columns=['lon', 'lat', 'alt', 'time', 'type', 'file'])
    df.to_csv(PATH + "/Loaded.csv")
    print("Nothing is yet loaded\nPlease run again")
