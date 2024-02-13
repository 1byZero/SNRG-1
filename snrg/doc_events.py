import frappe
from frappe.model.mapper import get_mapped_doc


@frappe.whitelist()
def make_secondary_customer(source_name, target_doc=None):
    return _make_secondary_customer(source_name, target_doc)

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

def validate_gstin(self, method):
    gstin = ""
    doctype = ""
    
    if self.doctype == "Lead":
        gstin = self.custom_gstin
        doctype = self.doctype

        gstin_exists = frappe.db.exists(doctype, {
            "custom_gstin": gstin
        })

        if gstin_exists: frappe.throw("The GSTIN Number that you are entered is already exists in {0}".format(doctype))
    else:
        gstin = self.gstin
        doctype = self.doctype

        gstin_exists = frappe.db.exists(doctype, {
            "gstin": gstin
        })

        if gstin_exists: frappe.throw("The GSTIN Number that you are entered is already exists in {0}".format(doctype))
    