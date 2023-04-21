from typing import List, Tuple
from datetime import datetime
from portal.models import Show, Theatre, Seat, Movie, Screen
import pdb

class CreateShowRequest:
    def __init__(self, movie_id: int, screen_id: int, start_time: datetime, end_time: datetime):
        self.movie_id = movie_id
        self.screen_id = screen_id
        self.start_time = start_time
        self.end_time = end_time


class GetShowRequest:
    def __init__(self, id: int):
        self.id = id


class ShowController:

    def create(self, request: CreateShowRequest) -> Show:
        movie = Movie.objects.get(id=request.movie_id)
        screen = Screen.objects.get(id=request.screen_id)

        show = Show(movie=movie, screen=screen, start_time=request.start_time, end_time=request.end_time)
        show.save()
        return show,

    def get(self, request: GetShowRequest) -> Show:
            show = Show.objects.get(id=request.id)
            return show,

