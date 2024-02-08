frappe.ui.form.on("Lead", {
    custom_gstin:function(frm) {
        const custom_gstin = frm.doc.custom_gstin
        const custom_gstin_field = frm.get_field("custom_gstin")
        custom_gstin_field.set_description(get_gstin_description());

        console.log("gstin",custom_gstin)
        console.log("gstin_field======", custom_gstin_field)

        function get_gstin_description() {
            if (!gst_settings.sandbox_mode) {
                return __("Autofill lead information by entering their GSTIN");
            }
        
            return __("Autofill is not supported in sandbox mode");
        }

        const custom_gstin_info = get_custom_gstin_info(custom_gstin)
        console.log("custo_gstin_info===========",custom_gstin_info)
        set_custom_gstin_description(custom_gstin_field, custom_gstin_info.status);
        console.log("set_custom_description===========".set_custom_gstin_description)
        map_custom_gstin_info(frm, custom_gstin_info)
        console.log("map_custom_info==============",map_custom_gstin_info)


        function get_custom_gstin_info(gstin, throw_error = true) {
            console.log("gstin====================================================================",gstin)
            return frappe.call({
                method: "india_compliance.gst_india.utils.gstin_info.get_gstin_info",
                args: {gstin, throw_error}
            }).then(r => r.message);
        }
        
        function set_custom_gstin_description(gstin_field, gstin_status) {
            console.log("gstin_field", gstin_field)
            console.log(gstin_status)
            gstin_field.set_description(india_compliance.get_gstin_status_desc(gstin_status));
        }

        function map_custom_gstin_info(frm, custom_gstin_info) {
            console.log("map_cusom", frm, "custom_info", custom_gstin_info)
            frm.set_value("company_name", custom_gstin_info.business_name)
            frm.set_value("state", custom_gstin_info.permanent_address.state)
            frm.set_value("city", custom_gstin_info.permanent_address.city)
        }

    }
})