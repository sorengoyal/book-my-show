import json
import pdb

from portal.controllers.city_controller import CityController, GetCityRequest, CreateCityRequest
from django.http import HttpResponse

from django.views.generic import View

from portal.controllers.show_seat_controller import GetAvailableSeatsRequest, ShowSeatController, CreateShowSeatRequest, \
    GetShowSeatRequest, UpdateShowSeatRequest
from portal.models import Seat, ShowSeat


class ShowSeatView(View):

    show_seat_controller = ShowSeatController()

    def post(self, request, *args, **kwargs):
        price_map = {}
        price_map[Seat.SeatType.VIP] = request.POST["Vip_Price"]
        price_map[Seat.SeatType.GOLD] = request.POST["Gold_Price"]
        price_map[Seat.SeatType.SILVER] = request.POST["Silver_Price"]
        create_request = CreateShowSeatRequest(show_id=kwargs["show_id"],
                                              price_map=price_map)
        show_seats = self.show_seat_controller.create(create_request)
        response = ''.join([str(seat) + '\n' for seat in show_seats])
        return HttpResponse(response)

    def get(self, request, *args, **kwargs):
        if "seat_id" in kwargs:
            get_request = GetShowSeatRequest(show_id=kwargs["show_id"], seat_id=kwargs["seat_id"])
            show_seat = self.show_seat_controller.getShowSeatRequest(get_request)
            return HttpResponse(show_seat)
        else:
            get_request = GetAvailableSeatsRequest(kwargs["show_id"])
            seats, = self.show_seat_controller.getAvailableSeats(get_request)
            response = ''.join([str(seat)+'\n' for seat in seats])
            return HttpResponse(response)

    def put(self, request, *args, **kwargs):
        params = json.loads(request.body)
        status = ShowSeat.Status[params["status"]]
        request = UpdateShowSeatRequest(show_id=kwargs["show_id"], show_seat_ids=params["seats"], status=status)
        seats, = self.show_seat_controller.update(request)
        response = ''.join([str(seat) + '\n' for seat in seats])
        return HttpResponse(response)