# pricing_logic/tasks.py

import frappe
from frappe.utils import nowdate

# this task run daily to desactivate expired coupon codes
def deactivate_expired_coupons():
    # Get today's date
    today = nowdate()

    # Find all active coupons with expired end_date
    expired_coupons = frappe.get_all("Coupon Code", filters={
        "active": 1,
        "end_date": ["<", today]
    })

    for coupon in expired_coupons:
        coupon_doc = frappe.get_doc("Coupon Code", coupon.name)
        coupon_doc.active = 0  # Deactivate the coupon
        coupon_doc.save()
        frappe.db.commit()  # Commit the changes
        frappe.log("Deactivated expired coupon", coupon.name)

