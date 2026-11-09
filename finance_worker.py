import sys
sys.path.insert(0, "/Users/stevem/projects/platform_core")

from agents.worker_agent import WorkerAgent
from providers.provider import Provider
from models.bill import Bill
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
           

    def load_bills():
           pass
           
