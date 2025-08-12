from playwright.sync_api import Page
from Automation.utils import constants, creds, local_data

def instant_appointment(page: Page, appointment: dict) -> None:

    page.get_by_role("tab", name="Scheduling").click()
    page.get_by_text("Appointments").click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Schedule Appointment").click()
    page.get_by_role("menuitem", name=constants.appointment[1]).click()
    
    page.get_by_role("heading", name=constants.appointment[1]).click()
    page.get_by_placeholder("Search & Select Patient").click()
    page.get_by_role("option", name=appointment.get("patient_name")).click()
    page.get_by_placeholder("Search Provider").click()
    page.get_by_placeholder("Search Provider").fill(local_data.provider1)
    page.get_by_role("option", name=local_data.provider1).click()
    page.locator("//p[text()='Reason for Visit']/ancestor::div[@class='MuiBox-root css-1hqz9cp']//textarea[@placeholder='Type here']").fill(appointment['cheif_complaint'])
    page.get_by_label("Note").fill(appointment.get("instant_appointment_note"))
    
    page.get_by_role("button", name="Create Appointment").click()
    page.get_by_text("Instant appointment book successfully").click()
    print("Instant appointment book successfully")
    
    page.get_by_role("button", name="Start Visit").click()
    
    page.wait_for_timeout(1000)
    # page.locator("//div[@aria-label='unmute']").click()
    # page.wait_for_timeout(1000)
    # page.locator("//div[@aria-label='mute']").click()
    # page.wait_for_timeout(1000)
    # page.locator("//div[@aria-label='unmute']").click()
    
    page.get_by_role("button", name="start camera").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="stop camera").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="start camera").click()
    page.wait_for_timeout(1000)
    
    page.get_by_text("Ready to join?").click()
    page.get_by_role("button", name="Start Appointment").click()
    
    page.get_by_text(f"{appointment.get('patient_name')} Appointment With Provider {local_data.provider1}").click()
    
    page.locator("//div[@aria-label='unmute']").click()
    page.wait_for_timeout(1000)
    page.locator("//div[@aria-label='mute']").click()
    page.wait_for_timeout(1000)
    page.locator("//div[@aria-label='unmute']").click()
    
    page.get_by_role("button", name="start camera").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="stop camera").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="start camera").click()
    
    page.get_by_test_id("RemoveOutlinedIcon").click()
    page.locator("//div[@aria-label='mute']").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="stop camera").click()
    page.wait_for_timeout(1000)
    page.get_by_test_id("FullscreenOutlinedIcon").click()
    
    page.get_by_role("button", name="Leave session").click()
    page.get_by_text("No Show", exact=True).click()
    page.get_by_text("Patient Didn't Joined the Call, are you want to Change the Status to No Show and").click()
    page.get_by_role("button", name="No").click()