
frappe.ui.form.on("Lead", {
    custom_gstin:function(frm) {
        
        const custom_gstin = frm.doc.custom_gstin
        const custom_gstin_field = frm.get_field("custom_gstin")
        console.log("gstin",custom_gstin)
        console.log("gstin_field======", custom_gstin_field)
        console.log(this.get_gstin_status(custom_gstin)); 

        const gstin_status = this.get_gstin_status(custom_gstin)
        console.log("gstin_status ===================================", gstin_status)

        this.set_custom_gstin_description(custom_gstin_field, gstin_status.status);
        console.log("set_custom_description===========".set_custom_gstin_description)

           
    },
    get_gstin_status: function (gstin) {
        return frappe
            .call({
                method: "india_compliance.gst_india.doctype.gstin.gstin.get_gstin_status",
                args: {gstin}
            })
            .then(r => r.message);
    },
    set_custom_gstin_description: function(gstin_field, status) {
        console.log("status====================================================================",status)
        gstin_field.set_description(india_compliance.get_gstin_status_desc(status));
    }
})
