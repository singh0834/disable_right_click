import frappe

@frappe.whitelist()
def executejob():
    toDay = frappe.utils.nowdate()
    # currt_time = frappe.utils.nowtime().split(".")[0]
    activeUser = frappe.db.sql("select user from `tabSessions`")

    leadD = frappe.db.get_all("Lead Details",filters=[["stage","not in",["Trashed","Rejected"]],["lead_type","=","Fresh Lead"]],fields=["*"], order_by='creation desc')

    for ld in leadD:
        for usr in activeUser:
            leadCount = frappe.db.count("Lead",filters={"lead_owner":usr[0],"date":toDay})
            if(leadCount <= 29 and not frappe.db.exists('Lead',{"is_active_lead":1,"lead_owner":usr[0]}) and not frappe.db.exists('Lead',{"primary_contact_no":ld.primary_contact_no}) ):
                frappe.get_doc(dict(
                    doctype = 'Lead',
                    lead_details_name = ld.name,
                    lead_name = ld.lead_name,
                    lead_owner = usr[0],
                    email = ld.email,
                    primary_contact_no = ld.primary_contact_no,
                    stage = "New",
                    status = ld.status,
                    address = ld.address,
                    city_name = ld.city_name,
                    state_name = ld.state_name,
                    pin_code = ld.pin_code,
                    channel_id = ld.channel_id,
                    product_id = ld.product_id,
                    affiliate_id = ld.affiliate_id,
                    click_id = ld.click_id,
                )).insert()
                
                det = frappe.get_doc("Lead Details",ld.name)
                det.lead_type = "Already assigned"
                det.save()