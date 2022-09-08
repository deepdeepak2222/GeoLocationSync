# import pdb
# pdb.set_trace()
import geojson
json_file = open("countries.geojson", encoding='utf8')
data = geojson.load(json_file)
for i in data.get("features", []):
    print(i)
    break
