# Copyright (c) 2013, Wayzon Technology Services Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Discount(Document):
	def on_submit(self):
		amount=self.discount+self.paid_amount;
		q=frappe.db.sql("""update `tabCreditor Info` set amount=amount+%s where client=%s and client_name=%s and client_address=%s and client_mobile=%s""",(amount,self.client,self.client_name,self.address,self.mobile_no))		
@frappe.whitelist()
def get_amount(client):
	query=frappe.db.sql("""select amount from `tabCreditor Info` where client=%s""",(client))
	return query[0][0]
