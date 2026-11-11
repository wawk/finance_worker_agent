from dataclasses import dataclass,asdict
from datetime import date
from enum import Enum, auto
class Field(Enum):
    NAME = auto()
    AMOUNT = auto()
    DUE_DATE = auto()


@dataclass
class Bill:
    name: str
    amount: float
    due_date: date

    def to_dict(self):
        data = asdict(self)
        data["due_date"] = self.due_date.isoformat()
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            amount=data["amount"],
            due_date=date.fromisoformat(
                data["due_date"]
            )
        )
        
        
