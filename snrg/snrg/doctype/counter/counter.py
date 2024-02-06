# Copyright (c) 2024, administrator and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe


class Counter(Document):
	pass

@frappe.whitelist()
def create_counters():

	leads = frappe.get_list('Lead', fields=['name', 'mobile_no', 'lead_name'])
	customers = frappe.get_list('Customer', fields=['name', 'mobile_no', 'customer_name'])
	secondary_customers = frappe.get_list('Secondary Customer', fields=['name', 'mobile_no', 'first_name'])

	counters = leads + customers + secondary_customers

	# for counter in counters:
	# 	doc = frappe.new_doc("Counter")
	# 	if not frappe.db.exists("Counter", {"name": counter.name}):
	# 		doc.counter_name = counter.name
	# 		doc.mobile_no = counter.mobile_no
	# 		doc.save()
	# 	else:
	# 		frappe.db.set_value('Counter', counter.name, 'mobile_no', counter.mobile_no)

	# 		frappe.db.set_value('Counter', counter.name, 'customer_name', )

	for lead in leads:
		doc = frappe.new_doc('Counter')
		if not frappe.db.exists("Counter", {"name": lead.name}):
			doc.counter_name = lead.name
			doc.mobile_no = lead.mobile_no
			doc.customer_name = lead.lead_name
			doc.save()
		else:
			frappe.db.set_value('Counter', lead.name, 'mobile_no', lead.mobile_no)
			frappe.db.set_value('Counter', lead.name, 'customer_name', lead.lead_name)

	for customer in customers:
		doc = frappe.new_doc('Counter')
		if not frappe.db.exists("Counter", {"name": customer.name}):
			doc.counter_name = customer.name
			doc.mobile_no = customer.mobile_no
			doc.customer_name = customer.customer_name
			doc.save()
		else:
			frappe.db.set_value('Counter', customer.name, 'mobile_no', customer.mobile_no)
			frappe.db.set_value('Counter', customer.name, 'customer_name', customer.customer_name)

	for secondary_customer in secondary_customers:
		doc = frappe.new_doc('Counter')
		if not frappe.db.exists("Counter", {"name": secondary_customer.name}):
			doc.counter_name = secondary_customer.name
			doc.mobile_no = secondary_customer.mobile_no
			doc.customer_name = secondary_customer.first_name
			doc.save()
		else:
			frappe.db.set_value('Counter', secondary_customer.name, 'mobile_no', secondary_customer.mobile_no)
			frappe.db.set_value('Counter', secondary_customer.name, 'customer_name', secondary_customer.first_name)

	return counters

def insert_or_update_document(self, method):
		doc = frappe.new_doc("Counter")

		if not frappe.db.exists("Counter", {"name": self.name}):
			if(self.doctype == 'Lead'):
				doc.counter_name = self.name
				doc.mobile_no = self.mobile_no
				doc.customer_name = self.lead_name
				doc.save()

			if(self.doctype == 'Customer'):
				doc.counter_name = self.name
				doc.mobile_no = self.mobile_no
				doc.customer_name = self.customer_name
				doc.save()

			if(self.doctype == 'Secondary Customer'):
				doc.counter_name = self.name
				doc.mobile_no = self.mobile_no
				doc.customer_name = self.first_name
				doc.save()
		else:
			if(self.doctype == 'Lead'):
				frappe.db.set_value('Counter', self.name, 'mobile_no', self.mobile_no)
				frappe.db.set_value('Counter', self.name, 'customer_name', self.lead_name)
			
			if(self.doctype == 'Customer'):
				frappe.db.set_value('Counter', self.name, 'mobile_no', self.mobile_no)
				frappe.db.set_value('Counter', self.name, 'customer_name', self.customer_name)

			if(self.doctype == 'Secondary Customer'):
				frappe.db.set_value('Counter', self.name, 'mobile_no', self.mobile_no)
				frappe.db.set_value('Counter', self.name, 'customer_name', self.first_name)