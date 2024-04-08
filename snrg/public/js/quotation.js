frappe.ui.form.on("Quotation", {
    refresh:function(frm){
        frm.set_query("transporter", {
            filters: {
                is_transporter: 1
            },
        });
    }
    // setup(frm) {
    //     frm.set_query("transporter", {
    //         filters: {
    //             is_transporter: 1,
    //         },
    //     });
    // }
})