from pathlib import Path
import json

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
print(len(all_eq_dict))