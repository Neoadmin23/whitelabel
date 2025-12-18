
# whitelabel/utils.py
import frappe

DEFAULT_LOGO = "/assets/whitelabel/images/whitelabel_logo.jpg"

def get_logo() -> str:
    """Return the app logo URL based on frappe.conf, falling back    """Return the app logo URL based on frappe.conf, falling back to default."""
    url = frappe.conf and frappe.conf.get("app_logo_url")
