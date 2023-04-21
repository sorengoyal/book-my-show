from portal.controllers.screen_controller import ScreenController, GetScreenRequest
from portal.controllers.screen_controller import CreateScreenRequest
from django.http import HttpResponse

from django.views.generic import View

from portal.models import Screen


class ScreenView(View):

    screen_controller = ScreenController()

    def post(self, request, *args, **kwargs):
        feature = request.POST["feature"] if "feature" in request.POST else None
        create_screen_request = CreateScreenRequest(request.POST["name"],
                                                    request.POST["theatre"],
                                                    feature,
                                                    request.POST["seat_layout"])

        screen, seat_ids = self.screen_controller.create(create_screen_request)
        return HttpResponse(screen.id, seat_ids)

    def get(self, request, *args, **kwargs):
        get_screen_request = GetScreenRequest(kwargs["id"])

        screen, seats = self.screen_controller.get(get_screen_request)
        seat_str = ''.join([str(seat)+'\n' for seat in seats])
        response = "Screen: %s\nSeats:\n%s" % (screen, seat_str)
        return HttpResponse(response)

