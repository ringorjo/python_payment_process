from typing import Protocol


class payment_method_protocol(Protocol):
    def create_payment(self, payment_data: dict[str, str]):
        """This method handle the payment creation  based on the payment_data

        Args:
            payment_data (dict[str,str]): the payment_data
        """
