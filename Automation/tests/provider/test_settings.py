from playwright.sync_api import Playwright
from Automation.pages.settings.account_setting_page import edit_profile
from Automation.pages.settings.provider_setting_page import provider_user
from Automation.pages.settings.user_setting_page import staff_user
from Automation.utils import creds, local_data
from Automation.utils import data
from Automation.utils.browser import login, open_browser

def test_settings(playwright: Playwright):
    page = open_browser(playwright)
    
    credential = {
        "url": creds.provider_url,
        "email": creds.provider_email,
        "password": creds.provider_password
    }
    login(page, credential)
    
    
    account_profile_data = {
        "npi_number": data.generate_random_digits(10),
        "contact_num": f"({data.generate_random_digits(3)}) {data.generate_random_digits(3)}-{data.generate_random_digits(4)}",
        "fax_num": data.generate_random_digits(5),
        "yearOfExperience": "10",
        "taxonomy_num": data.generate_random_digits(6),
        "state": "Alaska (AK)",
        "license_num": data.generate_random_digits(10),
        "expertise": "Cardiology & Hypertension Management",
        "workExperience": "Experienced healthcare provider skilled in patient care, diagnosis, and treatment of acute and chronic conditions."
    }
    edit_profile(page, account_profile_data)
    
    
    user_data = {
        # add
        "user_fname": data.fake.first_name_male(),
        "user_lname": data.fake.last_name(),
        "user_dob": "10-28-1987",
        "user_gender": "Male",
        "user_email": None,
        "user_contact_num": f"({data.generate_random_digits(3)}) {data.generate_random_digits(3)}-{data.generate_random_digits(4)}",
        "user_role": "Biller",
        "user_location": local_data.pg_location,
        
        # edit
        "edit_user_fname": data.fake.first_name_female(),
        "edit_user_lname": data.fake.last_name(),
        "edit_user_dob": "11-25-1988",
        "edit_user_gender": "Female",
        "edit_user_email": None,
        "edit_user_contact_num": f"({data.generate_random_digits(3)}) {data.generate_random_digits(3)}-{data.generate_random_digits(4)}",
        "edit_user_role": "Nurse",
    }
    user_data["user_email"] = f"{user_data['user_fname']}+{data.generate_random_digits(5)}@mailinator.com"
    staff_user(page, user_data)
    
    
    provider_data = {
        # add
        "fname": data.fake.first_name_female(),
        "lname": data.fake.last_name(),
        "role": "Therapist",
        "dob": "12-20-1988",
        "gender": "Female",
        "npi_number": data.generate_random_digits(10),
        "contact_num": f"({data.generate_random_digits(3)}) {data.generate_random_digits(3)}-{data.generate_random_digits(4)}",
        "fax_num": data.generate_random_digits(5),
        "yearOfExperience": "10",
        "taxonomy_num": data.generate_random_digits(6),
        "email": None,
        "state": "Alaska (AK)",
        "license_num": data.generate_random_digits(10),
        "bio": "Skilled healthcare provider focused on patient care, diagnosis, and treatment.",
        "expertise": "Cardiology & Hypertension Management",
        "workExperience": "Experienced provider with a strong background in diagnosis, treatment, and patient care.",
        # edit
        "edit_fname": data.fake.first_name_male(),
        "edit_lname": data.fake.last_name(),
        "edit_role": "Provider",
        "edit_dob": "11-18-1989",
        "edit_gender": "Male",
        "edit_npi_number": data.generate_random_digits(10),
        "edit_contact_num": f"({data.generate_random_digits(3)}) {data.generate_random_digits(3)}-{data.generate_random_digits(4)}",
        "edit_fax_num": data.generate_random_digits(5),
        "edit_yearOfExperience": "12",
        "edit_taxonomy_num": data.generate_random_digits(6),
        "edit_email": None,
        "edit_state": "Delaware (DE)",
        "edit_license_num": data.generate_random_digits(10),
        "edit_bio": "Compassionate provider committed to quality patient care and effective treatment.",
        "edit_expertise": "Endocrinology & Diabetes Care",
        "edit_workExperience": "Experienced healthcare provider skilled in patient care, diagnosis, and treatment of acute and chronic conditions."
    }
    provider_data["email"] = f"{provider_data['fname']}+{data.generate_random_digits(5)}@mailinator.com"
    provider_data["edit_email"] = f"{provider_data['edit_fname']}+{data.generate_random_digits(5)}@mailinator.com"
    provider_user(page, provider_data)