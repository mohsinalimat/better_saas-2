import frappe

@frappe.whitelist(allow_guest=True)
def fetch_site_by_email(email):
    try:
        domains = list(set([x.get("parent") for x in frappe.get_list('User Details', filters={'emai_id': email}, fields=['parent'])]))
        return ["app.onehash.ai"] + domains
    except:
        return []