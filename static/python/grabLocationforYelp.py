"""
Created by: 
Leon Chen

We can get the user's location, longitude and latitude via this application. From there,
we will import the data into the yelp API.
"""

while True:
	from geopy.geocoders import Nominatim
	try:
		userLoc = input("Where are you? Give a rough estimate of your address. ")
		location = Nominatim()
		whereamI = location.geocode(userLoc)
		print(whereamI.address)
		break
	except:
		print("Sorry, try again with a different address.")
		continue
