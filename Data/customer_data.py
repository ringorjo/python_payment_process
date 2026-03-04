from dataclasses import dataclass

from details import details


@dataclass
class Customer_Data:
    amount: float
    owner: str
    source: str
    description: str
    details: details
