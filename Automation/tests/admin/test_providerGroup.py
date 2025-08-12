import random
from playwright.sync_api import Playwright
from Automation.pages.admin.providerGroup_page import providerGroup
from Automation.utils import creds, data, constants, local_data
from Automation.utils.browser import login, open_browser


def test_providerGroup(playwright: Playwright):
    
    page = open_browser(playwright)
    credential = {
        "url": creds.admin_url,
        "email": creds.admin_email,
        "password": creds.admin_password
    }
    login(page, credential)
    
    
    providerGroup_data = {
        # add - provider group
        "pg_name": f"{random.choice(constants.providerGroup_name)} {data.generate_random_string(4)}",
        "pg_subdomain": None,
        "pg_groupNpiNumber": data.generate_random_digits(10),
        "pg_contactNumber": f"({data.generate_random_digits(3)}) {data.generate_random_digits(3)}-{data.generate_random_digits(4)}",
        "pg_email": "abcdef+"+data.generate_random_digits(7)+"@mailinator.com",
        "pg_faxId": data.generate_random_digits(6),
        "pg_website": "https://www.godaddy.com/en-in",
        # edit provider group
        "pg_name2": f"{random.choice(constants.providerGroup_name)} {data.generate_random_string(4)}",
        "pg_subdomain2": None,
        "pg_groupNpiNumber2": data.generate_random_digits(10),
        "pg_contactNumber2": f"({data.generate_random_digits(3)}) {data.generate_random_digits(3)}-{data.generate_random_digits(4)}",
        "pg_email2": "abcdef+"+data.generate_random_digits(7)+"@mailinator.com",
        "pg_faxId2": data.generate_random_digits(6),
        "pg_website2": "https://www.godaddy.com/en-in",
        # "pg_website2": data.generate_random_website(),
        
        # add - location
        "loc_name": local_data.pg_location,
        "loc_Id": f"{data.generate_random_string(2)}{data.generate_random_digits(3)}",
        "loc_contact_num": f"({data.generate_random_digits(3)}) {data.generate_random_digits(3)}-{data.generate_random_digits(4)}",
        "loc_email": f"qwerty+{data.generate_random_digits(5)}@mailinator.com",
        "loc_fax": f"{data.generate_random_string(1)}{data.generate_random_digits(4)}",
        # edit - location
        "loc_name2": local_data.pg_location1,
        "loc_Id2": f"{data.generate_random_string(2)}{data.generate_random_digits(3)}",
        "loc_contact_num2": f"({data.generate_random_digits(3)}) {data.generate_random_digits(3)}-{data.generate_random_digits(4)}",
        "loc_email2": f"asdfg+{data.generate_random_digits(5)}@mailinator.com",
        "loc_fax2": f"{data.generate_random_string(1)}{data.generate_random_digits(4)}",
        # Adding Another Location
        "loc_name3": local_data.pg_location,
        "loc_Id3": f"{data.generate_random_string(2)}{data.generate_random_digits(3)}",
        "loc_contact_num3": f"({data.generate_random_digits(3)}) {data.generate_random_digits(3)}-{data.generate_random_digits(4)}",
        "loc_email3": f"zxcvb+{data.generate_random_digits(5)}@mailinator.com",
        "loc_fax3": f"{data.generate_random_string(1)}{data.generate_random_digits(4)}",
        
        # Add Staff
        "staff_fname": data.fake.first_name_female(),
        "staff_lname": data.fake.last_name(),
        "staff_email": f"staff+{data.generate_random_digits(5)}@mailinator.com",
        "staff_number": f"({data.generate_random_digits(3)}) {data.generate_random_digits(3)}-{data.generate_random_digits(4)}",
        # Edit Staff
        "staff_fname2": data.fake.first_name_male(), 
        "staff_lname2": data.fake.last_name(), 
        "staff_email2": f"staff1+{data.generate_random_digits(5)}@mailinator.com",
        "staff_number2": f"({data.generate_random_digits(3)}) {data.generate_random_digits(3)}-{data.generate_random_digits(4)}",
        # Adding Another Staff
        "staff_fname3": data.fake.first_name_male(),
        "staff_lname3": data.fake.last_name(),
        "staff_email3": f"staff2+{data.generate_random_digits(5)}@mailinator.com",
        "staff_number3": f"({data.generate_random_digits(3)}) {data.generate_random_digits(3)}-{data.generate_random_digits(4)}",
        
        # Add Department
        "dept_name": random.choice(constants.department_name_list),
        "dept_Id": f"{data.generate_random_string(2)}{data.generate_random_digits(3)}",
        "dept_contact_num": f"({data.generate_random_digits(3)}) {data.generate_random_digits(3)}-{data.generate_random_digits(4)}",
        # Edit Department
        "dept_name2": random.choice(constants.department_name_list),
        "dept_Id2": f"{data.generate_random_string(2)}{data.generate_random_digits(3)}",
        "dept_contact_num2": f"({data.generate_random_digits(3)}) {data.generate_random_digits(3)}-{data.generate_random_digits(4)}",
        
        # Add Provider
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
        # Edit Provider
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
    providerGroup_data["pg_subdomain"] = providerGroup_data["pg_name"]
    providerGroup_data["pg_subdomain2"] = providerGroup_data["pg_name2"]
    providerGroup_data["email"] = f"{providerGroup_data['fname']}{data.generate_random_digits(5)}@mailinator.com"
    providerGroup_data["edit_email"] = f"{providerGroup_data['edit_fname']}{data.generate_random_digits(5)}@mailinator.com"
    providerGroup(page, providerGroup_data)
    
    
    
    
    
    
    
    # condition_name = ["Dental problems", "PolyNeuropathy", "Back Pain", "Other psychotic disorders", "Schizophrenia", "Hip/Pelvic Fracture", "Glucoma", "Cataract", "Prostate cancer", "Lung cancer", "Sickle Cell Anemia", "Chronic Hepatitis C", "Headaches / Migraines", "Cerebral Infarction (CVA / Stroke)", "Degenerative Disc Disease", "Human Immunodeficiency Virus (HIV)", "Hypertension (High Blood Pressure)", "Emphysema / lung disease", "Dorsalgia", "Basal Cell Carcinoma", "Pelvic Pain Syndrome", "Bipolar disorder", "Interstitial lung disease", "Chronic Bronchitis", "Endometriosis", "Parkinson's disease", "Coronary Artery Disease", "Asthma", "Chronic kidney disease", "Osteoarthritis", "Thyroid disorders", "leukemia", "Crohn's Disease", "Alzheimer's Disease", "Osteoporosis", "Heart Disease", "Diabetes"]
    # selected_condition = random.choice(condition_name)

    # department_name_list = ["Cardiology", "Neurology", "Orthopedics", "Pediatrics", "Oncology", "Emergency", "Radiology", "Gynecology", "Dermatology", "Gastroenterology", "Endocrinology", "Pulmonology", "Nephrology", "Hematology", "Urology", "Psychiatry", "Rehabilitation", "Anesthesiology", "Ophthalmology", "Pathology"]
