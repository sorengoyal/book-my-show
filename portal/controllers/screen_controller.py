from typing import List, Tuple

from portal.models import Screen, Theatre, Seat
import pdb

class CreateScreenRequest:
    # length in mins
    def __init__(self, name: str, theatreName: str, feature: str, seat_layout: List[Tuple[int,int,str]]):
        self.name = name
        self.theatreName = theatreName
        self.feature = Screen.Feature(feature) if feature else Screen.Feature.NONE
        self.seat_layout = seat_layout


class GetScreenRequest:
    # length in mins
    def __init__(self, id: int):
        self.id = id


class ScreenController:

    def create(self, request: CreateScreenRequest) -> Screen:
        theatre = Theatre.objects.get(name=request.theatreName)
        screen = Screen(name=request.name, theatre=theatre, feature=request.feature)
        screen.save()
        seat_ids = []
        seat_layout = self.parseSeatLayout(request.seat_layout)
        for row, col, type in seat_layout:
            seat_type = Seat.SeatType(type)
            seat_record = Seat(row=row,col=col,type=seat_type, screen=screen)
            seat_record.save()
            seat_ids.append(seat_record.id)
        return screen, seat_ids,

    def get(self, request: GetScreenRequest) -> Screen:
            screen = Screen.objects.get(id=request.id)
            seats = Seat.objects.filter(screen=screen)
            return screen, list(seats)


    def parseSeatLayout(self, input: str) -> List[Tuple[int, int, Seat.SeatType]]:
        rows = input.split(',')
        seat_layout = []
        for row in rows:
            str_vals = row.split(' ')
            # pdb.set_trace()
            row, col, type = int(str_vals[0]), int(str_vals[1]), Seat.SeatType(str_vals[2])
            seat_layout.append((row, col, type))

        return seat_layout