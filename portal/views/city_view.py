from portal.controllers.city_controller import CityController, GetCityRequest, CreateCityRequest
from django.http import HttpResponse

from django.views.generic import View


class CityView(View):

    city_controller = CityController()

    def post(self, request, *args, **kwargs):
        create_request = CreateCityRequest(request.POST["name"])

        city, = self.city_controller.create(create_request)
        return HttpResponse(city.id)

    def get(self, request, *args, **kwargs):
        get_request = GetCityRequest(kwargs["id"])

        city, = self.city_controller.get(get_request)
        return HttpResponse(city)
