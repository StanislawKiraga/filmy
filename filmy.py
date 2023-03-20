from faker import Faker
fake = Faker()
from datetime import date
import random
from functools import wraps

class Film:
    def __init__(self, title, year, movie_type):
        self.title = title
        self.year = year
        self.movie_type = movie_type

        self.nr_view = random.randint(1, 1000)

    def play(self, step=1):
        self.nr_view += step
        
    
    def __str__(self):
        return f'{self.title}, {self.year}'

    def __repr__(self):
        return f'[{self.title}, year:{self.year}, type:{self.movie_type}, view:{self.nr_view}]'
    
class Serie(Film):
    def __init__(self, season_number, episod_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season_number = season_number
        self.episod_number = episod_number
    
    def __str__(self):
        return f'{self.title}, S{self.season_number:02}E{self.episod_number:02}'
    
    def __repr__(self):
        return f'Serial:[{self.title}, S{self.season_number:02}E{self.episod_number:02}, view:{self.nr_view}]'
    

film1 = Film(title='Gladiator', year=2000, movie_type='action')
film2 = Film(title='Red Roses', year=1994, movie_type='dramat')
film3 = Film(title='Zukazama', year=2020, movie_type='family')
film4 = Film(title='Lion king', year=2002, movie_type='animation')
film5 = Film(title='Saw', year=2005, movie_type='horror')

serial1 = Serie(title='The office', year=1999, movie_type='paradocument', season_number=4, episod_number=8)
serial2 = Serie(title='Breaking Bad', year=1999, movie_type='action', season_number=2, episod_number=7)
serial3 = Serie(title='Paw patrol', year=1999, movie_type='scifi', season_number=1, episod_number=4)
serial4 = Serie(title='Lost', year=1999, movie_type='thriller', season_number=5, episod_number=5)
serial5 = Serie(title='Świat według kiepskich', year=1999, movie_type='comedy', season_number=3, episod_number=9)

films_list = [film1, film2, film3, film4, film5, serial1, serial2, serial3, serial4, serial5]

def get_movies():
    only_movies = []
    for movie in films_list:
        if not isinstance(movie, Serie):
            only_movies.append(movie)    
            only_movies = sorted(only_movies, key=lambda movie: movie.title)       
    return only_movies

def get_series(list):
    only_series = []
    for movie in list:
        if isinstance(movie, Serie):
            only_series.append(movie)
            only_series = sorted(only_series, key=lambda movie: movie.title)
    return only_series

def search(x):
    for movie in films_list:
        if movie.title == x:
            print(movie)

def generate_10_times():
    for i in range(10):
        print(generate_views())
    
def generate_views(x=random.randint(1, 100)):
    return f'{random.choice(films_list)}, Views:{x}'

def top_title(x=0):
    tops = [film for film in sorted(films_list, key=lambda movie: movie.nr_view, reverse=True)]
    return tops[:x]


if __name__ == "__main__":
    print('Biblioteka filmów')
    print(50 * '-')
    print(films_list)
    print(50 * '-')
    print(f'Najpopularniejsze filmy i seriale dnia {date.today():%d-%m-%Y}:')
    for top in top_title(3):
        print(f'{top.title}, Views:{top.nr_view}')

        
