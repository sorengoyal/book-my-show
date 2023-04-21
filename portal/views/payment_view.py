import json

from portal.controllers.payment_controller import PaymentController, GetPaymentRequest
from portal.controllers.payment_controller import CreatePaymentRequest
from django.http import HttpResponse

from django.views.generic import View
import pdb


class PaymentView(View):

    payment_controller = PaymentController()

    def post(self, request, *args, **kwargs):
        params = json.loads(request.body)
        create_payment_request = CreatePaymentRequest(params["price"],
                                                  params["external_ref_id"])

        payment, = self.payment_controller.createPayment(create_payment_request)
        return HttpResponse(payment)

    def get(self, request, *args, **kwargs):
        get_payment_request = GetPaymentRequest(kwargs["id"])

        payment, = self.payment_controller.getPayment(get_payment_request)
        return HttpResponse(payment)
