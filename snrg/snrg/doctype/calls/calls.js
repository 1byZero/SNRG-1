// Copyright (c) 2024, administrator and contributors
// For license information, please see license.txt

frappe.ui.form.on("Calls", {
    lead__party(frm) {
        frappe.call({
            method: "snrg.snrg.doctype.calls.calls.get_values_for_mobile_no_and_company_name",
            args :{
                doc: frm.doc,
            },
            callback: function (response) {
                if(response.message){
                    if(response.message[0].company_name){
                        frm.set_value('company_name', response.message[0].company_name)
                    }
                    else if(response.message[0].customer_name){
                        frm.set_value('company_name', response.message[0].customer_name)
                    }
                    else if(response.message[0].first_name){
                        frm.set_value('company_name', response.message[0].first_name)
                    }
                    else if(response.message[0].employee_name){
                        frm.set_value('company_name', response.message[0].employee_name)
                        frm.set_value('mobile_number', response.message[0].cell_number)
                    }
                    if(response.message[0].mobile_no != null)
                        frm.set_value('mobile_number', response.message[0].mobile_no)
                }
            }
        })
    }
});
