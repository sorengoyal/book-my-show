from portal.models import Seat, City


class CreateSeatRequest:
    # length in mins
    def __init__(self, name: str, address: str, cityName: str):
        self.name = name
        self.address = address
        self.cityName = cityName


class GetSeatRequest:
    # length in mins
    def __init__(self, id: int):
        self.id = id


class SeatController:

    def create(self, request: CreateSeatRequest) -> Seat:
        city = City.objects.get(name=request.cityName)
        seat = Seat(name=request.name, address=request.address, city=city)
        seat.save()
        return seat,

    def get(self, request: GetSeatRequest) -> Seat:
            seat = Seat.objects.get(id=request.id)
            return seat,


