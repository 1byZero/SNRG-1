
frappe.ui.form.on("Lead", {
    custom_gstin:function(frm) {
        
        const custom_gstin = frm.doc.custom_gstin
        const custom_gstin_field = frm.get_field("custom_gstin")
        console.log("gstin",custom_gstin)
        console.log("gstin_field======", custom_gstin_field)

        const gstin_status = get_gstin_status(custom_gstin)
        console.log("gstin_status ===================================", gstin_status)

        set_custom_gstin_description(custom_gstin_field, gstin_status.status);
        console.log("set_custom_description===========".set_custom_gstin_description)

        

        
    }
})
function get_gstin_status(gstin) {
    return frappe
        .call({
            method: "india_compliance.gst_india.doctype.gstin.gstin.get_gstin_status",
            args: {gstin}
        })
        .then(r => r.message);
}
function set_custom_gstin_description(gstin_field, status) {
    console.log("status====================================================================",status)
    gstin_field.set_description(india_compliance.get_gstin_status_desc(status));
}
