from dataclasses import dataclass
from typing import Protocol

from Data.payment_data import Payment_Data
from Enums.pay_methods import Pay_Methods


@dataclass
class payment_method_protocol(Protocol):
    pay_method: Pay_Methods

    def is_valid(self, payment_data: Payment_Data) -> bool:
        """This method validate the payment method  based on the payment_data

        Args:
            payment_data (dict[str,str]): the payment_data
        """
