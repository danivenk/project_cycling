#!/usr/bin/env python
# -*- Coding: utf-8 -*-

import os
import sys
import gpxpy

import matplotlib.pyplot as plt
import numpy as np
import scipy.spatial as scsp

from alive_progress import alive_it

from classes.point import Point


def main(argv):

    types = ["Cycling", "Walking", "Other", "Skating", "Running"]

    if len(argv) != 0 and len(argv) != 1:
        help(types)
    if len(argv) == 1 and argv[0] not in types:
        help(types)
    elif len(argv) == 1:
        print(f"Initiating for {argv[0]}")
        onetype = True
    else:
        print("Initiating for all availble types")
        onetype = False

    year = ""

    PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Data")
    PATH_cor = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "Data_Runkeeper-correction")

    files = [os.path.abspath(os.path.join(PATH, file)) for file in
             os.listdir(PATH) if file.endswith(".gpx") if year in file]
    correction_dir = [item for item in os.listdir(PATH_cor)
                      if os.path.isdir(os.path.join(PATH_cor, item))
                      and year in item]

    for correction in correction_dir:
        files.extend([os.path.abspath(os.path.join(PATH_cor, correction,
                      "merged", file)) for file in
                      os.listdir(os.path.join(PATH_cor, correction, "merged"))])

    gpxs = []

    for file in alive_it(files):
        with open(file, "r") as _file:
            gpx = gpxpy.parse(_file)

            if len(gpx.tracks) > 1:
                print("Something went wrong")
                help(types)
            track = gpx.tracks[0]
            if not onetype:
                gpxs.append(gpx)
            elif onetype and argv[0] in track.name:
                gpxs.append(gpx)

    print(files)

    # all_points = set()
    # poss = 0

    # for gpx in alive_it(gpxs):
    #     for segment in gpx.tracks[0].segments:
    #         for point in segment.points:
    #             poss += 1
    #             p = Point(point.longitude, point.latitude)
    #             all_points.add(p)

    # all_points = list(all_points)

    # # print(all_points)

    # plot_data = np.array(list(all_points))

    # tree = scsp.KDTree(plot_data, copy_data=True)

    # data = [all_points]

    # for i in range(0, 10):
    #     data.append([])
    #     for p in alive_it(data[i]):
    #         x = tree.query_ball_point(p.coords(), 10**(-i))
    #         if len(x) == 1:
    #             break
    #         data[i+1].append(Point(*np.mean(plot_data[x], axis=0)))

    # print(np.array(data[0]).T)

    # plt.figure(0, figsize=(6, 6))
    # for i in range(len(data)):
    #     plt.scatter(*np.array(data[i]).T, s=1)
    # # plt.scatter(*median.T, s=1, c="Red")
    # # plt.scatter(*plot_data[x].T, s=1, c="pink")
    # plt.axis("scaled")
    # plt.show()
    return


def dist(a):
    try:
        assert len(a) == 2
    except TypeError:
        raise TypeError("make sure a is an array")
    return np.sqrt(a[0]**2 + a[1]**2)


def help(types):
    print(f"Usage: {sys.argv[0]} [type]\n\tAvailable types - "
          f"{', '.join(_type for _type in types)}")
    exit()


if __name__ == "__main__":
    main(sys.argv[1:])
