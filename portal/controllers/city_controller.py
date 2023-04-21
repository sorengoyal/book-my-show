from portal.models import City

class CreateCityRequest:
    # length in mins
    def __init__(self, name: str):
        self.name = name


class GetCityRequest:
    # length in mins
    def __init__(self, id: int):
        self.id = id


class CityController:

    def create(self, request: CreateCityRequest) -> City:
        city = City(name=request.name)
        city.save()
        return city,

    def get(self, request: GetCityRequest) -> City:
            city = City.objects.get(id=request.id)
            return city,
