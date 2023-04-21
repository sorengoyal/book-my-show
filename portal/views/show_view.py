from portal.controllers.show_controller import ShowController, GetShowRequest
from portal.controllers.show_controller import CreateShowRequest
from django.http import HttpResponse
from django.views.generic import View
from datetime import datetime


class ShowView(View):

    show_controller = ShowController()

    def post(self, request, *args, **kwargs):

        create_show_request = CreateShowRequest(request.POST["movie_id"],
                                                    request.POST["screen_id"],
                                                    datetime.fromisoformat(request.POST["start_time"]),
                                                    datetime.fromisoformat(request.POST["end_time"]))

        show, = self.show_controller.create(create_show_request)
        return HttpResponse(show)

    def get(self, request, *args, **kwargs):
        get_show_request = GetShowRequest(kwargs["id"])
        show, = self.show_controller.get(get_show_request)
        return HttpResponse(show)

