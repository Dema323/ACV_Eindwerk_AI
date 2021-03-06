import json
from datetime import datetime

with open('data.json',"r") as infile, open('output.json',"w") as outfile:
    outfile.write('{ "gps" : ')
    for line in infile:
        line = line.replace("\\", "")
        line = line.replace('"[', "[")
        line = line.replace(']"', "]")
        outfile.write(line)
    outfile.write("}")

f = open('output.json',)
data = json.load(f)


points_list = []

for point in data['gps']:
    timestamp = point['timestamp']
    #print(timestamp)
    latitude = point['coords']['latitude']
    #print(latitude)
    longitude = point['coords']['longitude']
    #print(longitude)
    speed = point['coords']['speed']
    #print(speed)
    point_list = [timestamp, latitude, longitude, speed]
    points_list.append(point_list)

for x in points_list:
    print(x)


with open('output.geojson',"w") as outfile:
    outfile.write('{' + '\n' + '"type": "FeatureCollection",' + '\n'
    + '"name": "testdata_geolife2",' + '\n'
    + '"crs": { "type": "output", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },' + '\n'
    + '"features": [' + '\n')
    i = 1
    for x in points_list:
        c_timestamp = int(str(x[0])[:-3])
        dt_object = datetime.fromtimestamp(c_timestamp)
        outfile.write('{ "type": "Feature", "properties": { "id": '+ str(i) + ', "sequence": ' + str(i) + ', "trajectory_id": 1, "tracker": 19, "t": "'+ str(dt_object) + '+00" }, "geometry": { "type": "Point", "coordinates": [ ' + str(x[2]) + ', '+ str(x[1]) + ' ] } },' + '\n')
        i= i+1
    outfile.write(']' + '\n'
        + '}' + '\n')
