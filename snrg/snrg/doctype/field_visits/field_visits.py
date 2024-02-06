# Copyright (c) 2024, administrator and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
from frappe import _

# @frappe.whitelist()
class FieldVisits(Document):
	pass
	# def get_data():
	# 	return {
	# 		'fieldname': 'counter_name',
	# 		'label': _('Counter Name'),
	# 		'fieldtype': 'Autocomplete',
	# 		'options': 'snrg.snrg.doctype.field_visits.field_visits.get_doctype_names',
	# 		'reqd': 1,
	# 	}

# @frappe.whitelist()
# def get_data():
# 		return {
# 			'fieldname': 'counter_name',
# 			'label': _('Counter Name'),
# 			'fieldtype': 'Autocomplete',
# 			'get_query': 'snrg.snrg.doctype.field_visits.field_visits.get_doctype_names',
# 			'reqd': 1,
# 		}

@frappe.whitelist()
# @frappe.validate_and_sanitize_search_inputs
def get_doctype_names(doctype = None, txt=None, searchfield=None, start=None, page_len=None, filters=None):
	frappe.errprint([doctype, txt, searchfield, start, page_len, filters])
	counter_name = []
	lead_name = frappe.get_list('Lead', pluck= 'name')
	customer_name = frappe.get_list('Customer', pluck= 'name')
	secondary_customer_name = frappe.get_list('Secondary Customer', pluck= 'name')

	counter_name.append(lead_name)
	counter_name.append(customer_name)
	counter_name.append(secondary_customer_name)
	print("------------------------------------------------------------------------------",counter_name)

	# values = [ (name, ) for name in counter_name]

	# frappe.errprint(values)
	return counter_name
