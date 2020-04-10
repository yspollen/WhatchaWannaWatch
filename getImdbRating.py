import requests
from apikey import apikey

def getImdbRating(movie):
	url = 'http://www.omdbapi.com/?apikey=' + apikey + '&t=' + movie
	r = requests.get(url)
	try:
		return r.json()["imdbRating"]
	except:
		print("movie not found: " + movie)
		pass