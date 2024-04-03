# Cycling Project
(2019 - now)
This project aims to be able to load gpx files from runkeeper and generate a heatmap.
The data is expected to be in `.gpx` format inside a `Data/` folder as well as a `Data_Runkeeper-correction/` folder which contains corrected files in `Data_Runkeeper-correction/*/merged/`

The project is however quite complex due to the large amount of GPX files which contain lots of GPS data points. The current plan is the following:
- Load the files
- Generate a network grid
- Look how many times a connection exists on a network connection
- Create heatmap
