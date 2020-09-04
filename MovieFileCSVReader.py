import csv
from Movie import Movie
from Actor import Actor
from Director import Director
from Genre import Genre


class MovieFileCSVReader:
    def __init__(self, file_name):
        self._file_name = file_name
        self.dataset_of_movies = set([])
        self.dataset_of_actors = set([])
        self.dataset_of_directors = set([])
        self.dataset_of_genres = set([])


    def read_csv_file(self):
        with open(self._file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            for row in movie_file_reader:
                # Title Add
                title = row['Title']
                release_year = int(row['Year'])
                new_movie = Movie(title, release_year)
                self.dataset_of_movies.add(new_movie)


                # Actor Add
                actors = row['Actors']
                actors_list = actors.split(",")
                for people in actors_list:
                    new_actor = Actor(people.strip())
                    if new_actor not in self.dataset_of_actors:
                        self.dataset_of_actors.add(new_actor)

                # Director Add
                director = row['Director']
                new_director = Director(director)
                if new_director not in self.dataset_of_directors:
                    self.dataset_of_directors.add(new_director)

                # Genre Add
                genre = row['Genre']
                genre_list = genre.split(",")
                for g in genre_list:
                    new_genre = Genre(g.strip())
                    if new_genre not in self.dataset_of_genres:
                        self.dataset_of_genres.add(new_genre)


filename = 'Data1000Movies.csv'
movie_file_reader = MovieFileCSVReader(filename)
movie_file_reader.read_csv_file()

print(f'number of unique movies: {len(movie_file_reader.dataset_of_movies)}')
print(f'number of unique actors: {len(movie_file_reader.dataset_of_actors)}')
print(f'number of unique directors: {len(movie_file_reader.dataset_of_directors)}')
print(f'number of unique genres: {len(movie_file_reader.dataset_of_genres)}')


movie = Movie("A", 1960)

movie2 = Movie("B", 1960)

movie3 = Movie("C", 2017)

movie4 = Movie("A", 2016)

list1 = [movie, movie2, movie3, movie4]

print(list1)
