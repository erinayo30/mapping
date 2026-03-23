from pathlib import Path
import json

import plotly.express as px
import plotly.io as pio


pio.renderers.default='browser'

# Read data as a string and convert to a python object
path = Path('eq_data/eq_data_1_day_m1.geojson')
contents= path.read_text(encoding='utf-8', errors='ignore')
all_eq_data = json.loads(contents)

# create a readable version of the data file
path= Path("eq_data/readable_eq_data.geojson")
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# print(contents[:1000])
# Examine all earthquakes in the dataset
all_eq_dict =all_eq_data['features']
# print(len(all_eq_dict))
mags, lons, lats =[], [], []
for eq_dict in all_eq_dict:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

title ="Global Earthquake"
fig= px.scatter_geo(lat=lats, lon=lons, title=title)
fig.show()
# fig.write_image("earthquake_map.html")
    # print(mags[:10])
    # print(lons[:5])
    # print(lats[:5])
    #
