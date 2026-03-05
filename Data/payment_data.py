from dataclasses import dataclass

from Data.pay_method import Pay_Method


@dataclass
class Payment_Data:
    amount: float
    owner: str
    description: str
    pay_method: Pay_Method
