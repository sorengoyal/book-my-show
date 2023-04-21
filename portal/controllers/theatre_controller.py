from portal.models import Theatre, City


class CreateTheatreRequest:
    # length in mins
    def __init__(self, name: str, address: str, cityName: str):
        self.name = name
        self.address = address
        self.cityName = cityName


class GetTheatreRequest:
    # length in mins
    def __init__(self, id: int):
        self.id = id


class TheatreController:

    def create(self, request: CreateTheatreRequest) -> Theatre:
        city = City.objects.get(name=request.cityName)
        theatre = Theatre(name=request.name, address=request.address, city=city)
        theatre.save()
        return theatre,

    def get(self, request: GetTheatreRequest) -> Theatre:
            theatre = Theatre.objects.get(id=request.id)
            return theatre,


