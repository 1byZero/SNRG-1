frappe.ui.form.on("Sales Order", {
    setup(frm) {
        frm.set_query("transporter", {
            filters: {
                is_transporter: 1,
            },
        });
    },
    company_address: function(frm) {
        frm.set_value("dispatch_address_name",frm.doc.company_address)
    }
})