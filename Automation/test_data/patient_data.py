from Automation.utils import constants, creds, data, local_data
def generate_patient_data():
    PATIENT_FNAME = data.fake.first_name_male()
    PATIENT_LNAME = data.fake.last_name()
    PATIENT_MOB_NUM = f"({data.generate_random_digits(3)}) {data.generate_random_digits(3)}-{data.generate_random_digits(4)}"
    PATIENT_EMAIL = (f"{PATIENT_FNAME}{data.generate_random_digits(5)}@mailinator.com").lower()
    email = (f"{PATIENT_FNAME}{data.generate_random_digits(5)}@mailinator.com").lower()
    return PATIENT_FNAME, PATIENT_LNAME, PATIENT_MOB_NUM,PATIENT_EMAIL, email
PATIENT_FNAME, PATIENT_LNAME, PATIENT_MOB_NUM,PATIENT_EMAIL, email = generate_patient_data()

patient_data = {
        # patient details
        "patient_fname": PATIENT_FNAME,
        "patient_lname": PATIENT_LNAME,
        "patient_dob": ["05-22-1985", "05/22/1985"],
        "patient_gender": "Male",
        "patient_marital_status": "Single",
        "patient_timezone": "Indian Standard Time (UTC +5:30)",
        "patient_language": "English",
        "patient_ssn": f"{data.generate_random_digits(3)}-{data.generate_random_digits(2)}-{data.generate_random_digits(4)}",
        "patient_mrn": data.generate_random_digits(5),
        "patient_race": "American Indian", 
        "patient_ethnicity":"Cuban",
        "patient_mob_num": PATIENT_MOB_NUM,
        "patient_home_num": f"({data.generate_random_digits(3)}) {data.generate_random_digits(3)}-{data.generate_random_digits(4)}",
        "patient_email": PATIENT_EMAIL,
        "patient_fax_num": data.generate_random_digits(5),
        # emergency contact
        "relationship_with_patient": "Child",
        "child_fname": data.fake.first_name_male(),
        "child_lname": data.fake.last_name(),
        "emergency_contact": f"({data.generate_random_digits(3)}) {data.generate_random_digits(3)}-{data.generate_random_digits(4)}",
        "emergency_email": None,
        # insurance details
        "insurance_plan_name": "BlueCare Advantage",
        "insurance_plan_type": "PPO",
        "insurance_order_of_benefits": "Primary",
        "insurance_id": f"INS{data.generate_random_digits(10)}",
        "insurance_group_id": f"GRP{data.generate_random_digits(5)}",
        "insurance_start_dt": data.insurance_dt("-", "month"),
        "insurance_end_dt": data.insurance_dt("-", "year"),
        "insurance_copay_amount": "200"
    }
patient_data["emergency_email"] = f"{patient_data['child_fname']}{data.generate_random_digits(1)}@mailinator.com".lower()

# Demographics > BASIC INFORMATION
basic_information = [
    ("Contact Number", patient_data['patient_mob_num'], "Patient Contact Num is incorrect or not visible."),
    ("Email", patient_data['patient_email'], "Patient Email is incorrect or not visible."),
    ("SSN", patient_data['patient_ssn'], "SSN is incorrect or not visible."),
    ("Marital Status", patient_data['patient_marital_status'].upper(), "Marital Status is incorrect or not visible."),
    ("Languages", patient_data['patient_language'], "Language is incorrect or not visible."),
    ("Race", patient_data['patient_race'], "Race is incorrect or not visible."),
    ("Ethnicity", patient_data['patient_ethnicity'], "Ethnicity is incorrect or not visible."),
    ("Gender", patient_data['patient_gender'], "Gender is incorrect or not visible."),
]

registering_information = [
    ("//div[contains(@class,'MuiGrid-container css-wl9yxs')]", "Primary Provider", local_data.provider1, "Primary Provider is not visible."),
    ("//div[contains(@class,'MuiGrid-container css-wl9yxs')]", "Registered Date", data.formatted_date, "Registered Date is incorrect or not visible")
]

insurance_info = [
    ("Payer Name", constants.insurance[0], "Insurance name is incorrect or not visible"),
    # ("Plan Type", patient_data['insurance_plan_type'].upper(), "Plan Type is incorrect or not visible"),
    ("Coverage Type", "Medical", "Coverage Type is incorrect or not visible"),
    ("Order Of Benefits", patient_data['insurance_order_of_benefits'], "Order Of Benefits is incorrect or not visible"),
    ("Insurance Id", patient_data["insurance_id"], "Insurance Id is incorrect or not visible."),
    ("Group Id", patient_data["insurance_group_id"], "Group Id is incorrect or not visible."),
    ("Start Date", data.insurance_dt("/", "month"), "Insurance Start Date is incorrect or not visible."),
    ("End Date", data.insurance_dt("/", "year"), "Insurance End Date is incorrect or not visible."),
    ("Provider", local_data.provider1, "Provider is incorrect or not visible.")
]
