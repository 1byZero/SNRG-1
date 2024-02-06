frappe.listview_settings['Counter'] = {
    onload: function(listview) {
       listview.page.add_inner_button(__("Check and Create Counter"), function() {

        frappe.call({
                method: "snrg.snrg.doctype.counter.counter.create_counters",
                callback: function(response) {
                    console.log(response)
                }
        })
       })
    }
};