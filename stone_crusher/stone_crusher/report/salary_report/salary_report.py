# Copyright (c) 2013, Wayzon Technology Services Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns = get_columns()
	item_stock = get_stock(filters)
	data = []
	for d in item_stock:
		row = [d.employee,d.employee_name,d.employee_mobile,d.advance_amount]
		data.append(row)
	return columns, data
def get_columns():
	return [("Employee")+"::150",("Employee Name")+"::150",("Employee Mobile")+"::150",(" Amount")+"::150"]
def get_stock(filters):
	return frappe.db.sql("""select employee,employee_name,employee_mobile,advance_amount from `tabSalary Info`""",as_dict=1)
