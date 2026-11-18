from dotenv import load_dotenv
from finance_worker import FinanceWorker
from bill import Bill
from bills import Bills
from factories.worker_agent_factory import WorkerAgentFactory
from kernel.kernel import Kernel
from models.worker_spec import WorkerSpec
from models.provider_spec import ProviderSpec, ProviderType
from providers.openai_provider import OpenAIProvider
from datetime import date
from dataclasses import asdict
import os

def setup_test():
     spec = ProviderSpec(
          ProviderType.OPENAI,
          "OpenAI",
          "gpt-4o"
     )
     provider = OpenAIProvider(spec)
     kernel = Kernel(provider)
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


def test_finance_worker_can_answer_questions_about_bills():

    finance_worker = setup_test()
    response = finance_worker.process("What bills fo I have?")

    assert response is not None

def test_finance_worker_uses_bill_context():

     finance_worker = setup_test()
     response = finance_worker.process("What bills fo I have?")
     assert "Electric Bill" in response

     