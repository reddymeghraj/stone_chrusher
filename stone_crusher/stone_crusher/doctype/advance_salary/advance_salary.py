# Copyright (c) 2013, Wayzon Technology Services Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class AdvanceSalary(Document):
	def on_submit(self):
		q=frappe.db.sql("""select * from `tabSalary Info` where employee=%s""",self.employee)
		if q:
			q1=frappe.db.sql("""update `tabSalary Info` set advance_amount=advance_amount+%s where employee=%s""",(self.advance_amount,self.employee))
		else:
			q2=frappe.db.sql("""select max(cast(name as int)) from `tabSalary Info`""")
			if q2[0][0]:
				name=int(q2[0][0])+1
			else:
				name=1
				
			q1=frappe.db.sql("""insert into `tabSalary Info` set name=%s,employee=%s,employee_name=%s,employee_mobile=%s,advance_amount=%s""",(name,self.employee,self.employee_name,self.mobile_no,self.advance_amount))	
