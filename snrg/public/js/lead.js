
frappe.ui.form.on("Lead", {
    custom_gstin:function(frm) {
        function get_gstin_status (gstin) {
            let status = "";
            frappe
                .call({
                    method: "india_compliance.gst_india.doctype.gstin.gstin.get_gstin_status",
                    args: {gstin},
                    callback:(r) => {
                        console.log("R. message =========================",r.message)
                        status = r.message.status
                        console.log("callback status===================", status)
                        return r.message
                    }
                })
        }

        function set_custom_gstin_description (gstin_field, status) {
            console.log("status====================================================================",status)
            gstin_field.set_description(india_compliance.get_gstin_status_desc(status));
        }
        
        const custom_gstin = frm.doc.custom_gstin
        const custom_gstin_field = frm.get_field("custom_gstin")
        const gstin_status = ""
        console.log("gstin",custom_gstin)
        console.log("gstin_field======", custom_gstin_field)
        // console.log(get_gstin_status(custom_gstin));

        if(custom_gstin) {
            const gstin_status = get_gstin_status(custom_gstin)
            console.log("gstin_status ===================================", gstin_status)
        }

        if(gstin_status != "") {
            set_custom_gstin_description(custom_gstin_field, gstin_status.status);
            console.log("set_custom_description===========",set_custom_gstin_description)
        }
      
    },
    refresh(frm) {
        if(!frm.is_new()) {
            frm.add_custom_button(__("Secondary Customer"), make_secondary_customer, __("Create"))
        }
        function make_secondary_customer() {
            console.log("Secondary Customer")
            frappe.model.open_mapped_doc({
                method: "snrg.doc_events.make_secondary_customer",
                frm: cur_frm,
            })
        }
    }
})
