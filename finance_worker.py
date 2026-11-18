
from agents.worker_agent import WorkerAgent
from providers.provider import Provider
from bill import Bill
from bills import Bills
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
                self.bills = Bills()
                self.bills.load()



    def add_bill(self,bill):
          self.bills.add_bill(bill)
            

    def get_bill(self,name):
            if name is None:
                return None
            if name.strip() == "":
                   return None
            if not self.bills.has_bill(name):
                   return None

            bill = self.bills.get_bill(name)
            return bill
                                  

    def list_bills(self):
          list = self.bills.list_bills()
          return list


    def save_bills(self):
          self.bills.save()
       

    def load_bills(self):
           self.bills.load()
      
    def remove_bill(self, bill_name):
             removed_bill = self.bills.remove_bill(bill_name)
             return removed_bill

  
    def get_bill_summary(self):
               # Temporary for testing purposes only
               total = self.bills.bills_total
               bill_lines =  ""
               for  bill in self.list_bills():
                  bill_lines += (
                    f" - {bill.name}: "
                    f"${bill.amount:.2f} "
                    f"{bill.due_date}\n"
                                  )
           
               MOCK_BILL_SUMMARY = f"""
                  Bill Summary
           
                  You currently have {self.bills.bills_count} bills.
           
                  Total obligations: ${total:.2f}
           
                  Bills:
                  {bill_lines}
                  """
               return  MOCK_BILL_SUMMARY

    def get_largest_bill(self):
            return self.bills.get_largest_bill()

    def get_smallest_bill(self):
           return self.bills.get_smallest_bill()
           


             
              
           
