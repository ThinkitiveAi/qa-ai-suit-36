from playwright.sync_api import Page
from Automation.utils import data

def diagnosis(page: Page, diagnosis: dict):
    page.get_by_role("tab", name="Diagnoses").click()
    # Add Diagnosis
    page.get_by_role("button", name="Add Diagnosis").click()
    
    page.get_by_placeholder("Select or Search Diagnosis").fill(diagnosis.get("code1"))
    page.get_by_role("option", name=f"{diagnosis.get('code1')} - {diagnosis.get('problem1')}", exact=True).click()

    page.locator("//input[@name='active']").click()
    page.get_by_role("option", name=diagnosis.get("status1"), exact=True).click()
    
    page.get_by_placeholder("Select").nth(2).click()
    page.get_by_role("option", name=diagnosis.get("type1")).click()
    
    page.get_by_placeholder("Choose Date").click()
    page.get_by_placeholder("Choose Date").fill("02-15-2021")
    
    page.get_by_placeholder("Type here").fill(diagnosis.get("note1"))
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Diagnosis added successfully").click()
    # verification
    page.get_by_role("cell", name=f"{diagnosis.get('code1')} - {diagnosis.get('problem1')}").click()
    page.get_by_role("cell", name=diagnosis.get("type1")).first.click()
    page.get_by_role("cell", name="02/15/2021").first.click()
    page.get_by_role("cell", name=data.formatted_date).first.click()
    page.get_by_role("cell", name=diagnosis.get("status1"), exact=True).first.click()
    page.get_by_role("cell", name=diagnosis.get("note1")).click()
    page.get_by_test_id("MoreVertIcon").first.click()
    
    # Edit Diagnosis
    page.get_by_role("menuitem", name="Edit").click()
    page.get_by_placeholder("Select or Search Diagnosis").fill(diagnosis.get("code2"))
    page.get_by_role("option", name=f"{diagnosis.get('code2')} - {diagnosis.get('problem2')}", exact=True).click()
    page.locator("input[name=\"active\"]").click()
    page.get_by_role("option", name=diagnosis.get("status2"), exact=True).click()
    page.get_by_placeholder("Select").nth(2).click()
    page.get_by_role("option", name=diagnosis.get("type2")).click()
    page.get_by_placeholder("Choose Date").click()
    page.get_by_placeholder("Choose Date").fill("04-20-2022")
    page.get_by_placeholder("Type here").click()
    page.get_by_placeholder("Type here").press("Control+a")
    page.get_by_placeholder("Type here").fill(diagnosis.get("note2"))
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Diagnosis updated successfully").click()
    # verification
    page.get_by_role("cell", name=f"{diagnosis.get('code2')} - {diagnosis.get('problem2')}").click()
    page.get_by_role("tooltip", name=diagnosis.get("problem2")).get_by_text(diagnosis.get("problem2")).click()
    page.get_by_role("cell", name=diagnosis.get("type2")).first.click()
    page.get_by_role("cell", name="04/20/2022").first.click()
    page.get_by_role("cell", name=data.formatted_date).first.click()
    page.get_by_role("cell", name=diagnosis.get("status2"), exact=True).first.click()
    page.get_by_role("cell", name=diagnosis.get("note2")).click()
    page.get_by_test_id("MoreVertIcon").first.click()

    # Delete Diagnosis
    page.get_by_role("menuitem", name="Delete").click()
    page.get_by_text("Are You Sure?").click()
    page.get_by_text("you want to delete this Diagnosis").click()
    page.get_by_role("button", name="Yes,Sure").click()
    page.get_by_text("Diagnosis archived successfully").click()
    print("Diagnosis Module : PASS")