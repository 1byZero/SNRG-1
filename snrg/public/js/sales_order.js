frappe.ui.form.on("Sales Order", {
    setup(frm) {
        frm.set_query("transporter" , {
            filters: {
                is_transporter: 1,
            },
        });
    }
})