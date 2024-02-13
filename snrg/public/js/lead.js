
frappe.ui.form.on("Lead", {
    custom_gstin:function(frm) {

        const gstin = frm.doc.custom_gstin
        const gstin_field = frm.get_field("custom_gstin")

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
        frm.remove_custom_button(__("Customer"), "Create");
    },
    refresh(frm) {
        if(!frm.is_new()) {
            frm.add_custom_button(__("Secondary Customer"), make_secondary_customer, __("Create"))
            frm.add_custom_button(__("Create Customer"), make_customer, __("Create"));
        }
        function make_secondary_customer() {
            frappe.model.open_mapped_doc({
                method: "snrg.doc_events.make_secondary_customer",
                frm: cur_frm,
            })
        }
    },
    
})

let make_customer = function  () {
    frappe.model.open_mapped_doc({
        method: "snrg.doc_events.make_customer",
        frm: cur_frm
    })
}
