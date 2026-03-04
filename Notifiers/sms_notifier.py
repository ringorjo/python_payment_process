from dataclasses import dataclass

from Data.customer_data import Customer_Data
from Protocols.notifier_protocol import notifier


@dataclass
class sms_notifier(notifier):
    sms: str

    def notify(self, custumer_data: Customer_Data):
        try:
            phone_key = custumer_data.details.key
            if not phone_key.lower() == "phone":
                raise Exception("no exist phone value for this customer_data")
            print(
                f"Send sms: {self.sms} To: {custumer_data.details.value} Description : {custumer_data.owner} thanks for your payment"
            )
        except Exception as e:
            print(f"Error: {e}")
