import json
from geopy import distance


coordinates_pure_lunchbar = (4.7301912, 50.8469991)
UCLL = (4.726474, 50.8479709)
point = (4.7305265, 50.8506929)




# The integer refernces to the type of stoppoint this coordinate is
# restaurant = 1
# delivery_point = 2
# stop_light = 3

append_resto = 1
delivery_point_data = 2
stop_light_data = 3



# with open('data/result.json', "r") as infile, open('data/result_labeled.json', "w") as outfile:
#     file_data = open('data/result.json')
#     data = json.load(file_data)
#
    # for features in data['features']:
    #     coordinate = features['geometry']['coordinates']
    #     points_distance = distance.distance(point, coordinate).meters
    #     if (points_distance < 5):
    #         print(coordinate, points_distance)
#             date.append(append_resto)
print("iets")

def add_label(filename='data/result.json'):
    with open(filename, 'r+') as file:
        print("jelo")
        file_data = json.load(file)
        for features in file_data['features']:
            coordinate = features['geometry']['coordinates']
            print(coordinate)
            points_distance = distance.distance(coordinates_pure_lunchbar, coordinate).meters
            print(points_distance)
            if (points_distance < 20):
                print(coordinate, points_distance)
                features['type']=append_resto

            points_distance = distance.distance(UCLL, coordinate).meters
            if (points_distance < 20):
                print(coordinate, points_distance)
                features['type']=delivery_point_data

        file.seek(0)
        json.dump(file_data, file, indent=4)

add_label()
