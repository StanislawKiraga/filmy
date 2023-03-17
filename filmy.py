from faker import Faker
fake = Faker()


class Films:
    def __init__(self, title, year, movie_type):
        self.title = title
        self.year = year
        self.movie_type = movie_type

        self.views = 0
    
    def play(self, step=1):
        self.views += step
    
    def __str__(self):
        return f'{self.title}, {self.year}'

    def __repr__(self):
        return f'[{self.title}, year:{self.year}, type:{self.movie_type}]'

class Series(Films):
    def __init__(self, season_number, episod_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season_number = season_number
        self.episod_number = episod_number

    def play(self, step=1):
        self.views += step
    
    def __str__(self):
        return f'{self.title}, S{self.season_number:02}E{self.episod_number:02}'
    
    def __repr__(self):
        return f'Serial:[{self.title}, S{self.season_number:02}E{self.episod_number:02}]'
    
def get_movies(list):
    only_movies = []
    for movie in list:
        if not isinstance(movie, Series):
            only_movies.append(movie)    
            only_movies = sorted(only_movies, key=lambda movie: movie.title)       
    return only_movies

def get_series(list):
    only_series = []
    for movie in list:
        if isinstance(movie, Series):
            only_series.append(movie)
            only_series = sorted(only_series, key=lambda movie: movie.title)
    return only_series

def search(x):
    for movie in films_list:
        if movie.title == x:
            print(movie)

film1 = Films(title='Gladiator', year=2000, movie_type='action')
film2 = Films(title='Red Roses', year=1994, movie_type='dramat')
film3 = Films(title='Zukazama', year=2020, movie_type='family')
film4 = Films(title='Lion king', year=2002, movie_type='animation')
film5 = Films(title='Saw', year=2005, movie_type='horror')

serial1 = Series(title='The office', year=1999, movie_type='paradocument', season_number=4, episod_number=8)
serial2 = Series(title='Breaking Bad', year=1999, movie_type='action', season_number=2, episod_number=7)
serial3 = Series(title='Paw patrol', year=1999, movie_type='scifi', season_number=1, episod_number=4)
serial4 = Series(title='Lost', year=1999, movie_type='thriller', season_number=5, episod_number=5)
serial5 = Series(title='Świat według kiepskich', year=1999, movie_type='comedy', season_number=3, episod_number=9)

films_list = [film1, film2, film3, film4, film5, serial1, serial2, serial3, serial4, serial5]

search('Breaking Bad')

