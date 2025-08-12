import random
from playwright.sync_api import Playwright
from Automation.pages.settings.practice_setting_page import practiceSetting
from Automation.utils import constants, creds, data
from Automation.utils.browser import login, open_browser

def test_practiceSetting(playwright: Playwright):
    
    page = open_browser(playwright)
    credential = {
        "url": creds.url,
        "email": creds.email,
        "password": creds.password
    }
    login(page, credential)
    
    practice_data = {
        # edit provider group
        "pg_name2": f"{random.choice(constants.providerGroup_name)} {data.generate_random_string(4)}",
        "pg_groupNpiNumber2": data.generate_random_digits(10),
        "pg_contactNumber2": f"({data.generate_random_digits(3)}) {data.generate_random_digits(3)}-{data.generate_random_digits(4)}",
        "pg_email2": "abcdef+"+data.generate_random_digits(7)+"@mailinator.com",
        "pg_faxId2": data.generate_random_digits(6),
        "pg_website2": data.generate_random_website(),
        
        # add - location
        "loc_name": f"{random.choice(constants.us_cities)} {data.generate_random_string(3)}",
        "loc_Id": f"{data.generate_random_string(2)}{data.generate_random_digits(3)}",
        "loc_contact_num": f"({data.generate_random_digits(3)}) {data.generate_random_digits(3)}-{data.generate_random_digits(4)}",
        "loc_email": f"qwerty+{data.generate_random_digits(5)}@mailinator.com",
        "loc_fax": f"{data.generate_random_string(1)}{data.generate_random_digits(4)}",
        # edit - location
        "loc_name2": f"{random.choice(constants.us_cities)} {data.generate_random_string(3)}",
        "loc_Id2": f"{data.generate_random_string(2)}{data.generate_random_digits(3)}",
        "loc_contact_num2": f"({data.generate_random_digits(3)}) {data.generate_random_digits(3)}-{data.generate_random_digits(4)}",
        "loc_email2": f"asdfg+{data.generate_random_digits(5)}@mailinator.com",
        "loc_fax2": f"{data.generate_random_string(1)}{data.generate_random_digits(4)}",
        
        # Add Department
        "dept_name": f"{random.choice(constants.department_name_list)} {data.generate_random_digits(3)}",
        "dept_Id": f"{data.generate_random_string(2)}{data.generate_random_digits(3)}",
        "dept_contact_num": f"({data.generate_random_digits(3)}) {data.generate_random_digits(3)}-{data.generate_random_digits(4)}",
        # Edit Department
        "dept_name2": f"{random.choice(constants.department_name_list)} {data.generate_random_digits(3)}",
        "dept_Id2": f"{data.generate_random_string(2)}{data.generate_random_digits(3)}",
        "dept_contact_num2": f"({data.generate_random_digits(3)}) {data.generate_random_digits(3)}-{data.generate_random_digits(4)}",
        
        "staff_user": "Juliee Edwards",
        "staff_user1": "Chris Rock"
    }
    
    practiceSetting(page, practice_data)