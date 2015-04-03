# Copyright (c) 2013, Wayzon Technology Services Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns = get_columns()
	item_stock = get_stock(filters)
	data = []
	for d in item_stock:
		row = [d.client_name,d.client_address,d.client_mobile,d.amount]
		data.append(row)
	return columns, data
def get_columns():
	return [("Client Name")+"::150",("Clent Address")+"::150",("Client Mobile")+"::150",("Credit Amount")+"::150"]
def get_stock(filters):
	return frappe.db.sql("""select client_name,client_address,client_mobile,amount from `tabCreditor Info`""",as_dict=1)