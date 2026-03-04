from email.mime.text import MIMEText

from Data.customer_data import Customer_Data
from Protocols.notifier_protocol import notifier


class email_notifier(notifier):
    def notify(self, custumer_data: Customer_Data):
        try:
            email = custumer_data.details.key
            if not email == "email":
                raise Exception("no exist email value for this customer_data")
            msg = MIMEText(f"{custumer_data.owner}, Thank you for your payment.")
            msg["Subject"] = "Payment Confirmation"
            msg["From"] = "no-reply@example.com"
            msg["To"] = custumer_data.details.value
            print("Email send to ")
        except Exception as e:
            print(f"Error: {e}")


"""

{
  "amount": 100.0,
  "owner": "Jonathan Rincon",
  "source": "tarjeta",
  "descripcion": "Curso de Patrones de Diseño",
  "details": {
    "email": "jonathan@dev.com"
  }
}


        """
