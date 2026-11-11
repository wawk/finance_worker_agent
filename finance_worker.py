
from agents.worker_agent import WorkerAgent
from providers.provider import Provider
from bill import Bill
from dataclasses import asdict
import os
import json

class FinanceWorker(WorkerAgent):
    def __init__(
            self, 
            name: str, 
            worker_id: str,
            provider: Provider,
            changed_definition_callback=None
            ):
                super().__init__(
                        name = name, 
                        worker_id = worker_id,
                        provider = provider,
                        changed_definition_callback=changed_definition_callback
                        )
                self.bills = {}
                self.load_bills()

    def add_bill(self,bill):
                     
            self.bills[bill.name] = bill

    def get_bill(self,name):
            if name is None:
                return None
            if name.strip() == "":
                   return None
            if name not in self.bills:
                   return None

            return self.bills[name]

    def list_bills(self):
           return list(self.bills.values())

    def save_bills(self):
           data = [
                  bill.to_dict() 
                  for  bill in self.bills.values()
                  ]
           with open("data/bills.json", "w") as file:
                  json.dump(data, file, indent=4)
           

    def load_bills(self):
       self.bills = {}
       try:
              with open("data/bills.json", "r") as file:
               data = json.load(file)
           
              for item in data:
               self.add_bill(Bill.from_dict(item))
       except FileNotFoundError:
              print("No bill file found. Starting with empty bill list.")

    def remove_bill(self, bill_name):
             removed_bill = self.bills.pop(bill_name, None)
             if removed_bill is not None:
                   self.save_bills()
             return removed_bill


             
              
           
