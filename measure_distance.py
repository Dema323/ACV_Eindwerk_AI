from geopy import distance


point = (50.8478771, 4.726232)

store_locations = [(50.8478639, 4.7262517),(50.84696484358569, 4.730871603704232),(50.849980486968384, 4.722730513569958)]
visited_stores = []

for store in store_locations:
    points_distance = distance.distance(store, point).meters
    if(points_distance < 5):
        print(store, points_distance)
        visited_stores.append(store)
        #print(store)