import googlemaps
from _datetime import datetime
import geopy
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='cogs_108_final_project')

location = geolocator.geocode("4122 Via Candidiz")

print(location.address)

print(location.longitude, location.latitude)