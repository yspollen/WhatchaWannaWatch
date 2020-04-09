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
		if (rating):
			movie = Movie(title, getImdbRating(title))
			movies.append(movie)
	movies.sort(key=lambda movie: movie.imdbRating, reverse=True)
	return movies

def printMoviesSorted(genre):
	for movie in getMoviesSorted(genre):
		print(movie.title + ": " + str(movie.imdbRating))

def main(argv):
	printMoviesSorted(argv[1])

main(sys.argv)
