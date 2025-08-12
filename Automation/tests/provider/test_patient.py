from Automation.pages.patient.order_page import order, prescription_order
from Automation.pages.patient.allergy_page import allergy
from Automation.pages.patient.careplan_page import careplan
from Automation.pages.patient.diagnosis_page import diagnosis
from Automation.pages.patient.document_page import document
from Automation.pages.patient.history_page import history
from Automation.pages.patient.medication_page import medication
from Automation.pages.patient.patient_page import create_patient
from Automation.pages.patient.vaccine_page import vaccine
from Automation.pages.patient.vitals_page import vitals
from Automation.test_data import patient_data
from Automation.utils.browser import open_browser, login
from playwright.sync_api import Playwright
from Automation.utils import creds, local_data

diagnosis_data = {
    # add
    "code1": "A010",
    "problem1": "Typhoid fever",
    "status1": "Inactive",
    "type1": "Acute",
    "note1": "This code is used for the diagnosis of typhoid fever, a bacterial infection caused by Salmonella typhi.",
    # edit
    "code2": "E119",
    "problem2": "Type 2 diabetes mellitus without complications",
    "status2": "Active",
    "type2": "Chronic",
    "note2": "Type 2 diabetes without complications is managed with diet, exercise, and medication to maintain blood sugar levels."
}

allergy_data = {
    # add
    "allergy_name": "Dust mites",
    "allergy_severity": "Mild",
    "allergy_reaction": "Sneezing and watery eyes",
    "allergy_note": "Regular cleaning and use of air purifiers help manage symptoms.",
    # edit
    "edit_allergy_name": "Latex",
    "edit_allergy_severity": "Moderate",
    "edit_allergy_reaction": "Skin irritation and redness",
    "edit_allergy_note": "Avoid use of latex gloves or materials."    
}

history_data = {
    "condition1": "Hypertension",
    "condition1_date": ["03-15-2018", "03/15/2018"],
    "condition1_note": "Controlled with medication and lifestyle changes.",
    "condition2": "Asthma",
    "condition2_note": "Mild, uses inhaler as needed.",
    "surgery1_name": "Cataract Surgery",
    "surgery1_date": ["02-20-2021", "02/20/2021"],
    "surgery1_note": "Performed on the right eye, vision fully restored.",
    "surgery2_name": "Gallbladder Removal",
    "surgery2_note": "Laparoscopic surgery, recovery without issues.",
    "problem1_name": ["A01000 - Typhoid", "A01000"],
    "problem1_note": None,
    "problem2_name": ["I110 - Hypertensive heart disease with heart failure", "I110"],
    "problem2_note": None,
    "habits": "Doing Yoga & Exercise"
}
history_data["problem1_note"] = f"Patient has a family history of {history_data['problem1_name'][0]}. Condition previously diagnosed in a first-degree relative."
history_data["problem2_note"] = f"Family history of {history_data['problem2_name'][0]}. Noted in immediate relatives with onset in mid-adulthood. Monitoring advised due to hereditary risk."

medication_data = {
    # add
    "medicine1": "COSENTYX",
    "medication1_start_date": ["07-28-2024", "07/28/2024"],
    "medication_note1": None,
    # edit
    "medicine2": "ELREXFIO - ELRANATAMAB",
    "medication_note2": None
}
medication_data["medication_note1"] = f"{medication_data['medicine1']} (300 tablets) prescribed by Dr. {local_data.provider1} for daily oral use before meals."
medication_data["medication_note2"] = f"Prescribed 300 drops, to be taken twice daily at bedtime via the optic route by Dr. {local_data.provider2}."
    
    
def test_patientflow(playwright: Playwright):
    
    page = open_browser(playwright)
    credential = {
        "url": creds.provider_url,
        "email": creds.provider_email,
        "password": creds.provider_password
    }
    

    # diagnosis_data = {
    #     # add
    #     "code1": "A01.0",
    #     "problem1": "Typhoid fever",
    #     "status1": "Inactive",
    #     "type1": "Acute",
    #     "note1": "This code is used for the diagnosis of typhoid fever, a bacterial infection caused by Salmonella typhi.",
    #     # edit
    #     "code2": "E11.9",
    #     "problem2": "Type 2 diabetes mellitus without complications",
    #     "status2": "Active",
    #     "type2": "Chronic",
    #     "note2": "Type 2 diabetes without complications is managed with diet, exercise, and medication to maintain blood sugar levels."
    # }
    
    
    # allergy_data = {
    #     # add
    #     "allergy_name": "Dust mites",
    #     "allergy_severity": "Mild",
    #     "allergy_reaction": "Sneezing and watery eyes",
    #     "allergy_note": "Regular cleaning and use of air purifiers help manage symptoms.",
    #     # edit
    #     "edit_allergy_name": "Latex",
    #     "edit_allergy_severity": "Moderate",
    #     "edit_allergy_reaction": "Skin irritation and redness",
    #     "edit_allergy_note": "Avoid use of latex gloves or materials."    
    # }


    # medication_data = {
    #     # add
    #     "medicine1": "Guanidine Hydrochloride",
    #     "medication_note1": None,
    #     # edit
    #     "medicine2": "Heparin Sodium",
    #     "medication_note2": None
    # }
    # medication_data["medication_note1"] = f"{medication_data['medicine1']} (300 tablets) prescribed by Dr. {local_data.provider1} for daily oral use before meals."
    # medication_data["medication_note2"] = f"Prescribed 300 drops, to be taken twice daily at bedtime via the optic route by Dr. {local_data.provider2}."
    
    
    vaccine_data = {
        "vaccine1": "Covaxin",
        "vaccine2": "EpiVacCorona"
    }
    
    
    select_vitals = ["Blood Pressure","Blood Glucose","Body Temperature","Heart Rate","Respiration Rate"]
    
    
    # history_data = {
    #     "condition1": "Hypertension",
    #     "condition1_note": "Controlled with medication and lifestyle changes.",
    #     "condition2": "Asthma",
    #     "condition2_note": "Mild, uses inhaler as needed.",
    #     "surgery1_name": "Cataract Surgery",
    #     "surgery1_note": "Performed on the right eye, vision fully restored.",
    #     "surgery2_name": "Gallbladder Removal",
    #     "surgery2_note": "Laparoscopic surgery, recovery without issues.",
    #     "problem1_name": "Difficulty breathing",
    #     "problem1_note": None,
    #     "problem2_name": "Headache",
    #     "problem2_note": None
    # }
    # history_data["problem1_note"] = f"A history of {history_data['problem1_name']}, possibly linked to a chronic respiratory condition."
    # history_data["problem2_note"] = f"Experiences {history_data['problem2_name']}, potentially related to stress, migraines, or other underlying conditions. Regular check-ups are advised."
    
    
    careplan_data = {
        # add
        "cp_title1": "Diabetes Management Plan",
        "cp_condition1": "Diabetes Type 2",
        "cp_description1": "Focuses on blood sugar monitoring, medication adherence, regular exercise, and a controlled diet to manage glucose levels effectively.",
        # edit
        "cp_title2": "Hypertension Care Plan",
        "cp_condition2": "Hypertension",
        "cp_description2": "Aims to control blood pressure through prescribed medication, low-sodium diet, regular exercise, and stress reduction techniques."
    }
    
    
    document_data = {
        "document_type1": "Lab Reports",
        "document_description1": "Lab report detailing experiment procedures, results, and conclusions.",
        "document_type2": "Surgery Reports",
        "document_description2": "Surgery report detailing procedure, findings, and post-op care."
    }
    

    login(page, credential)
    create_patient(page, patient_data.patient_data)
    diagnosis(page, diagnosis_data)
    allergy(page, allergy_data)
    medication(page, medication_data)
    vaccine(page, vaccine_data)
    vitals(page, select_vitals)
    history(page, history_data)
    careplan(page, careplan_data)
    document(page, document_data)
    # order(page)
    # prescription_order(page)