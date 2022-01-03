from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Harversine")
location = geolocator.geocode("New Your")
print(location.address)
print(location.latitude,location.longitude)