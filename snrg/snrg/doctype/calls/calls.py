# Copyright (c) 2024, administrator and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
import json


class Calls(Document):
	pass


@frappe.whitelist()
def get_values_for_mobile_no_and_company_name(doc):
	doc = json.loads(doc)

	doctype = doc.get('call_to')
	name = doc.get('lead__party')

	filters = {'name': name}
	fields = ['mobile_no']

	if doctype == 'Lead':
		fields.append('company_name')
		fields.append('lead_name')
	
	if doctype == 'Customer':
		fields.append('customer_name')

	if doctype == 'Secondary Customer':
		fields.append('first_name')

	document = frappe.get_list(doctype, filters, fields)

	return document


