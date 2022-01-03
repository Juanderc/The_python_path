#harversine formulation
#https://en.wikipedia.org/wiki/Haversine_formula
import math 
import re

def validate(f):
    def wrapper(lat1,long1,lat2,long2):
        if lat1 < 9 or lat2 < 9:
            print("Invalid latitude")
        else:
           print(len(str(long1)))
           f(lat1,long1,lat2,long2)
    return wrapper

@validate
def harversine(lat1,long1,lat2,long2):
    lat1,long1,lat2,long2 = map(math.radians, [lat1,long1,lat2,long2])
    slat = lat2 - lat1 # latitude subtraction
    slong = long2 - long1 # longitude subtraction
    R = 6372 # earth radius
    #---------Harversine--Method------
    D = (math.sin(slat/2))**2 + (math.cos(lat1)) * (math.cos(lat2)) * (math.sin(slong/2))**2
    distance = 2 * R * math.asin(math.sqrt(D))
    #---------------------------------
    #-----------Return-in-meters------
    if re.findall("^0",str(distance)): #it find an occurrency of 0
        print("metros")
        print("{} m" .format(distance * 1000))
    #----------Return-in-kilometres---
    else:
       print(len(str(long2)))
       print("{} km" .format(distance))



harversine(18.466541, -69.626654, 55.69103,37.41301)