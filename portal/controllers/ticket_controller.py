from datetime import datetime
from typing import List

from portal.exceptions.insufficient_payment_exception import InsufficientPaymentException
from portal.exceptions.seat_unavailable_exception import SeatUnavailableException
from portal.models import Ticket, ShowSeat, Payment, User


class CreateTicketRequest:
    def __init__(self, customer_id: int, seat_ids: List[int], payment_ids: List[int]):
        self.customer_id = customer_id
        self.seat_ids = seat_ids
        self.payment_ids = payment_ids


class GetTicketRequest:
    def __init__(self, id: int):
        self.id = id

class TicketController:

    def createTicket(self, request: CreateTicketRequest) -> Ticket:
        customer = User.objects.get(id=request.customer_id)
        show_seats = []
        for show_seat_id in request.seat_ids:
            show_seat = ShowSeat.objects.get(id=show_seat_id)
            if show_seat.status != ShowSeat.Status.ON_HOLD:
                raise SeatUnavailableException(show_seat)
            show_seats.append(show_seat)

        total_cost = sum([show_seat.price for show_seat in show_seats])
        payments = []
        for payment_id in request.payment_ids:
            payment = Payment.objects.get(id=payment_id)
            payments.append(payment)
        total_payment = sum([payment.price for payment in payments])
        if total_cost > total_payment:
            raise InsufficientPaymentException("Expected: $%s, Actual: $%d"%(total_cost, total_payment))

        ticket = Ticket(customer=customer, booking_time=datetime.now())
        ticket.save()
        ticket.seats.set(show_seats)
        ticket.payments.set(payments)
        ticket.save()
        for show_seat in show_seats:
            show_seat.status = ShowSeat.Status.BOOKED
            show_seat.save()
        return ticket,

    def getTicket(self, request: GetTicketRequest) -> Ticket:
            ticket = Ticket.objects.get(id=request.id)
            return ticket,
