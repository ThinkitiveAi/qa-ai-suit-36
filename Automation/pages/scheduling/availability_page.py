from playwright.sync_api import Page

from Automation.utils import constants, creds, data, local_data


def availability(page: Page) -> None:
    
    page.get_by_role("tab", name="Scheduling").click()
    page.get_by_text("Availability").click()
    page.get_by_role("heading", name="Availability").click()
    
    page.get_by_role("button", name="Edit Availability").click()
    page.get_by_role("combobox", name="Select Provider").click()
    page.get_by_role("button", name="Clear").click()
    page.get_by_role("option", name=local_data.provider1).click()
    page.locator("input[name=\"timezone\"]").click()
    page.get_by_role("option", name="Indian Standard Time (UTC +5:30)").click()
    page.locator("input[name=\"bookingWindow\"]").click()
    page.get_by_role("option", name="1 Week", exact=True).click()
    # Day Slot Creation
    page.locator("//input[@class='PrivateSwitchBase-input MuiSwitch-input css-1m9pwf3']").click()
    page.get_by_role("tab", name=data.weekday).click()
    page.get_by_text("Time Slots").click()
    page.locator("(//input[@placeholder='Select'])[3]").click()    # start time 
    page.get_by_role("option", name=data.time[0]).click()
    page.locator("(//input[@placeholder='Select'])[4]").click()    # end time 
    page.get_by_role("option", name=data.time[4], exact=False).click()
    page.get_by_role("checkbox", name=constants.visit_type[1]).check()        # virtual
    
    # # Add Time Slot
    # page.get_by_role("button", name="Add Time Slot").click()
    # page.locator("(//input[@placeholder='Select'])[6]").click()    # start time 
    # page.get_by_role("option", name="01:00 AM", exact=True).click()
    # page.locator("(//input[@placeholder='Select'])[7]").click()    # end time 
    # page.get_by_role("option", name="03:00 AM (2 hrs)").click()
    # page.locator("(//input[@placeholder='Select'])[8]").click()    # location 
    # page.get_by_role("option", name=local_data.pg_location1).click()

    # Availability Settings
    page.get_by_role("heading", name="Availability Settings", exact=True).click()
    page.locator("(//p[text()='Duration']/following::input[@placeholder='Select Time'])[1]").click()
    page.get_by_role("option", name="15 minutes").click()
    page.locator("//p[text()='Add More']").click()
    
    page.locator("(//h4[text()='Availability Settings']/following::p[text()='Appointment Type']/following::input[@placeholder='Appointment Type'])[2]").click()
    page.get_by_role("option", name=constants.appointment_type[1]).click()
    page.locator("(//p[text()='Duration']/following::input[@placeholder='Select Time'])[2]").click()
    page.get_by_role("option", name="15 minutes").click()
    
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Save").click()
    page.get_by_text(f"Availability added successfully for provider {local_data.provider1}").click()
    page.wait_for_timeout(1000)
    print(f"Availability added successfully for provider {local_data.provider1}")
    print(f"slots: {data.time[0]} - {data.time[4]}" )
    
    page.get_by_placeholder("Visit Mode").click()
    page.get_by_role("option", name=constants.visit_type[1]).click()
    page.get_by_placeholder("Appointment Type").click()
    page.get_by_role("option", name=constants.appointment_type[0]).click()
    
    buttons = page.locator(f"//button[text()='{data.day.zfill(2)}']")
    count = buttons.count()
    for i in range(count):
        if not buttons.nth(i).is_disabled():
            page.locator(f"(//button[text()='{data.day.zfill(2)}']/following::p[contains(text(), 'Slots Available')])[1]").click()
            page.locator(f"//p[text()='Available Slots {data.day} {data.month_name}']").click(click_count=3)
            break
    page.wait_for_timeout(500)
    page.get_by_test_id("CloseIcon").nth(5).click()
    return page