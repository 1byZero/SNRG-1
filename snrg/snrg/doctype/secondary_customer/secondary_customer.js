// Copyright (c) 2024, administrator and contributors
// For license information, please see license.txt

frappe.ui.form.on("Secondary Customer", {
    gstin:function(frm) {

        const gstin = frm.doc.gstin
        const gstin_field = frm.get_field("gstin")

        frappe.call({
            method: "india_compliance.gst_india.doctype.gstin.gstin.get_gstin_status",
            args: {gstin},
            callback:(r) => {
                const  status = r.message.status
                gstin_field.set_description(india_compliance.get_gstin_status_desc(status));
            }
        })
    },
    onload_post_render(frm) {
        
        if(!frm.doc.address_display && !frm.is_new()){
            frappe.call({
                method: "snrg.doc_events.get_address",
                args: {
                    "docname":frm.doc.name
                },
                callback: function(r) {
                    if(r.message){
                        frm.set_value("address_display",r.message)
                    }
                }
            })
        }

        if(!frm.doc.contact_display && !frm.is_new()){
            frappe.call({
                method: "snrg.doc_events.get_contact",
                args: {
                    "docname": frm.doc.name
                },
                callback: function(r) {
                    if(r.message) {
                        frm.set_value("contact_display", r.message)
                    }
                },
            })
        }
    },
})
