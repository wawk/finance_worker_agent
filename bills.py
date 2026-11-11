import json
from bill import Bill, Field
from  typing import Any

class Bills:
    def __init__(self):
        self._bills = {}

    def add_bill(self, bill):
        self._bills[bill.name] = bill

    def remove_bill(self, bill_name):
        removed_bill = self._bills.pop(bill_name, None)
        if removed_bill is not None:
                           self.save()
        return removed_bill

    def get_bill(self, bill_name):
         if bill_name is None:
            return None
         if bill_name.strip() == "":
            return None
         if bill_name not in self._bills:
            return None
        
         return self._bills[bill_name]

    def update_bill(self, bill_name):
        pass

    def save(self):
          data = [
            bill.to_dict() 
            for  bill in self._bills.values()
            ]
          with open("data/bills.json", "w") as file:
            json.dump(data, file, indent=4)
                   

    def load(self):
        self._bills = {}
        try:
            with open("data/bills.json", "r") as file:
                       data = json.load(file)
                   
            for item in data:
                       self.add_bill(Bill.from_dict(item))
        except FileNotFoundError:
                      print("No bill file found. Starting with empty bill list.")
        

    def has_bill(self, bill_name):
        return bill_name in self._bills

    def list_bills(self):
          return list(self._bills.values())

    def update(
                self, 
                name: str, 
                field: Field,
                value: Any
            ):
        bill_to_update = self.get_bill(name)
        if bill_to_update is None:
                return None
        match field:
                case Field.NAME:
                      del self._bills[name]
                      bill_to_update.name = value
                      self._bills[value] = bill_to_update
                case Field.AMOUNT:
                      bill_to_update.amount = value
                case Field.DUE_DATE:
                      bill_to_update.due_date = value
        self.save()

        return bill_to_update
          

          
          

    @property
    def bills_count(self):
        return len(self._bills)