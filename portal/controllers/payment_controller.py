from portal.models import Payment

class CreatePaymentRequest:
    # length in mins
    def __init__(self, price: int, external_ref_id: int):
        self.price = price
        self.external_ref_id = external_ref_id


class GetPaymentRequest:
    def __init__(self, id: int):
        self.id = id

class PaymentController:

    def createPayment(self, request: CreatePaymentRequest) -> Payment:
        payment = Payment(price=request.price,
                          external_ref_id=request.external_ref_id)
        payment.save()
        return payment,

    def getPayment(self, request: GetPaymentRequest) -> Payment:
            payment = Payment.objects.get(id=request.id)
            print(payment)
            return payment,
