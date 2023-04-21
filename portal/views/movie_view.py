import json

from portal.controllers.movie_controller import MovieController, GetMovieRequest
from portal.controllers.movie_controller import CreateMovieRequest
from django.http import HttpResponse

from django.views.generic import View
import pdb


class MovieView(View):

    movie_controller = MovieController()

    def post(self, request, *args, **kwargs):
        params = json.loads(request.body)
        create_movie_request = CreateMovieRequest(params["name"],
                                                  params["director"],
                                                  params["length"])

        movie, = self.movie_controller.createMovie(create_movie_request)
        return HttpResponse(movie)

    def get(self, request, *args, **kwargs):
        # pdb.set_trace()
        get_movie_request = GetMovieRequest(kwargs["id"])

        movie, = self.movie_controller.getMovie(get_movie_request)
        return HttpResponse(movie)
