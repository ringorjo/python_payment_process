from dataclasses import dataclass

from details import details

from Enums.pay_methods import Pay_Methods


@dataclass
class Pay_Method:
    type: Pay_Methods
    details: details
