from playwright.sync_api import Page
from Automation.utils import creds, data, local_data

def document(page: Page, document: dict):
    # DOCUMENTS
    page.get_by_role("tab", name="Documents").click()
    # Upload Document
    page.get_by_role("button", name="Upload Document").click()
    page.locator("//p[contains(text(), 'Document Tag')]/following::div[1]//input[@placeholder='Select Tag']").click()
    page.get_by_role("option", name=document["document_type1"]).click()
    page.get_by_placeholder("Choose Date").fill("12-27-2024")
    page.get_by_placeholder("Enter Title").fill(document["document_description1"])
    
    file_input = page.query_selector('input[type="file"]')
    file_path = "./Automation/utils/uploads/WorkplaceLabReport.jpg"
    file_input.set_input_files(file_path)
    
    page.get_by_role("button", name="Upload").click()
    page.get_by_text("Patient document uploaded successfully").click()
    page.wait_for_timeout(1500)
    
    page.get_by_role("cell", name=document["document_description1"]).click()
    page.get_by_role("cell", name=document["document_type1"]).click()
    # page.get_by_role("cell", name="Jpeg").click()
    page.get_by_role("cell", name=local_data.provider1).click()
    page.get_by_role("cell", name=data.formatted_date).click()
    
    # View
    page.get_by_test_id("MoreVertIcon").click()
    page.get_by_role("menuitem", name="View").click()
    page.get_by_text("Preview Document").click()
    page.wait_for_timeout(3000)
    page.get_by_role("button", name="Close").click()
    
    # Share To Patient
    page.get_by_test_id("MoreVertIcon").click()
    page.get_by_role("menuitem", name="Share To Patient").click()
    page.get_by_text("Document Successfully Share To Patient").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Okay").click()
    page.get_by_test_id("MoreVertIcon").click()

    # Edit
    page.get_by_role("menuitem", name="Edit").click()
    
    if(page.locator("//p[contains(text(), 'Document Tag')]/following::div[1]//input[@placeholder='Select Tag']").input_value()==document["document_type1"] and page.get_by_placeholder("Choose Date").input_value()=="12-27-2024" and page.get_by_placeholder("Enter Title").input_value()==document["document_description1"]):
        print("condition 1 passed")
        page.locator("//p[contains(text(), 'Document Tag')]/following::div[1]//input[@placeholder='Select Tag']").click()
        page.get_by_role("option", name=document["document_type2"]).click()
        page.get_by_placeholder("Choose Date").fill("01-20-2025")
        page.get_by_placeholder("Enter Title").fill(document["document_description2"])

        file_input = page.query_selector('input[type="file"]')
        file_path = "./Automation/utils/uploads/labresult.png"
        file_input.set_input_files(file_path)

        page.get_by_role("button", name="Upload").click()
        page.get_by_text("Document updated successfully").click()
        page.wait_for_timeout(1500)
    else:
        print("condition 1 failed")
    page.get_by_role("combobox", name="Select Tag").click()
    page.get_by_role("option", name="Surgery Reports").click()

    page.get_by_role("cell", name=document["document_description2"]).click()
    page.get_by_role("cell", name=document["document_type2"]).click()
    # page.get_by_role("cell", name="Jpeg").click()
    page.get_by_role("cell", name=local_data.provider1).click()
    page.get_by_role("cell", name=data.formatted_date).click()
    
    # View
    page.get_by_test_id("MoreVertIcon").click()
    page.get_by_role("menuitem", name="View").click()
    page.get_by_text("Preview Document").click()
    page.wait_for_timeout(3000)
    page.get_by_role("button", name="Close").click()

    # Edit
    page.get_by_test_id("MoreVertIcon").click()
    page.get_by_role("menuitem", name="Edit").click()
    if(page.locator("//p[contains(text(), 'Document Tag')]/following::div[1]//input[@placeholder='Select Tag']").input_value()==document["document_type2"] and page.get_by_placeholder("Choose Date").input_value()=="01-20-2025" and page.get_by_placeholder("Enter Title").input_value()==document["document_description2"]):
        print("condition 2 passed")
        page.get_by_role("heading", name="Upload").get_by_test_id("CloseIcon").click()
    else:
        print("condition 2 failed")
    # Delete
    page.get_by_test_id("MoreVertIcon").click()
    page.get_by_role("menuitem", name="Delete").click()
    page.get_by_text("Are You Sure?").click()
    page.get_by_text("you want to delete this Document").click()
    page.get_by_role("button", name="Yes,Sure").click()
    page.get_by_text("Document archived successfully").click()
    print("Document Module : PASS")