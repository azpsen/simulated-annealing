import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt


def create_singlepoint_gdf(coords):
    lat = coords[0]
    long = coords[1]
    df = pd.DataFrame({
        'Latitude': [lat],
        'Longitude': [long],
    })
    geometry = [Point(long, lat)]
    return gpd.GeoDataFrame(df, geometry=geometry, crs=4326)


def create_multipoint_gdf(coord_list):
    data = {'Label': [], 'Latitude': [], 'Longitude': []}
    for i in range(len(coord_list)):
        if i == 0:
            data['Label'].append("Start")
        elif i == len(coord_list) - 1:
            data['Label'].append("Finish")
        else:
            data['Label'].append("")
        data['Latitude'].append(coord_list[i][0])
        data['Longitude'].append(coord_list[i][1])

    df = pd.DataFrame.from_dict(data)

    df['coordinates'] = df[['Longitude', 'Latitude']].values.tolist()

    # Change the coordinates to a geoPoint
    df['coordinates'] = df['coordinates'].apply(Point)

    geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
    return gpd.GeoDataFrame(df, geometry=geometry, crs=4326)


def create_point_label(gdf, text, color, size, offset):
    gdf.plot(marker='o', color=color, markersize=size, ax=plt.gca())

    offset_coords = [0, 0]
    if offset == 'down':
        offset_coords = [7, -14]
    elif offset == 'up':
        offset_coords = [7, 14]

    for _, row in gdf.iterrows():
        plt.annotate(
            text=text,
            xy=[row.geometry.x, row.geometry.y],
            xytext=offset_coords,
            textcoords="offset points",
            bbox=dict(boxstyle='round', fc='black', lw=2, alpha=0.8),
        )


def plot_point(coords, text, color, size, offset='down'):
    gdf = create_singlepoint_gdf(coords)
    create_point_label(gdf, text, color, size, offset)


def visualize(sln, goal):

    # Style the plot
    plt.style.use('dark_background')
    plt.rcParams["figure.figsize"] = (10, 10)

    # Plot map of Minnesota
    usa = gpd.read_file('gis/states.shp')
    usa[usa.STATE_ABBR == 'MN'].plot(edgecolor='white', color='dimgrey')

    # Plot solution path
    gdf = create_multipoint_gdf(sln)
    gdf.plot(marker='o', cmap='winter', markersize=5, ax=plt.gca())

    # Plot start, end, and goal with labels
    plot_point(sln[0], "Start", 'red', 10)
    plot_point(goal, "Goal", 'red', 10)
    plot_point(sln[-1], "End", 'red', 10, offset='up')

    plt.title("Minnesota")
    plt.show()
