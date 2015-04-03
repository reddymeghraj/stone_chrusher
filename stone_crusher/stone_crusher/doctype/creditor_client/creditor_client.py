# Copyright (c) 2013, Wayzon Technology Services Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CreditorClient(Document):
	def on_submit(self):
		q=frappe.db.sql("""select * from `tabCreditor Info` where client=%s and client_name=%s and client_address=%s and client_mobile=%s""",(self.client,self.client_name,self.client_address,self.client_mobile))
		if q:
			q1=frappe.db.sql("""update `tabCreditor Info` set amount=amount+%s where client=%s and client_name=%s and client_address=%s and client_mobile=%s""",(self.credit_amount,self.client,self.client_name,self.client_address,self.client_mobile))
		else:
			qc=frappe.db.sql("""select max(cast(name as int)) from `tabCreditor Info`""")
			if qc[0][0]:
				name=int(qc[0][0])+1
			else:
				name=1
				
			query1=frappe.db.sql("""insert into `tabCreditor Info` set name=%s,client=%s,client_name=%s,client_address=%s,client_mobile=%s,amount=%s""",(name,self.client,self.client_name,self.client_address,self.client_mobile,self.credit_amount));	