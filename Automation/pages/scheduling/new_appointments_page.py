from playwright.sync_api import Page, expect
from Automation.tests.provider.test_patient import diagnosis_data, allergy_data, history_data, medication_data
from Automation.test_data.patient_data import PATIENT_MOB_NUM, PATIENT_EMAIL
from Automation.test_data.scheduling_data import appointment_details, insurance_details, verify_appointment_and_patient_details, appointmnt_status
from Automation.utils import data, local_data
from Automation.utils import constants
patientId = None
def new_appointment(page: Page, appointment: dict) -> None:
    
    page.get_by_role("tab", name="Scheduling").click()
    page.get_by_text("Appointments").click()
    page.wait_for_timeout(500)
    # Schedule Appointment
    page.get_by_role("button", name="Schedule Appointment").click()
    page.get_by_role("menuitem", name=constants.appointment[0]).click()
    page.get_by_role("heading", name="Schedule Appointment").get_by_text("Schedule Appointment").click(click_count=3)
    
    page.get_by_placeholder("Search Patient").click()
    page.get_by_role("option", name=appointment.get("patient_name")).click()
    print(f"New Appointment (Selected Patient): {appointment.get('patient_name')}")
    
    page.get_by_placeholder("Select Type").click()      # Appointment Type
    page.get_by_role("option", name=constants.appointment_type[0]).click()
    
    page.get_by_placeholder("Reason").fill(appointment.get("cheif_complaint"))
    
    page.locator("//input[@name='timezone']").click()
    page.get_by_role("option", name="Indian Standard Time (GMT +05:30)").click()
    
    page.get_by_role("button", name=constants.visit_type[1]).click()      # visit type 
    
    # page.get_by_text("Location", exact=True).click()
    # page.get_by_role("combobox", name="Select", exact=True).click()
    # page.get_by_role("option", name=local_data.pg_location).click()
    
    # page.get_by_placeholder("Search Provider").fill(local_data.provider1)
    # page.get_by_role("option", name=local_data.provider1).click()
    
    page.get_by_role("button", name="View availability").click()
    page.get_by_role("gridcell", name=data.day, exact=True).click()
    print("schedule_slot: ", data.slot_time)
    page.get_by_role("button", name=data.slot_time).click()

    page.get_by_role("button", name="Insurance").click()
    page.wait_for_timeout(200)
    expect(page.get_by_label("Primary Insurance")).to_have_value(constants.insurance[0])
    
    page.get_by_placeholder("Appointment Note").fill(appointment.get("new_appointment_note"))

    page.get_by_role("button", name="Save And Close").click()
    page.get_by_text("Appointment booked successfully").click(click_count=3)
    page.wait_for_timeout(1000)
    
    page.get_by_text("Search By Patient").click()
    page.get_by_placeholder("Search & Select").first.click()
    page.get_by_role("option", name=appointment.get("patient_name")).click()
    
    # page.get_by_text("Search By Provider").click()
    # page.get_by_placeholder("Search & Select").nth(1).click()   
    # page.get_by_role("option", name=local_data.provider1).click()
    
    page.get_by_role("button", name="Appointment Type").click()
    page.get_by_label(constants.appointment_type[0]).check()
    page.wait_for_timeout(2000)
    
    namewithid = page.locator("//p[@class='MuiTypography-root MuiTypography-body1 css-1fi2nf3']").inner_text()
    patientId = namewithid.split('(')[1].split(')')[0]
    
    page.get_by_role("cell", name=f"{data.scheduleTime} | 15 Mins").get_by_text(data.scheduleTime).click()
    page.get_by_role("cell", name=constants.visit_type[1]).click()
    assert page.get_by_text(f"{appointment.get('patient_name')} ({patientId})").is_visible(), "Patient Name & ID is Not Visible"
    page.get_by_role("cell", name=constants.appointment_type[0]).click()
    page.get_by_role("cell", name=f"{local_data.provider1} Multispecialty").get_by_text(local_data.provider1).click()
    page.get_by_role("cell", name=appointment.get("cheif_complaint")).click()
    page.get_by_role("cell", name=appointmnt_status[0]).get_by_text(appointmnt_status[0]).click()
    
    # Scheduled
    verify_appointment_and_patient_details(page, appointmnt_status[0], data.scheduleTime, patientId)
    appointment_details(page, appointmnt_status[0])
    insurance_details(page)
    print("Appointment booked successfully & verified")
    
    # Reschedule Appointment
    page.get_by_role("button", name="Reschedule Appointment").click()
    page.get_by_role("heading", name="Reschedule Appointment").get_by_text("Reschedule Appointment").click()
    
    if (page.locator(f"//p[text()='Patient Name']/following::p[text()='{appointment.get('patient_name')}']").is_visible() and
        page.locator(f"//p[text()='Provider Name']/following::p[text()='{local_data.provider1}']").is_visible() and 
        page.get_by_title("Reschedule Appointment").locator(f"//p[text()='Appointment Status']/following::p[text()='{appointmnt_status[0]}']").is_visible() and     
        page.get_by_title("Reschedule Appointment").locator(f"//p[text()='Appointment Type']/following::p[text()='{constants.appointment_type[0]}']").is_visible() and
        page.get_by_title("Reschedule Appointment").locator(f"//p[text()='Visit Type']/following::p[text()='{constants.visit_type[1]}']").is_visible()
        ):
        page.get_by_role("gridcell", name=data.day, exact=True).click()
        print("reschedule_slot: ", data.reschedule_slot)
        page.get_by_role("button", name=data.reschedule_slot).click()
        page.get_by_role("button", name="Save And Close").click()
        
    page.get_by_role("button", name="Confirm Appointment").click()
    page.get_by_text("Appointment updated successfully.").click()
    page.get_by_role("cell", name=appointmnt_status[1]).get_by_text(appointmnt_status[1]).click()

    # Confirmed
    verify_appointment_and_patient_details(page, appointmnt_status[1], data.rescheduleTime, patientId)
    appointment_details(page, appointmnt_status[1])
    insurance_details(page)
    print("Appointment Updated successfully & verified")
    
    page.get_by_role("button", name="Start Check In").click()
    page.get_by_text("Check In", exact=True).click()
    page.get_by_title("Check In").get_by_text(constants.visit_type[1]).click()
    page.get_by_title("Check In").get_by_text("Appointment Type").click()
    page.get_by_title("Check In").get_by_text(constants.appointment_type[0]).click()
    page.get_by_text("Primary Provider Name").click()
    page.get_by_title("Check In").get_by_text(local_data.provider1).click()
    page.get_by_title("Check In").get_by_text("Chief Complaint").click()
    page.get_by_title("Check In").get_by_text(appointment.get("cheif_complaint")).click()
    
    # page.get_by_role("button", name="Collect Payment").click()
    # page.get_by_role("tab", name="Card Payment").click()
    # page.query_selector("input[name='amount']").fill("1")
    # page.locator("//div[@class='MuiBox-root css-1sykfg7']").click()
    # page.get_by_role("button", name="Pay").click()
    # page.get_by_text("Payment Successfully Added").click()
    
    page.get_by_role("button", name="Complete Check In").click()
    page.wait_for_timeout(1000)
    page.locator("//div[@aria-label='unmute']").click()
    page.wait_for_timeout(1000)
    page.locator("//div[@aria-label='mute']").click()
    page.wait_for_timeout(1000)
    page.locator("//div[@aria-label='unmute']").click()
    
    page.get_by_role("button", name="start camera").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="stop camera").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="start camera").click()
    
    page.get_by_text("Ready to join?").click()
    page.get_by_role("button", name="Start Appointment").click()
    
    page.get_by_text(f"{appointment.get('patient_name')} Appointment With Provider {local_data.provider1}").click()
    
    page.locator("//div[@aria-label='unmute']").click()
    page.wait_for_timeout(1000)
    page.locator("//div[@aria-label='mute']").click()
    page.wait_for_timeout(1000)
    page.locator("//div[@aria-label='unmute']").click()
    
    page.get_by_role("button", name="start camera").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="stop camera").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="start camera").click()
    
    page.get_by_test_id("RemoveOutlinedIcon").click()
    page.locator("//div[@aria-label='mute']").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="stop camera").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="start camera").click() 
    
    # =================================================================================================================
    
    page.locator("//p[text()='Simple Soap Note']").click()
    page.get_by_role("menuitem", name="Psychiatric Note").click()
    
    page.get_by_text(f"{data.day} {data.month} {data.year}").click()
    page.get_by_text(data.rescheduleTime).click()
    page.locator(f"//p[text()='Provider']/following::p[text()='{local_data.provider1}']").click()
    page.get_by_text(f"{constants.visit_type[1]} Visit").click()
    
    page.locator("//input[@name='problems']").fill(diagnosis_data.get("problem1"))
    page.get_by_role("button", name="Add Allergy").click()
    page.get_by_placeholder("Enter Allergy Name").fill(allergy_data.get("allergy_name"))
    page.get_by_placeholder("Select Severity").click()
    page.get_by_role("option", name=allergy_data.get("allergy_severity")).click()
    page.get_by_placeholder("Enter Reaction").fill(allergy_data.get("allergy_reaction"))
    page.get_by_placeholder("Choose Date").click()
    page.get_by_placeholder("Choose Date").fill("03-22-2020")
    page.get_by_placeholder("Select", exact=True).click()
    page.get_by_role("option", name="Inactive").click()
    page.get_by_placeholder("Type here").fill(allergy_data.get("allergy_note"))
    page.get_by_role("button", name="Save").click()    
    page.get_by_text("Allergy created successfully").click()
    page.wait_for_timeout(1000)
    
    page.get_by_role("button", name="Add PMH").click()
    page.get_by_placeholder("Enter Condition Name").fill(history_data["condition1"])
    page.get_by_placeholder("Choose date").click()
    page.get_by_placeholder("Choose date").fill(history_data["condition1_date"][0])
    page.get_by_placeholder("Type here").fill(history_data["condition1_note"])
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Past Medical history created successfully").click()
    page.wait_for_timeout(1000)
    
    page.get_by_role("button", name="Add PSH").click()
    page.get_by_placeholder("Enter Surgery Name").fill(history_data["surgery1_name"])
    page.get_by_placeholder("Choose date").click()
    page.get_by_placeholder("Choose date").fill(history_data['surgery1_date'][0])
    page.get_by_placeholder("Type here").fill(history_data["surgery1_note"])
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Past Surgical history created successfully").click()
    page.wait_for_timeout(1000)
    
    page.get_by_role("button", name="Add FH").click()
    page.get_by_placeholder("Select or Search Problem").fill(history_data["problem1_name"][1])
    page.get_by_role("option", name=history_data["problem1_name"][0]).click()
    page.locator("input[name=\"relative\"]").click()
    page.get_by_role("option", name="Grandparent", exact=True).click()
    page.get_by_placeholder("Enter Age").fill("65")
    page.get_by_placeholder("Type here").fill(history_data["problem1_note"])
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Family history created successfully").click()
    
    page.locator("//input[@name='habits']").fill(history_data['habits'])
    
    page.get_by_role("button", name="Add Med").click()
    page.get_by_placeholder("Select Or Search Medicine").fill(medication_data["medicine1"]) 
    Medicine_name_1 = page.get_by_role("option").first.inner_text()
    page.get_by_role("option").first.click()
    page.get_by_placeholder("Enter Quantity").fill("100")
    page.get_by_placeholder("Dosage Unit").click()
    page.get_by_role("option", name="Tablet (s)", exact=True).click()
    page.get_by_placeholder("frequency").click()
    page.get_by_role("option", name="Every Day").click()
    page.get_by_placeholder("When").click()
    page.get_by_role("option", name="Before Meal").click()
    page.get_by_placeholder("Time").click()
    page.get_by_role("option", name="Oral").click()
    page.locator("//input[@name='medicationStartDate']").click()
    page.locator("//input[@name='medicationStartDate']").fill(medication_data['medication1_start_date'][0])
    page.locator("(//input[@placeholder='Choose Date'])[2]").click()
    page.locator("(//input[@placeholder='Choose Date'])[2]").fill("11-20-2024")
    page.get_by_placeholder("Select Provider").click()
    page.get_by_placeholder("Select Provider").fill(local_data.provider1)
    page.get_by_role("option", name=local_data.provider1).click()
    page.get_by_placeholder("Type here").click()
    page.get_by_placeholder("Type here").fill(medication_data["medication_note1"])
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Medication created successfully").click()
    
    page.get_by_role("button", name="ROS Template").click()
    page.locator("//p[text()='ROS Templates']").click()
    page.get_by_placeholder("Speciality").click()
    page.get_by_role("option", name=constants.speciality[2]).click()
    page.get_by_placeholder("Select Template").click()
    page.get_by_role("option", name=local_data.ros_template).click()
    page.get_by_role("button", name="Export to Note").click()    
    page.get_by_text("Template updated successfully").click()
    page.wait_for_timeout(200)
    page.get_by_role("button", name="Close").click()

    page.get_by_placeholder("Sys", exact=True).fill("125")
    page.get_by_placeholder("Dia", exact=True).fill("90")
    
    page.get_by_placeholder("%").fill("92")
    page.get_by_placeholder("cm", exact=True).fill("177")
    page.get_by_placeholder("kg/m^2").fill("24")
    page.get_by_placeholder("BPM", exact=True).fill("60")
    page.get_by_placeholder("lbs", exact=True).fill("143")
    page.get_by_placeholder("f", exact=True).fill("96")
    
    page.get_by_role("button", name="PE Template").click()
    page.locator("//p[text()='PE Templates']").click()
    page.get_by_placeholder("Speciality").click()
    page.get_by_role("option", name=constants.speciality[0]).click()
    page.get_by_placeholder("Select Template").click()
    page.get_by_role("option", name=local_data.pe_template).click()
    page.get_by_role("button", name="Export to Note").click()    
    page.get_by_text("Template updated successfully").click()
    page.wait_for_timeout(200)
    page.get_by_role("button", name="Close").click()

    page.get_by_role("button", name="Psych Template").click()
    page.get_by_role("menuitem", name="PHQ-9").click()
    page.get_by_text("Phq9 Assessment").click(click_count=3)
    Phq9_btn = ["2", "7", "10", "16", "17", "22", "25", "30", "33"]
    for btn in Phq9_btn:
        page.locator(f"(//input[@type='radio'])[{btn}]").click()
    page.get_by_role("button", name="Save").click()    
    
    page.get_by_role("button", name="Psych Template").click()
    page.get_by_role("menuitem", name="GAD-7").click()
    page.get_by_text("Gad7 Assessment").click(click_count=3)
    Gad7_btn = ["2", "7", "12", "14", "17", "23", "25"]
    for btn in Gad7_btn:
        page.locator(f"(//input[@type='radio'])[{btn}]").click()
    page.get_by_role("button", name="Save").click()    
    
    page.get_by_role("button", name="Psych Template").click()
    page.get_by_role("menuitem", name="MDQ").click()
    page.get_by_text("Mdq Assessment").click(click_count=3)
    Mdq_btn = ["1", "3", "6", "7", "10", "11", "14", "15", "18", "19"]
    for btn in Mdq_btn:
        page.locator(f"(//input[@type='radio'])[{btn}]").click()
    page.get_by_role("button", name="Save").click()    
     
    page.get_by_role("button", name="Psych Template").click()
    page.get_by_role("menuitem", name="CAGE").click()
    page.get_by_text("Cage Assessment").click(click_count=3)
    Cage_btn = ["2", "3", "5", "8"]
    for btn in Cage_btn:
        page.locator(f"(//input[@type='radio'])[{btn}]").click()
    page.get_by_role("button", name="Save").click()     
    
    page.get_by_role("button", name="Psych Template").click()
    page.get_by_role("menuitem", name="Substance Abuse").click()
    page.get_by_text("Substance Abuse Assessment").click(click_count=3)
    Substance_btn = ["1", "4", "5", "8", "10", "11", "13", "16", "17", "20"]
    for btn in Substance_btn:
        page.locator(f"(//input[@type='radio'])[{btn}]").click()
    page.get_by_role("button", name="Save").click()
    
    page.get_by_role("button", name="Save & Start Exam").click()
    print("Intake: Encounter Summary Updated Successfully")
    page.wait_for_timeout(2000)
    page.locator("//textarea[@name='followUp']").click()

    for _ in range(10):
        page.get_by_placeholder("Search & Select ICD Codes").fill(appointment.get("icd_code")[0])
        page.wait_for_timeout(1000)
        page.get_by_role("option", name=f"{appointment.get('icd_code')[0]} - {appointment.get('icd_code')[1]}").click()
        page.wait_for_timeout(1000)
        # page.locator("//textarea[@name='followUp']").click()      # to remove the option list
        if page.locator("span", has_text=f"{appointment.get('icd_code')[0]} - {appointment.get('icd_code')[1]}").is_visible(timeout=5000):
            break
        
    page.locator("//p[text()='Proc']/following::input[@placeholder='Select CPT Codes']").click()
    page.locator("//p[text()='Proc']/following::input[@placeholder='Select CPT Codes']").fill(appointment.get("cpt_code")[0])
    page.get_by_role("option", name=f"{appointment.get('cpt_code')[0]} - {appointment.get('cpt_code')[1]}").click()
    
    page.locator("//input[@name='carePlan']").fill(appointment.get("carePlan"))
    
    page.locator("//textarea[@name='followUp']").fill(appointment.get("followUp"))
    page.get_by_role("button", name="Done With Exam").click()
    print("Done With Exam: Encounter Summary Updated Successfully")
    page.wait_for_timeout(2000)

    page.locator(f"//p[text()='CHIEF COMPLAINT']/following::p[text()='{appointment.get('cheif_complaint')}']").click(click_count=3)
    page.locator(f"//p[text()='PROBLEM']/following::p[text()='{diagnosis_data.get('problem1')}']").click(click_count=3)
    assert page.locator(f"//p[text()='ALLERGIES']/following::p[text()='1. {allergy_data.get('allergy_name')}']").is_visible(), "Allergy not visible"       

    page.locator(f"//p[text()='HISTORY']/following::p[text()='Past Medical History']/following::p[text()='1. {history_data['condition1']}']/following::textarea[text()='{history_data['condition1_date'][1]}']").click(click_count=3)
    page.locator(f"//p[text()='HISTORY']/following::p[text()='Past Surgical History']/following::p[text()='1. {history_data['surgery1_name']}']/following::textarea[text()='{history_data['surgery1_date'][1]}']").click(click_count=3)
    page.locator(f"//p[text()='HISTORY']/following::p[text()='Family History']/following::p[text()='1. Grandparent']/following::textarea[text()='{history_data['problem1_name'][0]}']").click(click_count=3)
    page.locator(f"//p[text()='HISTORY']/following::p[text()='Habits']/following::textarea[text()='{history_data['habits']}']").click(click_count=3)
    medicine_name_2 = Medicine_name_1.split(" - ")[1]
    # page.locator(f"//p[text()='HISTORY']/following::p[text()='Medications']/following::p[text()='1. {medicine_name_2}']/following::textarea[text()='{medication_data['medication1_start_date'][1]}']").click(click_count=3)

    # page.locator(f"//p[text()='REVIEW OF SYSTEM']/following::p[text()='1. GENERAL']/following::textarea[text()='Testing ROS Template']").click(click_count=3)
    # page.locator(f"//p[text()='PHYSICAL EXAM']/following::p[text()='1. GENERAL']/following::textarea[text()='Testing PE Template']").click(click_count=3)    
    page.locator(f"//p[text()='ASSESSMENT']/following::p[text()='1. {appointment.get('icd_code')[0]}']").click(click_count=3)
    page.locator(f"//p[text()='CAREPLAN']/following::textarea[text()='{appointment.get('carePlan')}']").click(click_count=3)
    page.locator(f"//p[text()='FOLLOW UP']/following::textarea[text()='{appointment.get('followUp')}']").click(click_count=3)
    
    page.get_by_role("button", name="Save & Sign Notes").click()
    page.get_by_role("button", name="Sign").click()
    
    page.locator("//input[@name='provider']").inner_text()==local_data.provider1
    page.locator("//textarea[@name='providerNote']").fill(appointment.get("signOffNote"))
    
    canvas = page.get_by_title("Sign And Lock Diagnosis And Treatment Plan").locator("canvas")
    
    # For 'J'
    for y in range(90, 160, 3):
        canvas.click(position={"x":155,"y":y})

    for x in range(154, 120, -3):
        canvas.click(position={"x":x,"y":160})

    for y in range(159, 145, -3):
        canvas.click(position={"x":120,"y":y})

    # For 'E'
    for y in range(90, 160, 3):
        canvas.click(position={"x":175,"y":y})

    for x in range(175, 210, 3):
        canvas.click(position={"x":x,"y":90}) 

    for x in range(175, 210, 3):
        canvas.click(position={"x":x,"y":125})

    for x in range(175, 210, 3):
        canvas.click(position={"x":x,"y":160})

    page.get_by_role("button", name="Sign & Lock").click()
    if (page.get_by_text("Encounter SignOff Successfully").is_visible(timeout=10000)):
        print("Encounter SignOff Successfully")
           
    page.wait_for_timeout(5000)
    page.get_by_role("button", name="Close").click()
    page.wait_for_timeout(3000)
    
    page.locator("//div[@class='MuiBox-root css-p2lvj0']").drag_to(page.locator("//p[text()='Rows per page:']"))
    
    page.locator("(//p[text()='Search By Patient']/following::div[1]//input[@placeholder='Search & Select'])").fill(appointment.get("patient_name"))
    page.get_by_role("option", name=appointment.get("patient_name")).click()

    # page.locator("(//p[text()='Search By Provider']/following::div[1]//input[@placeholder='Search & Select'])").fill(local_data.provider1)    
    # page.get_by_role("option", name=local_data.provider1).click()
    page.wait_for_timeout(3000)
    
    page.get_by_role("cell", name=appointmnt_status[3]).get_by_text(appointmnt_status[3]).click()
    
    # Signed Off
    verify_appointment_and_patient_details(page, appointmnt_status[3], data.rescheduleTime, patientId)
    appointment_details(page, appointmnt_status[3])
    insurance_details(page)
    page.get_by_role("heading", name=appointmnt_status[3]).get_by_test_id("CloseIcon").click()
    
    page.locator(f"//p[text()='{appointment.get('patient_name')} ({patientId})']").click()
    
    page.locator("(//p[text()='Visit Details'])[1]").click()
    page.wait_for_timeout(400)
    page.get_by_role("cell", name=f"{data.formatted_date}, {data.rescheduleTime}").click()
    page.get_by_role("cell", name=local_data.provider1).click()
    page.get_by_role("cell", name="NEW").click()
    page.get_by_role("cell", name=appointment.get("cheif_complaint")).click()
    page.get_by_role("cell", name=appointmnt_status[3]).click()
    print("Visit Details verified successfully")
    
    page.get_by_test_id("FullscreenOutlinedIcon").click()
    page.get_by_role("button", name="Leave session").click()
    page.get_by_text("No Show", exact=True).click()
    page.get_by_text("Patient Didn't Joined the Call, are you want to Change the Status to No Show and").click()
    page.get_by_role("button", name="No").click()
    return patientId