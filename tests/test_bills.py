from bills import Bills
from bill import Bill, Field
from datetime import date
import os

def test_bills_can_add_bill():
    bills = Bills()
    bill_1 =  Bill( "Electric Bill",
            165.00,
            date(2026, 11, 14)
        )
    bills.add_bill(bill_1)

    assert bills.bills_count == 1
    bill = next(iter(bills._bills.values()))
    assert bill.name == "Electric Bill"


def test_bills_can_save_bills():
    bills = Bills()

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
    bills.add_bill(bill_1)
    bills.add_bill(bill_2)
    bills.add_bill(bill_3)
    bills.save()
    assert os.path.exists("data/bills.json")


def test_bills_has_bill():
    bills = Bills()
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
    bill_4 = Bill(
                "Entertainment",
                500.0,
                date(2026, 11, 24)
            )
    bills.add_bill(bill_1)
    bills.add_bill(bill_2)
    bills.add_bill(bill_3)
    bills.add_bill(bill_4)
   
    assert bills.has_bill("Electric Bill")
    assert not bills.has_bill("Health")

def test_bills_can_load_bills():
    bills = Bills()
    bills.load()
    assert bills.bills_count == 3
    assert bills.has_bill("Electric Bill")

    

def test_bills_can_get_bill():
    bills = Bills()
    bills.load()
    bill = bills.get_bill("Mowing")
    assert bill is not None
    assert bill.name == "Mowing"




def test_bills_can_list_bills():
    bills = Bills()
    bills.load()
    list = bills.list_bills()
    assert len(list)  == bills.bills_count

def test_bills_can_update_bill():
    bills = Bills()
    bills.load()
   
    updated = bills.update("Mowing", Field.NAME, "Snow Plowing")
    assert updated is not None
    assert updated.name == "Snow Plowing"
    bills.load()
    assert bills.has_bill("Snow Plowing")

def test_bills_can_remove_bill():
        bills = Bills()
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
        bill_4 = Bill(
                        "Entertainment",
                        500.0,
                        date(2026, 11, 24)
                    )
        bills.add_bill(bill_1)
        bills.add_bill(bill_2)
        bills.add_bill(bill_3)
        bills.add_bill(bill_4)
        assert bills.bills_count == 4
        removed_bill = bills.remove_bill("Entertainment")
        assert removed_bill is not None
        assert isinstance(removed_bill, Bill)
        assert removed_bill.name == "Entertainment"
        assert bills.bills_count == 3
        assert not bills.has_bill("Entertainment")








    
