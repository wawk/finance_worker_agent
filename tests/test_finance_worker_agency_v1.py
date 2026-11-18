from finance_worker import FinanceWorker
from bill import Bill
from bills import Bills
from factories.worker_agent_factory import WorkerAgentFactory
from kernel.kernel import Kernel
from models.worker_spec import WorkerSpec
from datetime import date
from dataclasses import asdict
import os

def setup_test():
     kernel = Kernel()
     factory = WorkerAgentFactory(kernel)
     worker_spec = WorkerSpec(
                                  "Rachel",
                                  "A Helpful Finance AI",
                                  worker_type = "finance",
                                  worker_class = FinanceWorker
                              )
     finance_agent = factory.create_worker_agent(worker_spec)
    
     bill_1 = Bill(
                     "Electric Bill",
                     165.00,
                     date(2026, 11, 14)
             )
    
     bill_2 = Bill(
                     "Mowing",
                     155.0,
                     date(2026, 11, 14)
             )
     bill_3 = Bill(
                     "Phones",
                     96.0,
                     date(2026, 11, 4)
             )
    
     finance_agent.add_bill(bill_1)
     finance_agent.add_bill(bill_2)
     finance_agent.add_bill(bill_3)
     finance_agent.save_bills()
     return finance_agent


def test_finance_worker_can_summarize_bills():
     finance_agent = setup_test()
     finance_agent.load_bills()
     summary = finance_agent.get_bill_summary()

     assert summary is not None
     assert "3 bills" in summary
     assert "$416.00" in summary
     assert "Electric Bill" in summary
     assert "Mowing" in summary
     assert "Phones" in summary
     assert "Sdports" not in summary

def test_finance_worker_can_get_largest_bill():
     finance_agent = setup_test()
     finance_agent.load_bills()
     largest_bill = finance_agent.get_largest_bill()
     assert largest_bill.name == "Electric Bill"

def test_finance_worker_can_get_smallest_bill():
     finance_agent = setup_test()
     finance_agent.load_bills()
     smallest_bill = finance_agent.get_smallest_bill()
     assert smallest_bill.name == "Phones"

    