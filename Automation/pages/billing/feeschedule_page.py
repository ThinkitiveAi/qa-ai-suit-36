from playwright.sync_api import Page

from Automation.utils import creds, data

def feeschedule(page: Page) -> None:
    #Go to Feeschedule
    page.get_by_role("tab", name="Billing").click()
    page.get_by_text("Fee Schedule").click()

    #Add feeschedule(CPT)
    page.get_by_text("Add Fee Schedule").click()
    page.wait_for_timeout(3000)
    
    # Use the exact selector for the Search Provider field
    # Based on the HTML structure: <input placeholder="Search Provider" ...>
    search_provider = page.locator('input[placeholder="Search Provider"]').first
    search_provider.wait_for(state="visible")
    search_provider.click(force=True)
    print("Is visible:", search_provider.is_visible())

    # Fill the provider field and select Julie Mark
    search_provider.fill("Julie Mark")
    page.get_by_role("option", name="Julie Mark").click()
    
    # Now select Code Type
    code_type_input = page.locator('input[placeholder="Select Code Type"]').first
    code_type_input.click()
    page.get_by_role("option", name="CPT").click()
    
    # Select Procedure Code
    procedure_input = page.locator('input[placeholder="Select Procedure Code"]').first
    procedure_input.click()
    page.get_by_role("option", name="99212 - Initial visit").click()

    page.locator("//input[@name='modifier.[0]']").fill("AA")
    page.locator("//input[@name='modifier.[1]']").fill("BA")
    page.locator("//input[@name='modifier.[2]']").fill("CA")
    page.locator("//input[@name='modifier.[3]']").fill("DA")
    page.wait_for_timeout(1000)

    page.get_by_placeholder(text="Enter NDC Code").fill("00777-3105-02")
    page.get_by_placeholder(text="Enter Amount").fill("5")
    page.get_by_placeholder(text="Enter NDC Quantity").fill("10")
    for _ in range(3):
        page.locator("//input[@class='PrivateSwitchBase-input MuiSwitch-input css-1m9pwf3']").click()
    page.get_by_placeholder(text="Description").fill("Test feeschedule description")
    page.get_by_role("button", name="Save").click()

    #Add feeschedule(HCPCS)
    page.get_by_text("Add New Fee Schedule").click()
    page.get_by_placeholder(text="Search Provider").click()
    page.get_by_role("option", name="Dennis Greco").click()
    page.get_by_placeholder(text="Select Code Type").click()
    page.get_by_role("option", name="HCPCS").click()
    page.get_by_placeholder(text="Select Procedure Code").click()
    page.get_by_role("option", name="G80650 - Supplies for maintenance of insulin infusion catheter, per week").click()

    page.locator("//input[@name='modifier.[0]']").fill("AA")
    page.locator("//input[@name='modifier.[1]']").fill("BA")
    page.locator("//input[@name='modifier.[2]']").fill("CA")
    page.locator("//input[@name='modifier.[3]']").fill("DA")
    
    page.get_by_placeholder(text="Enter NDC Code").fill("00777-3105-02")

    for _ in range(3):
        page.locator("//input[@class='PrivateSwitchBase-input MuiSwitch-input css-1m9pwf3']").click()

    page.get_by_placeholder(text="Enter Amount").fill("5")
    page.get_by_placeholder(text="Enter NDC Quantity").fill("10")
    page.get_by_placeholder(text="Description").fill("Test feeschedule description")
    page.get_by_role("button", name="Save").click()

    #View feeschedule (CPT)
    page.get_by_role("row", name= "99212 - Initial visit").get_by_test_id("MoreVertIcon").first.click()
    page.get_by_role("menuitem", name="View").click()
    page.get_by_text("View Fee Schedule").click()
    page.get_by_test_id("CloseIcon").click()
    page.wait_for_timeout(1000)
    #View feeschedule (HCPCS)
    page.locator("(//span[starts-with(text(), 'G80650 - Supplies for mainte')]/following::div[@class='MuiBox-root css-gmuwbf'])[1]").click()
    page.get_by_role("menuitem", name="View").click()
    page.get_by_text("View Fee Schedule").click()
    page.get_by_test_id("CloseIcon").click()
    
    #Edit feeschedule(CPT)
    page.get_by_role("row", name= "99212 - Initial visit").get_by_test_id("MoreVertIcon").first.click()
    page.get_by_role("menuitem", name="Edit").click()

    page.get_by_placeholder(text="Search Provider").clear()
    page.get_by_placeholder(text="Search Provider").click()
    page.get_by_role("option", name="Dennis Greco").click()
    page.get_by_placeholder(text="Select Code Type").clear()
    page.get_by_placeholder(text="Select Code Type").click()
    page.get_by_role("option", name="CPT").click()
    page.get_by_placeholder(text="Select Procedure Code").clear()
    page.get_by_placeholder(text="Select Procedure Code").click()
    page.get_by_role("option", name="99212 - Initial visit").click()

    page.locator("//input[@name='modifier.[0]']").fill("DA")
    page.locator("//input[@name='modifier.[1]']").fill("CA")
    page.locator("//input[@name='modifier.[2]']").fill("BA")
    page.locator("//input[@name='modifier.[3]']").fill("AA")
    page.wait_for_timeout(1000)

    page.get_by_placeholder(text="Enter NDC Code").fill("55000-4105-30")
    page.get_by_placeholder(text="Enter Amount").fill("10")
    page.get_by_placeholder(text="Enter NDC Quantity").fill("5")
    for _ in range(3):
        page.locator("//input[@class='PrivateSwitchBase-input MuiSwitch-input css-1m9pwf3']").click()
    page.get_by_placeholder(text="Description").fill("Test Edit feeschedule description")
    page.get_by_role("button", name="Save").click()

    # Edit feeschedule(HCPCS)
    page.locator("(//span[starts-with(text(), 'G80650 - Supplies for mainte')]/following::div[@class='MuiBox-root css-gmuwbf'])[1]").click()
    page.get_by_role("menuitem", name="Edit").click()
    page.get_by_placeholder(text="Search Provider").clear()
    page.get_by_placeholder(text="Search Provider").click()
    page.get_by_role("option", name="Dennis Greco").click()
    page.get_by_placeholder(text="Select Code Type").clear()
    page.get_by_placeholder(text="Select Code Type").click()
    page.get_by_role("option", name="HCPCS").click()
    page.get_by_placeholder(text="Select Procedure Code").clear()
    page.get_by_placeholder(text="Select Procedure Code").click()
    page.get_by_role("option", name="G80650 - Supplies for maintenance of insulin infusion catheter, per week").click()

    page.locator("//input[@name='modifier.[0]']").fill("DA")
    page.locator("//input[@name='modifier.[1]']").fill("CA")
    page.locator("//input[@name='modifier.[2]']").fill("BA")
    page.locator("//input[@name='modifier.[3]']").fill("AA")
    
    page.get_by_placeholder(text="Enter NDC Code").fill("77000-3105-02")

    for _ in range(3):
        page.locator("//input[@class='PrivateSwitchBase-input MuiSwitch-input css-1m9pwf3']").click()

    page.get_by_placeholder(text="Enter Amount").fill("10")
    page.get_by_placeholder(text="Enter NDC Quantity").fill("5")
    page.get_by_placeholder(text="Description").fill("Test edit feeschedule description")
    page.get_by_role("button", name="Save").click()

    #Delete feeschedule(CPT)
    page.get_by_role("row", name= "99212 - Initial visit").get_by_test_id("MoreVertIcon").first.click()
    page.get_by_role("menuitem", name="Delete").click()
    page.get_by_role("button", name="Yes,Sure").click()

    #Delete feeschedule(HCPCS)
    page.locator("(//span[starts-with(text(), 'G80650 - Supplies for mainte')]/following::div[@class='MuiBox-root css-gmuwbf'])[1]").click()
    page.get_by_role("menuitem", name="Delete").click()
    page.get_by_role("button", name="Yes,Sure").click()

    return page