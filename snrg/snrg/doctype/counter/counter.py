# Copyright (c) 2024, administrator and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe


class Counter(Document):
	pass

@frappe.whitelist()
def create_counters():

	leads = frappe.get_list('Lead', fields=['name', 'mobile_no'])
	customers = frappe.get_list('Customer', fields=['name', 'mobile_no'])
	secondary_customers = frappe.get_list('Secondary Customer', fields=['name', 'mobile_no'])

	counters = leads + customers + secondary_customers

	for counter in counters:
		doc = frappe.new_doc("Counter")
		if not frappe.db.exists("Counter", {"name": counter.name}):
			doc.counter_name = counter.name
			doc.mobile_no = counter.mobile_no
			doc.save()
		else:
			frappe.db.set_value('Counter', counter.name, 'mobile_no', counter.mobile_no)

	return counters

def to_insert_new_document(self, method):
		doc = frappe.new_doc("Counter")
		if not frappe.db.exists("Counter", {"name": self.name}):
			doc.counter_name = self.name
			doc.mobile_no = self.mobile_no
			doc.save()
		else:
			frappe.db.set_value('Counter', self.name, 'mobile_no', self.mobile_no)

