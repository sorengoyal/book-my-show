from typing import List, Dict, Tuple

from portal.models import City, Seat, Show, ShowSeat


class GetAvailableSeatsRequest:
    def __init__(self, show_id: int):
        self.show_id = show_id

class GetShowSeatRequest:
    def __init__(self,show_id: int, seat_id: int):
        self.show_id = show_id
        self.seat_id = seat_id

class BookSeatsRequest:
    def __init__(self, show_id: int, seat_ids: List[int]):
        self.show_id = show_id
        self.seat_ids = seat_ids

class CreateShowSeatRequest:
    def __init__(self, show_id: int, price_map: Dict[ShowSeat.Status, int]):
        self.show_id = show_id
        self.price_map = price_map

class UpdateShowSeatRequest:
    def __init__(self, show_id: int, show_seat_ids: List[int], status: ShowSeat.Status):
        self.show_id = show_id
        self.show_seat_ids = show_seat_ids
        self.status = status

class ShowSeatController:

    def getAvailableSeats(self, request: GetAvailableSeatsRequest) -> List[Seat]:
        show = Show.objects.get(id=request.show_id)
        available_show_seats = ShowSeat.objects.filter(show=show, status=ShowSeat.Status.AVAILABLE)
        return available_show_seats,

    def getShowSeat(self, request: GetShowSeatRequest):
        show = Show.objects.get(id=request.show_id)
        seat = Seat.objects.get(id=request.seat_id)
        show_seat = ShowSeat.objects.get(show=show, seat=seat)
        return show_seat

    def create(self, request: CreateShowSeatRequest):
        show = Show.objects.get(id=request.show_id)
        seats = Seat.objects.filter(screen=show.screen)
        for seat in seats:
            type = seat.type
            price = request.price_map[type]
            show_seat = ShowSeat(show=show, seat=seat, price=price, status=ShowSeat.Status.AVAILABLE)
            show_seat.save()
        available_seats = ShowSeat.objects.filter(show=show, status=ShowSeat.Status.AVAILABLE)
        return available_seats

    def bookSeats(self, request: BookSeatsRequest):
        show = Show.objects.get(id=request.show_id)
        for id in request.seat_ids:
            showSeat = ShowSeat(show=show, )

    def update(self, request: UpdateShowSeatRequest):
        show = Show.objects.get(id=request.show_id)
        for show_seat_id in request.show_seat_ids:
            show_seat = ShowSeat.objects.get(id=show_seat_id)
            show_seat.status = request.status
            show_seat.save()
        available_seats = ShowSeat.objects.filter(show=show)
        return available_seats,


