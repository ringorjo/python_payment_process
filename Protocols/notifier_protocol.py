from typing import Protocol

from Data.customer_data import Customer_Data


class notifier(Protocol):
    def notify(self, custumer_data: Customer_Data):
        """Method used for handle notication Order

        Args:
            custumer_data (dict[str,str]): the customer data info
        """
