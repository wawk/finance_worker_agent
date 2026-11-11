
from finance_worker import FinanceWorker
from bill import Bill
from factories.worker_agent_factory import WorkerAgentFactory
from kernel.kernel import Kernel
from models.worker_spec import WorkerSpec
from datetime import date
from dataclasses import asdict
import os
from datetime import date





def test_factory_creates_finance_worker():
    kernel = Kernel()
    factory = WorkerAgentFactory(kernel)
    worker_spec = WorkerSpec(
        "Rachel",
        "A Helpful Finance AI",
        worker_type = "finance",
        worker_class = FinanceWorker
    )
    
    finance_agent = factory.create_worker_agent(worker_spec)

    assert isinstance(finance_agent, FinanceWorker)

def test_can_store_and_retrieve_bill():
     kernel = Kernel()
     factory = WorkerAgentFactory(kernel)
     worker_spec = WorkerSpec(
            "Rachel",
            "A Helpful Finance AI",
            worker_type = "finance",
            worker_class = FinanceWorker
        )
    
     finance_agent = factory.create_worker_agent(worker_spec)

     finance_agent.add_bill(
       
       )Bill( "Electric Bill",
        165.00,
        date(2026, 11, 14)
    )

     bill = finance_agent.get_bill("Electric Bill")

     assert bill.name == "Electric Bill"
     assert bill.amount == 165.00
     assert bill.due_date == date(2026, 11, 14)

def test_get_bill_returns_none_when_bill_not_found():
              kernel = Kernel()
              factory = WorkerAgentFactory(kernel)
              worker_spec = WorkerSpec(
                      "Rachel",
                      "A Helpful Finance AI",
                      worker_type = "finance",
                      worker_class = FinanceWorker

                  )
              finance_agent = factory.create_worker_agent(worker_spec)
          
              finance_agent.add_bill(
                 Bill( "Electric Bill",
                  165.00,
                  date(2026, 11, 14)
                 )
              )
          
              bill = finance_agent.get_bill("Power Bill")

              assert bill is None

def test_finance_worker_can_list_bills():
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

         bills = finance_agent.list_bills()
         assert len(bills) == 3

def test_finance_worker_can_save_bills():
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

        assert os.path.exists("data/bills.json")
        assert True == True

def test_bill_can_be_serialized():
        bill = Bill(
                "Electric Bill",
                165.00,
                date(2026,11,14)
        )
        data = bill.to_dict()
        assert data["name"] == "Electric Bill"
        assert data["amount"] == 165.00
        assert data["due_date"] == "2026-11-14"

def test_bill_can_be_deserialized():
        bill = Bill(
                        "Electric Bill",
                        165.00,
                        date(2026,11,14)
                )
        data = bill.to_dict()

        bill = Bill.from_dict(data)

        assert bill.name == "Electric Bill"
        assert bill.amount == 165.00
        assert bill.due_date == date(2026, 11, 14)

def test_finance_worker_can_load_bills():
        kernel = Kernel()
        factory = WorkerAgentFactory(kernel)
        worker_spec = WorkerSpec(
                "Rachel",
                "A Helpful Finance AI",
                worker_type = "finance",
                worker_class = FinanceWorker
                                          )
        finance_agent = factory.create_worker_agent(worker_spec)

        finance_agent.load_bills()
        assert len(finance_agent.bills) == 3
        bill = finance_agent.get_bill("Electric Bill")
        assert bill is not None
        assert bill.name == "Electric Bill"
        assert bill.amount == 165.00
        assert bill.due_date == date(2026, 11, 14)


def test_finance_worker_can_remove_bills():
        kernel = Kernel()
        factory = WorkerAgentFactory(kernel)
        worker_spec = WorkerSpec(
                        "Rachel",
                        "A Helpful Finance AI",
                        worker_type = "finance",
                        worker_class = FinanceWorker
                                                  )
        finance_agent = factory.create_worker_agent(worker_spec)

        bill_removed = finance_agent.remove_bill("Mowing")

        assert bill_removed
        assert len(finance_agent.bills) == 2
        assert finance_agent.get_bill("Mowing") is None

def test_remove_bill_returns_none_when_bill_not_found():
    kernel = Kernel()
    factory = WorkerAgentFactory(kernel)
    worker_spec = WorkerSpec(
                           "Rachel",
                           "A Helpful Finance AI",
                           worker_type = "finance",
                           worker_class = FinanceWorker
                                                     )
    finance_agent = factory.create_worker_agent(worker_spec)
   
    bill_removed = finance_agent.remove_bill("Entertainment")

    assert bill_removed is None
    assert len(finance_agent.bills) == 2
    
   
        
        

        


         
                  