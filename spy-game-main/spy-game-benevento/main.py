from gps_class import GPSVis


vis = GPSVis(
    # <--- data file with GSM positions (change only this row)
    data_path=5,
    locations="data-locations.csv",                 # restaurants and residences
    # Map downloaded from OSM (https://www.openstreetmap.org/export)
    map_path="map.png",
    # Two coordinates of the map (upper left, lower right)
    points=(41.1379, 14.7673, 41.116113, 14.803)
)

# Set the color and the width of the GNSS tracks.
vis.create_image(color=(0, 0, 255), width=5)
vis.plot_map(output='save')

# print()
