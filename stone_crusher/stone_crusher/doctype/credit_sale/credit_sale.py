# Copyright (c) 2013, Wayzon Technology Services Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CreditSale(Document):
	def validate(self):
		query=frappe.db.sql("""select * from `tabCreditor Client` where client=%s and client_name=%s and client_address=%s and client_mobile=%s""",(self.client,self.client_name,self.address,self.mobile_no))
		if query:
			pass
		else:
			frappe.throw("Please Add Client first in Creditor Client List")	
	def on_submit(self):
		q=frappe.db.sql("""update `tabCreditor Info` set amount=amount-%s where client=%s and client_name=%s and client_address=%s and client_mobile=%s""",(self.amount_received,self.client,self.client_name,self.address,self.mobile_no))		
@frappe.whitelist()
def get_credit_amount(client):
	que=frappe.db.sql("""select amount from `tabCreditor Info` where client=%s""",client)[0][0]
	return que		