import requests
from bs4 import BeautifulSoup

def getMoviesFromNetflix(genre):
	# request URL
	url = 'https://www.netflix.com/browse/genre/'
	
	if (genre == 'all'):
		pass
	elif (genre == 'action'):
		url += '1365?bc='
	elif (genre == 'children'):
		url += '783?bc='
	elif (genre == 'classics'):
		url += '31574?bc='
	elif (genre == 'comedies'):
		url += '6548?bc='
	elif (genre == 'dramas'):
		url += '5763?bc='
	elif (genre == 'faith'):
		url += '26835?bc='
	elif (genre == 'horror'):
		url += '8711?bc='
	elif (genre == 'musicals'):
		url += '52852?bc='
	elif (genre == 'romantic'):
		url += '8883?bc='
	elif (genre == 'scifi'):
		url += '1492?bc='
	elif (genre == 'sports'):
		url += '4370?bc='
	elif (genre == 'standup'):
		url += '11559?bc='
	elif (genre == 'thriller'):
		url += '8933?bc='
	else:
		print("Invalid Genre.")
		return []

	url += '34399'

	# GET response
	r = requests.get(url)

	# Parse HTML response
	soup = BeautifulSoup(r.content, 'html.parser')
	rows = soup.find_all('a')
	titles = []
	for row in rows:
		titles.append(row.text)

	# Remove Duplicates
	titles = list(dict.fromkeys(titles))

	# Retrieve 100 entries if 'all' genre
	if (genre == 'all'):
		if (len(titles) >= 103):
			return titles[3:103]
		else:
			return titles[3:]

	# Retrieve 50 entries if all other genres
	if (len(titles) >= 53):
		return titles[3:53]
	else:
		return titles[3:]