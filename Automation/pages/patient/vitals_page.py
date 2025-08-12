from playwright.sync_api import Page

def vitals(page: Page, vitals: list):
    # VITALS
    page.get_by_role("tab", name="Vitals").click()
    # Add Vitals
    page.get_by_role("button", name="Add Vitals").click()
    page.get_by_placeholder("Select Vitals").click()
    for vital in vitals:
        page.get_by_role("option", name=vital).click()
    page.get_by_role("heading", name="Add Vitals").get_by_text("Add Vitals").click()
    
    # Blood Pressure
    page.locator("input[name=\"patientVitals\\.0\\.systolic\"]").fill("118")
    page.locator("input[name=\"patientVitals\\.0\\.diastolic\"]").fill("78")
    page.locator("input[name=\"patientVitals\\.0\\.pulse\"]").fill("70")
    page.get_by_placeholder("sitting").click()
    page.get_by_role("option", name="Sitting").click()
    page.get_by_placeholder("l arm").click()
    page.get_by_role("option", name="L Arm").click()
    page.get_by_placeholder("adult").click()
    page.get_by_role("option", name="Small Adult").click()
    page.locator("input[name=\"patientVitals\\.0\\.flag\"]").click()
    page.get_by_role("option", name="Normal").click()
    # Blood Glucose
    page.locator("input[name=\"patientVitals\\.1\\.value\"]").fill("30")
    page.get_by_placeholder("Before Meal").click()
    page.get_by_role("option", name="Before Meal").click()
    page.get_by_placeholder("BreakFast").click()
    page.get_by_role("option", name="Breakfast").click()
    page.locator("input[name=\"patientVitals\\.1\\.flag\"]").click()
    page.get_by_role("option", name="Normal").click()
    # Body Temperature
    page.get_by_placeholder("F", exact=True).click()
    page.get_by_role("option", name="F").click()
    page.locator("input[name=\"patientVitals\\.2\\.value\"]").fill("99")
    page.get_by_placeholder("Oral").click()
    page.get_by_role("option", name="Oral").click()
    page.locator("input[name=\"patientVitals\\.2\\.flag\"]").click()
    page.get_by_role("option", name="Normal").click()
    # Heart Rate
    page.locator("input[name=\"patientVitals\\.3\\.value\"]").fill("75")
    page.locator("input[name=\"patientVitals\\.3\\.flag\"]").click()
    page.get_by_role("option", name="Normal").click()
    # Respiration Rate
    page.locator("input[name=\"patientVitals\\.4\\.value\"]").fill("22")
    page.locator("input[name=\"patientVitals\\.4\\.flag\"]").click()
    page.get_by_role("option", name="Normal").click()
    
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Vital created successfully").click()
    page.wait_for_timeout(1000)
    print("Vitals Module : PASS")