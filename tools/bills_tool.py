from bills import Bills
from tools.tool import Tool
from bills import Bills

class BillsTool(Tool):
    NAME = "bills_tool"
    def  __init__(
        self,
        bills: Bills
    ):
        super().__init__(BillsTool.NAME)
        self.bills = bills

    def list_bills(self):
        return self.bills.list_bills()
   
   