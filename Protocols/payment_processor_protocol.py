from typing import Protocol

from payment_method_protocol import payment_method_protocol


class payment_processor_protocol(Protocol):
    def process_payment(self, payment_method: payment_method_protocol):
        """this method hanblde the payment process based a payment_method_protocol

        Args:
            payment_method (payment_method_protocol):
        """
