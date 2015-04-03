# Copyright (c) 2013, Wayzon Technology Services Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class TempororyCredit(Document):
	def on_submit(self):
		query=frappe.db.sql("""select * from `tabTemporory Creditdebit` where tname=%s and mobile_no=%s""",(self.from_name,self.mobile_no))
		if query:
			q=frappe.db.sql("""update `tabTemporory Creditdebit` set amount=amount+%s where tname=%s and mobile_no=%s""",(self.amount,self.from_name,self.mobile_no))
		else:
			q1=frappe.db.sql("""select max(cast(name as int)) from `tabTemporory Creditdebit`""")
			if q1[0][0]:
				name=int(q1[0][0])+1
			else:
				name=1
				
			q=frappe.db.sql("""insert into `tabTemporory Creditdebit` set name=%s,tname=%s,mobile_no=%s,amount=%s""",(name,self.from_name,self.mobile_no,self.amount))
			