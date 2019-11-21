import googlemaps
import json
import pandas as pd

key = 'AIzaSyCTVn4TU6dUwegavg0UQRL_BAoi4Hqhp88'
gmaps = googlemaps.Client(key=key)

geocode_result = gmaps.geocode('81732 Lido Ave, Indio, CA')

geo_json = geocode_result.json()
print(geocode_result)

google_df = pd.DataFrame(geocode_result)

print(google_df['geometry'])
