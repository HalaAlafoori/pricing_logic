# pricing_logic/tasks.py

import frappe
from frappe.utils import nowdate

# this task run daily to desactivate expired discount codes
def deactivate_expired_discounts():
    # Get today's date
    today = nowdate()

    # Find all active coupons with expired end_date
    expired_discounts = frappe.get_all("Discount Code", filters={
        "active": 1,
        "end_date": ["<", today]
    })

    for discount in expired_discounts:
        discount_doc = frappe.get_doc("Discount Code", discount.name)
        discount_doc.active = 0  # Deactivate the coupon
        discount_doc.save()
        frappe.db.commit()  # Commit the changes
        frappe.log("Deactivated expired discount", discount.name)

