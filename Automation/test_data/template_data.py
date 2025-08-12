import random
from Automation.utils import data

templates = ["Review Of System (ROS)", "Physical Exam (PE)"]
specialities = ["Chiropractic", "Dermatology", "Gastroenterology", "Gynecology", "Oncology", "Urology"]
speciality_for_creation = random.choice(specialities)
remaining_specialities = [s for s in specialities if s != speciality_for_creation]
speciality_for_update = random.choice(remaining_specialities)

template_name1 = "Test_Template_"+ data.generate_random_string(4)
template_name2 = "Demo_Template_"+ data.generate_random_string(4)

ros_template_data = {
    "General Appearance": "Alert, oriented, no acute distress.",
    "HEENT": "Head atraumatic, normocephalic. Vision and hearing intact. No nasal congestion or sore throat.",
    "Neck": "No stiffness or pain. No lymphadenopathy.",
    "Chest And Lungs": "Clear to auscultation bilaterally. No shortness of breath.",
    "Mouth/Speech": "Speech fluent and clear. No dysarthria or slurred speech.",
    "Abdomen": "Soft, non-tender, no distension. Bowel sounds present.",
    "Genitourinary": "No dysuria, urgency, or incontinence.",
    "Rectal": "Normal tone. No hemorrhoids or bleeding reported.",
    "Lympathic": "No lymph node swelling noted.",
    "Back/Spine": "No spinal tenderness or deformity. Full range of motion.",
    "Joints/Endocrine": "No joint pain or swelling. No signs of thyroid enlargement.",
    "Genito-urinary": "As above. Normal urinary and reproductive function.",
    "Skin": "No rash or lesions. Skin warm and dry.",
    "Neurological System": "Cranial nerves II-XII intact. Normal strength, sensation, and reflexes.",
    "Galt":	"Normal gait; no imbalance or limping.",
    "Mood And Affect": "Mood appropriate; affect congruent with mood.",
    "Behavior":	"Cooperative; behavior appropriate to situation."
}
pe_template_data = {
    "General": "Patient appears well-nourished, alert, and oriented.",
    "Diet": "Low-sodium, diabetic-friendly diet advised.",
    "Exercise": "Engages in regular physical activity; walks 30 mins daily.",
    "Eyes": "PERRLA; no redness or discharge noted.",
    "Hent": "Head normocephalic, atraumatic; ENT clear without congestion.",
    "Resp": "Clear to auscultation bilaterally; no wheezes, rales, or rhonchi.",
    "Cvs": "Regular rate and rhythm; no murmurs or gallops detected.",
    "Breat": "Breasts symmetrical; no masses or tenderness.",
    "Gi": "Abdomen soft, non-tender, no hepatosplenomegaly.",
    "Gu": "Genitalia normal; no lesions or discharge.",
    "Gyne": "External genitalia normal; pap smear up to date.",
    "Mss": "Full range of motion; no joint swelling or tenderness.",
    "Ns": "Alert and oriented x3; cranial nerves II-XII intact.",
    "Skin": "No rashes, lesions, or ulcers; skin warm and dry.",
    "Hemo": "No signs of anemia, bruising, or bleeding disorders.",
    "Endoc": "Thyroid not enlarged; no goiter or nodules; blood sugar stable.",
    "Psych": "Normal affect; coherent thoughts; no signs of depression or anxiety."
}
