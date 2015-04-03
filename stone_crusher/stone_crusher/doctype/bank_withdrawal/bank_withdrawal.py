# Copyright (c) 2013, Wayzon Technology Services Pvt Ltd and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class BankWithdrawal(Document):
	def on_submit(self):
		query=frappe.db.sql("""insert into `tabBank Balance` set bank=%s,bank_name=%s,account_no=%s,deposited_amount='0',withdrawal_amount=%s, interest_amount=%s,date=%s""",(self.bank,self.bank_name,self.account_no,self.withdrawal_amount,self.interest_amount,self.date))
