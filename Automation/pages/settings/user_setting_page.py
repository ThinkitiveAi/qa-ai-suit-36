from playwright.sync_api import Page

def staff_user(page: Page, user: dict):
    page.get_by_role("tab", name="Settings").click()
    # User Settings
    page.get_by_text("User Settings").click()
    # Users
    page.get_by_role("tab", name="Users").click()
    page.get_by_role("button", name="Add Staff User").click()
    page.get_by_role("heading", name="Add Staff User").get_by_text("Add Staff User").click()
    
    page.get_by_placeholder("Enter First Name").fill(user.get("user_fname"))
    page.get_by_placeholder("Enter Last Name").fill(user.get("user_lname"))
    print("Staff User Name :", user.get("user_fname"), user.get("user_lname"))
    page.get_by_placeholder("YY-MM-DD").fill(user.get("user_dob"))
    page.locator("(//input[@placeholder='Select'])[1]").click()
    page.get_by_role("option", name=user.get("user_gender"), exact=True).click()
    page.get_by_placeholder("Enter Email").fill(user.get("user_email"))
    page.get_by_placeholder("Enter Contact Number").fill(user.get("user_contact_num"))
    page.get_by_placeholder("Select Role", exact=True).click()
    page.get_by_role("option", name=user.get("user_role")).click()
    page.locator("(//input[@placeholder='Select'])[2]").click()
    page.get_by_role("option", name=user.get("user_location")).click()
    
    page.get_by_role("button", name="Save").click()
    page.wait_for_timeout(1000)
    # verification
    page.get_by_placeholder("Search").click()
    page.get_by_placeholder("Search").fill(user.get("user_fname"), user.get("user_lname"))
    page.get_by_role("heading", name=f"{user.get('user_fname')} {user.get('user_lname')}").click()
    page.get_by_text(user.get("user_contact_num")).click()
    page.get_by_text(user.get("user_email")).click()
    # View Profile
    page.get_by_role("button", name="View Profile").click()
    page.get_by_title("User Profile").get_by_text(f"{user.get('user_fname')} {user.get('user_lname')}").click()
    page.get_by_title("User Profile").get_by_text(user.get("user_email")).click()
    page.get_by_text(user.get("user_dob")).click()
    page.get_by_text(user.get("user_gender")).click()
    page.get_by_text(user.get("user_contact_num")).click()
    page.get_by_text(user.get("user_role")).click()
    page.get_by_test_id("CloseIcon").click()
    
    # Edit Profile
    page.get_by_role("button", name="Edit Profile").click()
    page.get_by_placeholder("Enter First Name").fill(user.get("edit_user_fname"))
    page.get_by_placeholder("Enter Last Name").fill(user.get("edit_user_lname"))
    print("Staff User Name :", user.get("edit_user_fname"), user.get("edit_user_lname"))
    page.get_by_placeholder("YY-MM-DD").fill(user.get("edit_user_dob"))
    page.locator("(//input[@placeholder='Select'])[1]").click()
    page.get_by_role("option", name=user.get("edit_user_gender"), exact=True).click()
    page.get_by_placeholder("Enter Email").fill(user.get("edit_user_email"))
    page.get_by_placeholder("Enter Contact Number").fill(user.get("edit_user_contact_num"))
    page.get_by_placeholder("Select Role", exact=True).click()
    page.get_by_role("option", name=user.get("edit_user_role")).click()
    
    page.get_by_role("button", name="Save").click()
    page.wait_for_timeout(1000)
    
    # View Profile
    page.get_by_role("button", name="View Profile").click()
    page.get_by_title("User Profile").get_by_text(f"{user.get('edit_user_fname')} {user.get('edit_user_lname')}").click()
    page.get_by_title("User Profile").get_by_text(user.get("edit_user_email")).click()
    page.get_by_text(user.get("edit_user_dob")).click()
    page.get_by_text(user.get("edit_user_gender")).click()
    page.get_by_text(user.get("edit_user_contact_num")).click()
    page.get_by_text(user.get("edit_user_role")).click()
    page.get_by_test_id("CloseIcon").click()


# Bug----> https://medarch.atlassian.net/browse/ECRH-1936