from faker import Faker
fake = Faker()


class Films:
    def __init__(self, title, year, movie_type, views):
        self.title = title
        self.year = year
        self.movie_type = movie_type
        self.views = views
    
    def play(self):
        return f'{self.views}' + 1
    
    def __str__(self):
        return f'{self.title}, {self.year}'

    def __repr__(self):
        return f'[{self.title}, year:{self.year}, type:{self.movie_type}]'

class Series(Films):
    def __init__(self, season_number, episod_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season_number = season_number
        self.episod_number = episod_number

    def play(self):
        return f'{self.views}' + 1
    
    def __str__(self):
        return f'{self.title}, S{self.season_number}E{self.episod_number}'
    
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
    sorted_series = []

film1 = Films(title='Gladiator', year=2000, movie_type='action', views=123)
film2 = Films(title='Red Roses', year=1994, movie_type='dramat', views=456)
film3 = Films(title='Zukazama', year=2020, movie_type='family', views=789)
film4 = Films(title='Lion king', year=2002, movie_type='animation', views=321)
film5 = Films(title='Saw', year=2005, movie_type='horror', views=654)

serial1 = Series(title='The office', year=1999, movie_type='paradocument', views=600, season_number=4, episod_number=8)
serial2 = Series(title='Breaking Bad', year=1999, movie_type='action', views=54, season_number=2, episod_number=7)
serial3 = Series(title='Paw patrol', year=1999, movie_type='scifi', views=565, season_number=1, episod_number=4)
serial4 = Series(title='Lost', year=1999, movie_type='thriller', views=676, season_number=5, episod_number=5)
serial5 = Series(title='Świat według kiepskich', year=1999, movie_type='comedy', views=878, season_number=3, episod_number=9)

films_list = [film1, film2, film3, film4, film5, serial1, serial2, serial3, serial4, serial5]

print(get_movies(films_list))

