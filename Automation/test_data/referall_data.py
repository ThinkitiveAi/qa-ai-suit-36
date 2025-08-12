import random
from Automation.test_data import patient_data
from Automation.utils import data
PATIENT_FNAME, PATIENT_LNAME, PATIENT_MOB_NUM, PATIENT_EMAIL, email = patient_data.generate_patient_data()

priority = ["High", "Low", "Medium"]


add_referall_data = {
    "patient_name": f"{patient_data.PATIENT_FNAME} {patient_data.PATIENT_LNAME}",
    "priority" : random.choice(priority),
    "referall_reason" : "Test Referall Reason",
    "referall_note" : "Test Referall Note",
    "diagnosis_code" : ["E119", "E119 - Type 2 diabetes mellitus without complications"],
    }

referral_in_add_patient_data = {
    "patient_fname": f"{PATIENT_FNAME}",
    "patient_lname": f"{PATIENT_LNAME}",
    "patient_dob": ["05-22-1985", "05/22/1985"],
    "patient_gender": "Male",
    "patient_email": f"{PATIENT_EMAIL}",
    "patient_mob": f"{PATIENT_MOB_NUM}",
}