from portal.models import Movie

class CreateMovieRequest:
    # length in mins
    def __init__(self, name: str, director: str, length: int):
        self.name = name
        self.director = director
        self.length = length


class GetMovieRequest:
    def __init__(self, id: int):
        self.id = id

class MovieController:

    def createMovie(self, request: CreateMovieRequest) -> Movie:
        movie = Movie(name=request.name,
                      director=request.director,
                      length=request.length)
        movie.save()
        return movie,

    def getMovie(self, request: GetMovieRequest) -> Movie:
            movie = Movie.objects.get(id=request.id)
            print(movie)
            return movie,
