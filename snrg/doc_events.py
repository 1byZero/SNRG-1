import frappe
from frappe.model.mapper import get_mapped_doc


@frappe.whitelist()
def make_secondary_customer(source_name, target_doc=None):
    return _make_secondary_customer(source_name, target_doc)

@frappe.whitelist()
def make_customer(source_name, target_doc=None):
      return _make_customer(source_name, target_doc)

def _make_secondary_customer(source_name, target_doc=None, ignore_permissions= False):
    
    doclist = get_mapped_doc(
        "Lead", 
        source_name,
        {
            "Lead": {
                "doctype": "Secondary Customer",
                "field_map": {
                    "company_name": "company_name",
                    "first_name": "first_name",
                    "Lead_owner":  "Lead_owner",
                    "source": "source",
                    "city": "city",
                    "state": "state",
                    "mobile_no": "mobile_no",
                    "request_type": "request_type",
                }
            }
        },
        target_doc,
        ignore_permissions= ignore_permissions,
    )
        
    return doclist

def _make_customer(source_name, target_doc=None, ignore_permissions=False):
	def set_missing_values(source, target):
		if source.company_name:
			target.customer_type = "Company"
			target.customer_name = source.company_name
		else:
			target.customer_type = "Individual"
			target.customer_name = source.lead_name

		target.customer_group = frappe.db.get_default("Customer Group")

	doclist = get_mapped_doc(
		"Lead",
		source_name,
		{
			"Lead": {
				"doctype": "Customer",
				"field_map": {
					"name": "lead_name",
					"company_name": "customer_name",
					"contact_no": "phone_1",
					"fax": "fax_1",
                    "custom_gstin": "gstin",
				},
				"field_no_map": ["disabled"],
			}
		},
		target_doc,
		set_missing_values,
		ignore_permissions=ignore_permissions,
	)

	return doclist

def validate_gstin(self, method):
    gstin = ""
    doctype = ""
    gstin_exists = False
    if self.doctype == "Lead":
        gstin = self.custom_gstin
        doctype = self.doctype

        if gstin:
            gstin_exists = frappe.db.exists(doctype, {
                "custom_gstin": gstin
            })

        if gstin_exists: frappe.throw("The GSTIN Number that you are entered is already exists in {0}".format(doctype))
    else:
        gstin = self.gstin
        doctype = self.doctype

        if gstin:
            gstin_exists = frappe.db.exists(doctype, {
                "gstin": gstin
            })

        if gstin_exists: frappe.throw("The GSTIN Number that you are entered is already exists in {0}".format(doctype))
    