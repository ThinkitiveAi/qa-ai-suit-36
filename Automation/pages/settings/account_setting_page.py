from playwright.sync_api import Page
from Automation.utils import creds, local_data

def edit_profile(page: Page, accountProfile: dict):
    page.get_by_role("tab", name="Settings").click()
    page.get_by_text("Account Settings").click()
    page.get_by_role("button", name="Edit Profile").click()
    
    # Edit Profile
    page.locator("input[name=\"npi\"]").fill(accountProfile.get("npi_number"))
    page.get_by_placeholder("Enter Contact Number").type(accountProfile.get("contact_num"))
    page.locator("input[name=\"officeFaxNumber\"]").fill(accountProfile.get("fax_num"))
    page.get_by_placeholder("Enter Year Of Experience").fill(accountProfile.get("yearOfExperience"))
    page.locator("input[name=\"taxonomyNumber\"]").fill(accountProfile.get("taxonomy_num"))
    
    page.locator("(//input[@placeholder='Select'])[6]").click()
    page.get_by_role("option", name=accountProfile.get("state"))
    page.locator("input[name=\"licenseNumber\"]").fill(accountProfile.get("license_num"))
    page.get_by_placeholder("Enter Expertise ").fill(accountProfile.get("expertise"))
    page.get_by_placeholder("Enter Education, Work Experience").fill(accountProfile.get("workExperience"))
    
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Provider updated successfully.").click()
    page.wait_for_timeout(1000)
    
    # verification
    page.get_by_text(local_data.provider1).click()
    page.get_by_text(accountProfile.get("contact_num")).click(click_count=3)
    page.get_by_text(creds.provider_email).click()
    # page.get_by_text("Role").click()
    # page.get_by_text("Provider", exact=True).click()
    # page.get_by_text("Provider Type").click()
    # page.get_by_text("MD").click()
    # page.get_by_text("Gender").click()
    # page.get_by_text("Male").click()
    page.get_by_text(accountProfile.get("npi_number")).click(click_count=3)
    page.get_by_text(accountProfile.get("fax_num")).click(click_count=3)
    page.get_by_text(accountProfile.get("taxonomy_num")).click(click_count=3)
    page.get_by_text(f"1. ({accountProfile.get('license_num')})").click(click_count=3)
    page.get_by_text(accountProfile.get("yearOfExperience"), exact=True).click(click_count=3)
    page.get_by_text(accountProfile.get("workExperience")).click(click_count=3)
