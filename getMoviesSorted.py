import sys
from getImdbRating import getImdbRating
from getMoviesFromNetflix import getMoviesFromNetflix

class Movie:
  def __init__(self, title, imdbRating):
    self.title = title
    self.imdbRating = imdbRating

def getMoviesSorted(genre):
	titles = getMoviesFromNetflix(genre)
	movies = []
	for title in titles:
		rating = getImdbRating(title)
		if (rating and rating != 'N/A'):
			movie = Movie(title, getImdbRating(title))
			movies.append(movie)
	movies.sort(key=lambda movie: movie.imdbRating, reverse=True)

	if (len(movies) >= 20):
		return movies[0:20]
	else:
		return movies

def printMoviesSorted(genre):
	for movie in getMoviesSorted(genre):
		print(movie.title + ": " + str(movie.imdbRating))

def main(argv):
	if (len(argv) == 2):
		printMoviesSorted(argv[1])
	else:
		print("Invalid Input.")

if __name__ == '__main__':
	main(sys.argv)