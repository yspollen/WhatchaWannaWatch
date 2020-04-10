import requests

def getMoviesFromNetflix(genre):
	url = 'https://www.netflix.com/browse/genre/'
	if (genre == 'action'):
		url += '1365?bc='
	#elif (genre == 'anime'):
	#	url += '3063?bc='
	elif (genre == 'children'):
		url += '783?bc='
	elif (genre == 'classics'):
		url += '31574?bc='
	elif (genre == 'comedies'):
		url += '6548?bc='
	#elif (genre == 'crime'):
	#	url += '5824?bc='
	#elif (genre == 'cult'):
		#url += '7627?bc='
	#elif (genre == 'documentary'):
		#url += '2243108?bc='
	elif (genre == 'dramas'):
		url += '5763?bc='
	elif (genre == 'faith'):
		url += '26835?bc='
	#elif (genre == 'history'):
	#	url += '81268388?bc='
	elif (genre == 'horror'):
		url += '8711?bc='
	#elif (genre == 'independent'):
	#	url += '7077?bc='
	#elif (genre == 'international'):
	#	url += '78367?bc='
	#elif (genre == 'LGBTQ'):
	#	url += '5977?bc='
	elif (genre == 'musicals'):
		url += '52852?bc='
	elif (genre == 'romantic'):
		url += '8883?bc='
	elif (genre == 'scifi'):
		url += '1492?bc='
	#elif (genre == 'nature'):
	#	url += '2595?bc='
	elif (genre == 'sports'):
		url += '4370?bc='
	elif (genre == 'standup'):
		url += '11559?bc='
	elif (genre == 'thriller'):
		url += '8933?bc='
	elif (genre == 'all'):
		pass
	else:
		print("Invalid Genre.")
		return []

	url += '34399'

	r = requests.get(url)

	from bs4 import BeautifulSoup

	soup = BeautifulSoup(r.content, 'html.parser')
	rows = soup.find_all('a')
	titles = []
	for row in rows:
		titles.append(row.text)
	return titles[3:33]