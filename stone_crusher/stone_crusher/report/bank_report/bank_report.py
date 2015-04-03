# Copyright (c) 2013, Wayzon Technology Services Pvt Ltd and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns = get_columns()
	item_stock = get_stock(filters)
	data = []
	for d in item_stock:
		row = [d.bank_name,d.account_no,d.bdamount,d.bwamount,d.interest_amount,d.available_balance]
		data.append(row)
	return columns, data
def get_columns():
	return [("Bank Name")+"::150",("Account No")+"::150",("Deposit Amount")+"::150",("Withrawal Amount")+"::150",("interest_amount")+"::150",("Available Balance")+"::150"]
def get_stock(filters):
	return frappe.db.sql("""select bank_name,account_no,sum(deposited_amount)as bdamount,sum(withdrawal_amount)as bwamount,sum(deposited_amount)-(sum(withdrawal_amount)+sum(interest_amount))as available_balance,sum(interest_amount)as interest_amount from `tabBank Balance` group by account_no""",as_dict=1)
	