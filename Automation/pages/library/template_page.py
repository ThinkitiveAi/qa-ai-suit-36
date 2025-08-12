from playwright.sync_api import Page

from Automation.test_data import template_data
from Automation.utils import data, local_data

def template(page: Page, template) -> None:
    #Go to Template
    page.get_by_role("tab", name="Library").click()
    page.get_by_role("menuitem", name="Templates").click()

    #Create new template
    page.get_by_role("button", name="Create New Template").click()
    page.get_by_placeholder("Select Form Type").click()
    page.get_by_role("option", name=template).click()
    page.locator("//input[@name='speciality']").click()
    page.get_by_role("option", name=template_data.speciality_for_creation, exact=True).click()
    page.get_by_placeholder("Enter Value").fill(template_data.template_name1)
    print(template_data.template_name1)
    
    if template == template_data.templates[0]:
        for section, text in template_data.ros_template_data.items():
            page.locator(f"(//span[text()='{section}']/following::input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1o6z5ng'])[1]").fill(text)
    else: 
        for section, text in template_data.pe_template_data.items():
            page.locator(f"(//span[text()='{section}']/following::input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall css-1o6z5ng'])[1]").fill(text)
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Template created successfully").click()
    page.wait_for_timeout(300)
    page.get_by_title("Close").click()
    
    #View template
    page.get_by_placeholder("Search By Template Name").fill(template_data.template_name1)
    page.wait_for_timeout(1000)
    page.locator(f"//p[text()='{template}']/following::p[.='{template_data.template_name1}']/following::p[.='{template_data.speciality_for_creation}']/following::div[.='{local_data.provider1}']/following::div[.='{data.dt_format(data.current_date,'/')}']/following::div[@class='MuiBox-root css-gmuwbf']").click()
    page.get_by_role("menuitem", name="View").click()
    page.get_by_text("Preview").click()
    
    if template == template_data.templates[0]:
        for section, text in template_data.ros_template_data.items():
            page.locator(f"//span[text()='{section}']/following::input[@value='{text}']").is_disabled()
    else: 
        for section, text in template_data.pe_template_data.items():
            page.locator(f"//span[text()='{section}']/following::input[@value='{text}']").is_enabled()
    page.get_by_test_id("CloseIcon").click()

    # Edit template
    page.get_by_test_id("MoreVertIcon").click()
    page.get_by_role("menuitem", name="Update").click()
    page.query_selector("input[name='speciality']").hover()
    page.get_by_role("button", name="Clear").click()
    page.locator("//input[@name='speciality']").click()
    page.get_by_role("option", name=template_data.speciality_for_update, exact=True).click()
    page.get_by_placeholder("Enter Value").fill(template_data.template_name2)
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Template updated successfully").click()
    page.wait_for_timeout(300)
    page.get_by_title("Close").click()
    
    #View template
    page.get_by_placeholder("Search By Template Name").fill(template_data.template_name2)
    page.wait_for_timeout(1000)
    page.locator(f"//p[text()='{template}']/following::p[.='{template_data.template_name2}']/following::p[.='{template_data.speciality_for_update}']/following::div[.='{local_data.provider1}']/following::div[.='{data.dt_format(data.current_date,'/')}']/following::div[@class='MuiBox-root css-gmuwbf']").click()
    page.get_by_role("menuitem", name="View").click()
    page.get_by_text("Preview").click()
    
    if template == template_data.templates[0]:
        for section, text in template_data.ros_template_data.items():
            page.locator(f"//span[text()='{section}']/following::input[@value='{text}']").is_disabled()
    else: 
        for section, text in template_data.pe_template_data.items():
            page.locator(f"//span[text()='{section}']/following::input[@value='{text}']").is_disabled()
    page.get_by_test_id("CloseIcon").click()
    
    #Delete template
    page.get_by_placeholder("Search By Template Name").fill(template_data.template_name2)
    page.wait_for_timeout(1000)
    page.get_by_test_id("MoreVertIcon").click()
    page.get_by_role("menuitem", name="Delete").click()
    page.get_by_role("button", name= "Yes,Sure").click()