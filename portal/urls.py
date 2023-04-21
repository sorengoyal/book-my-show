from django.urls import path, re_path

from portal.views.city_view import CityView
# from . import views
from portal.views.movie_view import MovieView
from portal.views.payment_view import PaymentView
from portal.views.screen_view import ScreenView
from portal.views.show_seat_view import ShowSeatView
from portal.views.show_view import ShowView
from portal.views.theatre_view import TheatreView
from portal.views.ticket_view import TicketView
from portal.views.user_view import UserView

urlpatterns = [
    path("movie/", MovieView.as_view(), name="movie-view"),
    path("movie/<int:id>", MovieView.as_view(), name="movie-view-id"),
    path("city/", CityView.as_view(), name="city-view"),
    path("city/<int:id>", CityView.as_view(), name="city-view-id"),
    path("user/", UserView.as_view(), name="user-view"),
    path("user/<int:id>", UserView.as_view(), name="user-view-id"),
    path("theatre/", TheatreView.as_view(), name="theatre-view"),
    path("theatre/<int:id>", TheatreView.as_view(), name="theatre-view-id"),
    path("screen/", ScreenView.as_view(), name="screen-view"),
    path("screen/<int:id>", ScreenView.as_view(), name="screen-view-id"),
    path("show/", ShowView.as_view(), name="show-view"),
    path("show/<int:id>", ShowView.as_view(), name="show-view-id"),
    path("show/<int:show_id>/seat/", ShowSeatView.as_view(), name="showseat-view-id"),
    path("payment/", PaymentView.as_view(), name="payment-view"),
    path("payment/<int:id>", PaymentView.as_view(), name="payment-view-id"),
    path("ticket/", TicketView.as_view(), name="ticket-view"),
    path("ticket/<int:ticket_id>", TicketView.as_view(), name="ticket-view-id"),
]