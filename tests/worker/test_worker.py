from dotenv import load_dotenv
from finance_worker import FinanceWorker
from bill import Bill
from bills import Bills
from tools.bills_tool import BillsTool
from factories.worker_agent_factory import WorkerAgentFactory
from kernel.kernel import Kernel
from models.worker_spec import WorkerSpec
from models.message import Message,MessageRole
from models.provider_spec import ProviderSpec, ProviderType
from providers.openai_provider import OpenAIProvider
from datetime import date
from dataclasses import asdict
import os
import json

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
                                  system_prompt = """
You are a financial worker agent.

Available Tools:

Tool: bills_tool
Functions:
- list_bills

When a user asks a question requiring bill information:

DO NOT ANSWER THE QUESTION.

Instead return ONLY a JSON object in this format:

{
    "tool": "bills_tool",
    "function": "list_bills"
}

Return no other text.

"""
,
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
     bills = Bills()
     bills.add_bill(bill_1)
     bills.add_bill(bill_2)
     bills.add_bill(bill_3)
     bills.save()

     finance_agent.bills = bills
    
     return finance_agent

def add_bills_tool_capability(worker):
       bills = worker.bills
       tool = BillsTool(bills)
       worker.add_tool(tool)
       return worker


def test_finance_worker_can_answer_questions_about_bills():

    finance_worker = setup_test()
    response = finance_worker.process("What bills fo I have?")

    assert response is not None

# def test_finance_worker_uses_bill_context():

#      finance_worker = setup_test()
#      response = finance_worker.process("What bills fo I have?")
#      assert "Electric Bill" in response

def test_finance_worker_can_register_list_bills_tool():
        finance_worker = setup_test()
        bills = finance_worker.bills
        tool = BillsTool(bills)
        finance_worker.add_tool(tool)
        assert tool.name in finance_worker.tool_registry
        bills_tool = finance_worker.tool_registry[tool.name]
        assert isinstance(bills_tool, BillsTool)

def test_bills_tool_returns_registered_bills():
      finance_worker = setup_test()
      bills = finance_worker.bills
      tool = BillsTool(bills)
      finance_worker.add_tool(tool)
      bills_tool = finance_worker.tool_registry[tool.name]
      bills_list = bills_tool.list_bills()
      assert len(bills_list) == 3
      assert  any (
            bill.name == "Electric Bill"
            for bill in bills_list
      )

def test_finance_worker_can_find_registered_bills_tool():
            finance_worker = add_bills_tool_capability(setup_test())
            tool = finance_worker.get_tool("bills_tool")
            assert tool is not None
            assert isinstance(tool, BillsTool)

def test_finance_worker_can_use_bills_tool():
            finance_worker = add_bills_tool_capability(setup_test())
            bills_list = finance_worker.use_tool(BillsTool.NAME, "list_bills")
            assert len(bills_list) == 3

def test_finance_worker_can_execute_llm_tool_request():
         finance_worker = add_bills_tool_capability(setup_test())
         llm_tool_request = {
                 "tool": "bills_tool",
                 "function": "list_bills"
         }
         result = finance_worker.execute_tool_request(llm_tool_request)
         
         assert len(result) == 3
        


# def test_finance_worker_can_determine_tool_and_function_for_question():
#          finance_worker = add_bills_tool_capability(setup_test())
#          tool_name, function_name = finance_worker.determine_tool_call(
#                  "What bill is due the next this month"
#          )
#          assert tool_name == BillsTool.NAME
#          assert function_name == ""

def test_finance_worker_uses_bills_tool_to_answer_due_bill_question():

      finance_worker = add_bills_tool_capability(setup_test())

      llm_response = finance_worker.process(
            "What bill is due the soonest this month?"
      )
      tool_request = json.loads(llm_response)
      result = finance_worker.execute_tool_request(tool_request)
               
      assert len(result) == 3

      assert "Electric Bill" in result