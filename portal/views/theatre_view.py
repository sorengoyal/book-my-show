from portal.controllers.theatre_controller import TheatreController, GetTheatreRequest
from portal.controllers.theatre_controller import CreateTheatreRequest
from django.http import HttpResponse

from django.views.generic import View
import pdb

from portal.models import Theatre


class TheatreView(View):

    theatre_controller = TheatreController()

    def post(self, request, *args, **kwargs):
        create_theatre_request = CreateTheatreRequest(request.POST["name"],
                                                  request.POST["address"],
                                                  request.POST["city"])

        theatre, = self.theatre_controller.create(create_theatre_request)
        return HttpResponse(theatre.id)

    def get(self, request, *args, **kwargs):
        # pdb.set_trace()
        get_theatre_request = GetTheatreRequest(kwargs["id"])

        theatre, = self.theatre_controller.get(get_theatre_request)
        return HttpResponse(theatre)
