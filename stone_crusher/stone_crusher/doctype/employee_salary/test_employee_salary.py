# Copyright (c) 2013, Wayzon Technology Services Pvt Ltd and Contributors
# See license.txt

import frappe
import unittest

test_records = frappe.get_test_records('Employee Salary')

class TestEmployeeSalary(unittest.TestCase):
	pass
