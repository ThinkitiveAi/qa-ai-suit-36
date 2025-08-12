from playwright.sync_api import Page
    
def catalog(page: Page):
    # LIBRARY
    page.get_by_role("tab", name="Library").click()
    # Catalog
    page.get_by_text("Catalog").click()
    # Diagnosis Code
    page.get_by_role("tab", name="Diagnosis Code Catalog").click()
    # Add Diagnosis Code
    page.get_by_role("button", name="Add Diagnosis Code").click()
    page.get_by_placeholder("Select").click()
    page.get_by_role("option", name="ICD 10").click()
    page.get_by_placeholder("Enter Code").click()
    page.get_by_placeholder("Enter Code").fill("AF844")
    page.get_by_placeholder("Description").click()
    page.get_by_placeholder("Description").fill("test code")
    page.get_by_role("button", name="Add").click()
    page.get_by_text("ICD code added successfully.").click()
    page.get_by_role("row", name="ICD 10 AF844 test code").get_by_text("ICD 10").click()
    page.get_by_text("AF844").click()
    
    # Edit
    page.get_by_role("row", name="ICD 10 AF844 test code").get_by_test_id("MoreVertIcon").click()
    page.get_by_role("menuitem", name="Edit").click()
    page.get_by_placeholder("Select").click()
    page.get_by_role("option", name="ICD 11").click()
    page.get_by_placeholder("Enter Code").click()
    page.get_by_placeholder("Enter Code").fill("SP756")
    page.get_by_placeholder("Description").click()
    page.get_by_placeholder("Description").fill("demo code")
    page.get_by_role("button", name="Edit").click()
    page.get_by_role("row", name="ICD 11 SP756 demo code").get_by_text("ICD 11").click()
    page.get_by_text("SP756").click()
    
    # Delete
    page.get_by_role("row", name="ICD 11 SP756 demo code").get_by_test_id("MoreVertIcon").click()
    page.get_by_role("menuitem", name="Delete").click()
    page.get_by_text("Are You Sure?").click()
    page.get_by_role("button", name="Yes,Sure").click()
    page.get_by_text("ICD code archived successfully.").click()
    
    # CPT Code Catalog
    page.get_by_role("tab", name="CPT Code Catalog").click()
    # Add CPT Code
    page.get_by_role("button", name="Add CPT Code").click()
    page.get_by_placeholder("Enter Code").click()
    page.get_by_placeholder("Enter Code").fill("CPT123")
    page.get_by_placeholder("Description").click()
    page.get_by_placeholder("Description").fill("test CPT")
    page.get_by_role("button", name="Add").click()
    page.get_by_text("CPT code added successfully.").click()
    page.get_by_text("CPT123").click()
    page.get_by_text("test CPT").click()
    
    # Edit
    page.get_by_role("row", name="CPT123 test CPT").get_by_test_id("MoreVertIcon").click()
    page.get_by_role("menuitem", name="Edit").click()
    page.get_by_placeholder("Enter Code").click()
    page.get_by_placeholder("Enter Code").fill("CPT456")
    page.get_by_placeholder("Description").click()
    page.get_by_placeholder("Description").fill("demo CPT")
    page.get_by_role("button", name="Edit").click()
    page.get_by_text("CPT code updated successfully.").click()
    page.get_by_text("CPT456").click()
    page.get_by_text("demo CPT").click()
    
    # Delete
    page.get_by_role("row", name="CPT456 demo CPT").get_by_test_id("MoreVertIcon").click()
    page.get_by_role("menuitem", name="Delete").click()
    page.get_by_text("Are You Sure?").click()
    page.get_by_role("button", name="Yes,Sure").click()
    page.get_by_text("CPT code archived successfully.").click()
    
    # HCPCS Code Catalog
    page.get_by_role("tab", name="HCPCS Code Catalog").click()
    # Add HCPCS Code
    page.get_by_role("button", name="Add HCPCS Code").click()
    page.get_by_placeholder("Enter Code").click()
    page.get_by_placeholder("Enter Code").fill("HP875")
    page.get_by_placeholder("Description").click()
    page.get_by_placeholder("Description").fill("test HCPCS")
    page.get_by_role("button", name="Add").click()
    page.get_by_text("HCPCS code added successfully").click()
    page.get_by_text("HP875").click()
    page.get_by_text("test HCPCS").click()
    
    # Edit
    page.get_by_role("row", name="HP875 test HCPCS").get_by_test_id("MoreVertIcon").click()
    page.get_by_role("menuitem", name="Edit").click()
    page.get_by_placeholder("Enter Code").click()
    page.get_by_placeholder("Enter Code").fill("HP965")
    page.get_by_placeholder("Description").click()
    page.get_by_placeholder("Description").fill("Demo HCPCS")
    page.get_by_role("button", name="Edit").click()
    page.get_by_text("HCPCS code updated successfully").click()
    page.get_by_text("HP965").click()
    page.get_by_text("Demo HCPCS").click()
    
    # Delete
    page.get_by_role("row", name="HP965 Demo HCPCS").get_by_test_id("MoreVertIcon").click()
    page.get_by_role("menuitem", name="Delete").click()
    page.get_by_text("Are You Sure?").click()
    page.get_by_text("you want to delete this HCPCS Code").click()
    page.get_by_role("button", name="Yes,Sure").click()
    page.get_by_text("HCPCS code archived successfully").click()
    
    # LOINC Code Catalog
    page.get_by_role("tab", name="LOINC Code Catalog").click()
    # Add LOINC Code
    page.get_by_role("button", name="Add LOINC Code").click()
    page.get_by_placeholder("Enter Code").click()
    page.get_by_placeholder("Enter Code").fill("LO123")
    page.get_by_placeholder("Description").click()
    page.get_by_placeholder("Description").fill("Test LOINC")
    page.get_by_role("button", name="Add").click()
    page.get_by_text("LOINC code added successfully").click()
    
    # Edit
    page.get_by_role("row", name="LO123 Test LOINC").get_by_test_id("MoreVertIcon").click()
    page.get_by_role("menuitem", name="Edit").click()
    page.get_by_placeholder("Enter Code").click()
    page.get_by_placeholder("Enter Code").fill("LO456")
    page.get_by_placeholder("Description").click()
    page.get_by_placeholder("Description").fill("Demo LOINC")
    page.get_by_role("button", name="Edit").click()
    page.get_by_text("LOINC code updated successfully.").click()
    page.get_by_text("LO456").click()
    page.get_by_text("Demo LOINC").click()
    
    # Delete
    page.get_by_role("row", name="LO456 Demo LOINC").get_by_test_id("MoreVertIcon").click()
    page.get_by_role("menuitem", name="Delete").click()
    page.get_by_text("Are You Sure?").click()
    page.get_by_text("you want to delete this LOINC Code").click()
    page.get_by_role("button", name="Yes,Sure").click()
    page.get_by_text("LOINC code archived successfully.").click()
    page.wait_for_timeout(1000)