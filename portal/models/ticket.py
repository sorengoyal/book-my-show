from django.db import models

from portal.models.payment import Payment
from portal.models.show_seat import ShowSeat
from portal.models.user import User


class Ticket(models.Model):

    customer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    seats = models.ManyToManyField(ShowSeat)
    payments = models.ManyToManyField(Payment)
    booking_time = models.DateTimeField(auto_now=True)


    def __str__(self):
        seat_str = ''.join([str(seat) + '\n' for seat in self.seats.all()])
        payment_str = ''.join([str(payment) + '\n' for payment in self.payments.all()])
        return "[%d] %s %s\nSeats\n---------\n%s\nPayments\n--------\n%s" % (self.id, self.customer.name, self.booking_time, seat_str, payment_str)


