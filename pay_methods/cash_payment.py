from dataclasses import dataclass

from Data.payment_data import Payment_Data
from Enums.pay_methods import Pay_Methods
from Protocols.payment_method_protocol import payment_method_protocol


@dataclass
class cash_payment(payment_method_protocol):
    pay_method: Pay_Methods = Pay_Methods.CASH

    def is_valid(self, payment_data: Payment_Data) -> bool:
        return True
