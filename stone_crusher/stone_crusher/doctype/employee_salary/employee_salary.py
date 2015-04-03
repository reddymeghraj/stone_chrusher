# Copyright (c) 2013, Wayzon Technology Services Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
class EmployeeSalary(Document):
	def validate(self):
		q=frappe.db.sql("""select advance_amount from `tabSalary Info` where employee=%s """,self.employee)
		if q:
			a=float(q[0][0])
			b=float(self.salary)
			if a<b:
				c=b-a
				frappe.msgprint(c,"Amount Is Less In Advance Salary")
				frappe.throw("Please Submit Amount In Advance Salary before Salary")
			else:
				pass
		else:
			frappe.throw("Please Submit the Advance Salary First and then Do Salary")
	def on_submit(self):
		q1=frappe.db.sql("""update `tabSalary Info` set advance_amount=advance_amount-%s where employee=%s""",(self.salary,self.employee))		