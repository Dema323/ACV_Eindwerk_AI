global str

from stop_detection import stop_points


str1 = '{['

for i in range(len(stop_points.geometry)):
    print(i)
    str2 = '{'
    str2 = str2 + '"stop_id": '
    str2 = str2 + stop_points.geometry.keys()[i]
    str2 = str2 + ',"geometry": '  
    str2 = str2 + str(stop_points.geometry[i])
    
    str2 = str2 + '}'
    print(str2)
    if i<len(stop_points.geometry)-1:
        str2 = str2 + ','
    str1 = str1 + str2
    
str1 = str1 + ']}' 





    
    
print(stop_points.geometry[1])


print(stop_points.duration_s)
print(stop_points.start_time)
print(stop_points.end_time)