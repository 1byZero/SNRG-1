import frappe
from frappe.model.mapper import get_mapped_doc
from frappe.contacts.doctype.address.address import get_address_display


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

    if not self.get_doc_before_save():
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


def create_address(self, method):
    
    if not self.get_doc_before_save():
        address = frappe.get_doc({
            "doctype": "Address",
            "address_title": self.get("name"),
            "address_line1": self.get("address_line1"),
            "address_line2": self.get("address_line2"),
            "city": self.get("city"),
            "state": self.get("state"),
            "pincode": self.get("pincode"),
            "country": self.get("country"),
            "links": [{"link_doctype": self.get("doctype"), "link_name": self.get("name")}]
        })

        address.insert()


def create_address_and_contact(self, method):

    if not self.get_doc_before_save():
        address = frappe.get_doc({
            "doctype": "Address",
            "address_title": self.get("name"),
            "address_line1": self.get("address_line1"),
            "address_line2": self.get("address_line2"),
            "city": self.get("city"),
            "state": self.get("state"),
            "pincode": self.get("pincode"),
            "country": self.get("country"),
            "links": [{"link_doctype": self.get("doctype"), "link_name": self.get("name")}]
        })

        address.insert()

        contact = frappe.get_doc({
             "doctype": "Contact",
             "first_name": self.get("first_name"),
             "last_name": self.get("last_name"),
             "company_name": self.get("company_name"),
             "is_primary_contact": 1,
             "email_ids": [{"email_id": self.get("email_id"), "is_primary": 1}],
             "phone_nos": [{"phone": self.get("mobile_no"), "is_primary_mobile_no": 1}],
             "links": [{"link_doctype": self.get("doctype"), "link_name": self.get("name")}],
        })

        contact.insert()

@frappe.whitelist()
def get_address(docname):
     
    get_address = frappe.get_list('Address',
                                  filters = [
                                       ['Dynamic Link', 'link_doctype', '=', 'Secondary Customer'],
                                       ['Dynamic Link', 'link_name', '=', docname],
                                       ['Dynamic Link', 'parenttype', '=', 'Address'], 
                                  ],
                                  fields = ["*"],)
    if len(get_address):
        return get_address_display(get_address[0])
    
    return {}


@frappe.whitelist()
def get_contact(docname):
     
     get_contact = frappe.get_list('Contact', 
                                   filters = [
                                       ['Dynamic Link', 'link_doctype', '=', 'Secondary Customer'],
                                       ['Dynamic Link', 'link_name', '=', docname],
                                       ['Dynamic Link', 'parenttype', '=', 'Contact'], 
                                  ],
                                  fields = ["*"],)
     
     if len(get_contact):
          return get_contact_display(get_contact[0].name)
     
     return {}
     

def get_contact_display(contact):
	contact_info = frappe.db.get_value(
		"Contact", contact, ["first_name", "last_name", "email_id", "mobile_no"], as_dict=1
	)

	contact_info.html = (
		""" <b>%(first_name)s %(last_name)s</b> <br> %(email_id)s <br> %(mobile_no)s"""
		% {
			"first_name": contact_info.first_name,
			"last_name": contact_info.last_name or "",
			"email_id": contact_info.email_id or "",
			"mobile_no": contact_info.mobile_no or "",
		}
	)

	return contact_info.html

