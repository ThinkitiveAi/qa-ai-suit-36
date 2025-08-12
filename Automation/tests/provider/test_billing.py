import playwright
from Automation.pages.billing.billing_page import super_bill_from_encounter_billing
from Automation.pages.billing.feeschedule_page import feeschedule
from Automation.utils import creds, data
from Automation.utils.browser import login, open_browser

def test_order(playwright: playwright):

    page= open_browser(playwright)
    credential = {
        "url": creds.provider_url,
        "email": creds.provider_email,
        "password": creds.provider_password
    }

    login(page, credential)
    super_bill_from_encounter_billing(page, data.billing_data, data.patient_id)
    # feeschedule(page)

    