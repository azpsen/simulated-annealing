from fitness import FitnessFunction
from annealing import Annealer

import scheduler
import successor

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt


fitness_func = FitnessFunction()
ksc_coords = (46.81819372475244, -92.08550938909693)

eagle_mtn = (47.897391, -90.560111)

# schedule_func = scheduler.ExponentialScheduler(20, 0.005, 100)
schedule_func = scheduler.LinearScheduler(40, 0.005, 100)

successor_func = successor.GaussianSuccessorFunction(0.25)

a = Annealer(ksc_coords, fitness_func, schedule_func, successor_func)
sln = a.anneal(get_list=True)

print(f"Found {sln[-1]} at height {fitness_func(sln[-1])}")
print(f"Goal is {eagle_mtn} at height {fitness_func(eagle_mtn)}")

data = {'Label': [], 'Latitude': [], 'Longitude': []}
for i in range(len(sln)):
    if i == 0: data['Label'].append("Start")
    elif i == len(sln) - 1: data['Label'].append("Finish")
    else: data['Label'].append("")
    data['Latitude'].append(sln[i][0])
    data['Longitude'].append(sln[i][1])

df = pd.DataFrame.from_dict(data)

df['coordinates'] = df[['Longitude', 'Latitude']].values.tolist()

# Change the coordinates to a geoPoint
df['coordinates'] = df['coordinates'].apply(Point)

start_df = pd.DataFrame({
    'Latitude': [ksc_coords[0]],
    'Longitude': [ksc_coords[1]],
})

end_df = pd.DataFrame({
    'Latitude': [sln[-1][0]],
    'Longitude': [sln[-1][1]],
})

geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs=4326)

start_geometry = [Point(xy) for xy in zip(start_df['Longitude'], start_df['Latitude'])]
start_gdf = gpd.GeoDataFrame(start_df, geometry=start_geometry, crs=4326)

end_geometry = [Point(xy) for xy in zip(end_df['Longitude'], end_df['Latitude'])]
end_gdf = gpd.GeoDataFrame(end_df, geometry=end_geometry, crs=4326)


usa = gpd.read_file('gis/states.shp')
u = usa[usa.STATE_ABBR == 'MN'].plot()

gdf.plot(marker='o', cmap='Greens', markersize=5, ax=plt.gca())
start_plot = start_gdf.plot(marker='o', color='violet', markersize=10, ax=plt.gca())
end_plot = end_gdf.plot(marker='o', color='red', markersize=10, ax=plt.gca())

for _, row in start_gdf.iterrows():
    plt.annotate(
        text="Start",
        xy=[row.geometry.x, row.geometry.y],
        xytext=[7, -14],
        textcoords="offset points",
        bbox=dict(boxstyle='round', fc='w', lw=2, alpha=0.8),
    )

for _, row in end_gdf.iterrows():
    plt.annotate(
        text="End",
        xy=[row.geometry.x, row.geometry.y],
        xytext=[7, -14],
        textcoords="offset points",
        bbox = dict(boxstyle='round', fc='w', lw=2, alpha=0.8),
    )

# for x, y, label in zip(df.geometry.x, df.geometry.y, df.label):
#     pl.annotate(label, xy=(x, y), xytext=(3, 3), textcoords="offset points")

plt.title("Minnesota")
plt.show()