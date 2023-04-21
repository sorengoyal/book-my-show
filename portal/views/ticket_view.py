import json

from portal.controllers.ticket_controller import TicketController, GetTicketRequest
from portal.controllers.ticket_controller import CreateTicketRequest
from django.http import HttpResponse

from django.views.generic import View
import pdb

from portal.exceptions.insufficient_payment_exception import InsufficientPaymentException
from portal.exceptions.seat_unavailable_exception import SeatUnavailableException


class TicketView(View):

    ticket_controller = TicketController()

    def post(self, request, *args, **kwargs):
        params = json.loads(request.body)
        create_ticket_request = CreateTicketRequest(params["customer_id"],
                                                  params["seat_ids"],
                                                  params["payment_ids"])
        try:
            ticket, = self.ticket_controller.createTicket(create_ticket_request)
        except (InsufficientPaymentException, SeatUnavailableException) as e:
            return HttpResponse(e, status=500)

        return HttpResponse(ticket)

    def get(self, request, *args, **kwargs):
        get_ticket_request = GetTicketRequest(kwargs["ticket_id"])

        ticket, = self.ticket_controller.getTicket(get_ticket_request)
        return HttpResponse(ticket)
