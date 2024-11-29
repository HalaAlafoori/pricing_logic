app_name = "pricing_logic"
app_title = "Pricing Logic"
app_publisher = "Momar Dia"
app_description = "Ab better pricing rules app"
app_email = "momar@boostwaydigital.com"
app_license = "agpl-3.0"

# Apps
# ------------------

# daily task to set expired coupons code to inactive
scheduler_events = {
    "daily": [
        "pricing_logic.scripts.pricing_logic_scripts.tasks.deactivate_expired_coupons"
    ]
}
