from playwright.sync_api import Page

from Automation.test_data.scheduling_data import verify_appointment_and_patient_details, appointment_details, insurance_details, appointmnt_status
from Automation.tests.provider.test_patient import diagnosis_data, allergy_data, history_data, medication_data
from Automation.utils import constants, creds, data, local_data
    
class OpenEncounter:
    def __init__(self, page: Page):
        self.page = page
        self.scheduling_tab = page.get_by_role("tab", name="Scheduling")
        self.appointments_tab = page.get_by_text("Appointments")
        self.schedule_appointment_btn = page.get_by_role("button", name="Schedule Appointment")
        self.appointment_type_menuitem = page.get_by_role("menuitem", name=constants.appointment[0])
        self.schedule_appointment_heading = page.get_by_role("heading", name="Schedule Appointment").get_by_text("Schedule Appointment")
        self.search_patient_input = page.get_by_placeholder("Search Patient")
        self.appointment_type_input = page.get_by_placeholder("Select Type")
        self.reason_input = page.get_by_placeholder("Reason")
        self.timezone_input = page.locator("//input[@name='timezone']")
        self.timezone_option = page.get_by_role("option", name="Indian Standard Time (GMT +05:30)")
        self.visit_type_button = page.get_by_role("button", name=constants.visit_type[1])
        self.search_provider_input = page.get_by_placeholder("Search Provider")
        self.provider_option = page.get_by_role("option", name=local_data.provider1)
        self.view_availability_btn = page.get_by_role("button", name="View availability")
        self.slot_day_cell = page.get_by_role("gridcell", name=data.day, exact=True)
        self.slot_time_btn = page.get_by_role("button", name=data.slot_time)
        self.appointment_note_input = page.get_by_placeholder("Appointment Note")
        self.save_close_btn = page.get_by_role("button", name="Save And Close")
        self.success_toast = page.get_by_text("Appointment booked successfully")
        self.search_by_patient_tab = page.get_by_text("Search By Patient")
        self.patient_search_select = page.get_by_placeholder("Search & Select").first
        self.search_by_provider_tab = page.get_by_text("Search By Provider")
        self.provider_search_select = page.get_by_placeholder("Search & Select").nth(1)
        self.appointment_type_btn = page.get_by_role("button", name="Appointment Type")
        self.appointment_type_checkbox = page.get_by_label(constants.appointment_type[0])
        self.save_btn = page.get_by_role("button", name="Save")
        self.close_btn = page.get_by_role("button", name="Close")
        self.date_picker = page.get_by_placeholder("Choose Date")
        
        # Reschedule
        self.reschedule_button = page.get_by_role("button", name="Reschedule Appointment")
        self.reschedule_heading = page.get_by_role("heading", name="Reschedule Appointment").get_by_text("Reschedule Appointment")
        self.confirm_button = page.get_by_role("button", name="Confirm Appointment")
        self.confirm_success_toast = page.get_by_text("Appointment updated successfully.")
        self.status_confirmed_cell = page.get_by_role("cell", name=appointmnt_status[1]).get_by_text(appointmnt_status[1])
        
        # Check-in
        self.start_checkin_button = page.get_by_role("button", name="Start Check In")
        self.checkin_text = page.get_by_text("Check In", exact=True)
        self.checkin_visit_type = page.get_by_title("Check In").get_by_text(constants.visit_type[1])
        self.checkin_appointment_type_label = page.get_by_title("Check In").get_by_text("Appointment Type")
        self.checkin_appointment_type = page.get_by_title("Check In").get_by_text(constants.appointment_type[0])
        self.checkin_provider_label = page.get_by_text("Primary Provider Name")
        self.checkin_provider = page.get_by_title("Check In").get_by_text(local_data.provider1)
        self.checkin_reason_label = page.get_by_title("Check In").get_by_text("Reason For Visit")
        
        # Video & Appointment Controls
        self.unmute_btn = page.locator("//div[@aria-label='unmute']")
        self.mute_btn = page.locator("//div[@aria-label='mute']")
        self.start_camera_btn = page.get_by_role("button", name="start camera")
        self.stop_camera_btn = page.get_by_role("button", name="stop camera")
        self.ready_to_join_text = page.get_by_text("Ready to join?")
        self.start_appointment_btn = page.get_by_role("button", name="Start Appointment")
        
        # Session controls
        self.session_summary = page.get_by_text(f"{local_data.provider1}")
        self.remove_icon = page.get_by_test_id("RemoveOutlinedIcon")
        self.leave_session_btn = page.get_by_role("button", name="Leave session", exact=True)
        self.leave_no_btn = page.get_by_role("button", name="No")
        self.leave_yes_btn = page.get_by_role("button", name="Leave", exact=True)
        self.leave_confirm_yes_btn = page.get_by_role("button", name="Yes,Sure")

        # Encounter Completion
        self.collaboration_tab = page.get_by_role("tab", name="Collaboration")
        self.open_encounters_tab = page.get_by_text("Open Encounters")
        self.more_options_icon = page.get_by_test_id("MoreVertIcon").first
        self.complete_encounter_text = page.get_by_text("Complete Encounter")
        self.start_encounter_btn = page.get_by_role("button", name="Start Encounter")
        self.soap_note_btn = page.get_by_role("button", name="Simple Soap Note")
        self.psychiatric_note_text = page.get_by_text("Psychiatric Note")
        self.save_start_exam_btn = page.get_by_role("button", name="Save & Start Exam")
        
        # Encounter Note & Templates
        self.soap_note_option = self.page.locator("//p[text()='Simple Soap Note']")
        self.psychiatric_note_option = self.page.get_by_role("menuitem", name="Psychiatric Note")
        self.encounter_date = self.page.get_by_text(f"{data.day} {data.month} {data.year}")
        self.encounter_time = self.page.get_by_text(data.rescheduleTime)
        self.provider_selection = self.page.locator(f"//p[text()='Provider']/following::p[text()='{local_data.provider1}']")
        self.visit_type_note = self.page.get_by_text(f"{constants.visit_type[1]} Visit")
        self.problem_input = self.page.locator("//input[@name='problems']")

        # Allergy
        self.add_allergy_btn = self.page.get_by_role("button", name="Add Allergy")
        self.allergy_name_input = self.page.get_by_placeholder("Enter Allergy Name")
        self.allergy_severity_dropdown = self.page.get_by_placeholder("Select Severity")
        self.allergy_reaction_input = self.page.get_by_placeholder("Enter Reaction")
        self.allergy_status_dropdown = self.page.get_by_placeholder("Select", exact=True)
        self.allergy_note_input = self.page.get_by_placeholder("Type here")
        self.allergy_success = self.page.get_by_text("Allergy created successfully")

        # PMH
        self.add_pmh_btn = self.page.get_by_role("button", name="Add PMH")
        self.pmh_condition_input = self.page.get_by_placeholder("Enter Condition Name")
        self.pmh_note_input = self.page.get_by_placeholder("Type here")
        self.pmh_success = self.page.get_by_text("Past Medical history created successfully")
        
        # PSH
        self.add_psh_btn = page.get_by_role("button", name="Add PSH")
        self.psh_name_input = page.get_by_placeholder("Enter Surgery Name")
        self.psh_note_input = page.get_by_placeholder("Type here")
        self.psh_success_msg = page.get_by_text("Past Surgical history created successfully")

        # Family History
        self.add_fh_btn = self.page.get_by_role("button", name="Add FH")
        self.fh_problem_input = self.page.get_by_placeholder("Select or Search Problem")
        self.fh_relative_dropdown = self.page.locator("input[name=\"relative\"]")
        self.fh_age_input = self.page.get_by_placeholder("Enter Age")
        self.fh_note_input = self.page.get_by_placeholder("Type here")
        self.fh_success = self.page.get_by_text("Family history created successfully")
        
        self.habbits_input = self.page.locator("//input[@name='habits']")

        # Medications
        self.add_med_btn = self.page.get_by_role("button", name="Add Med")
        self.med_search_dropdown = self.page.get_by_placeholder("Select Or Search Medicine")
        self.med_quantity_input = self.page.get_by_placeholder("Enter Quantity")
        self.med_dosage_unit = self.page.get_by_placeholder("Dosage Unit")
        self.med_frequency = self.page.get_by_placeholder("frequency")
        self.med_when = self.page.get_by_placeholder("When")
        self.med_time = self.page.get_by_placeholder("Time")
        self.med_start_date = self.page.locator("//input[@name='medicationStartDate']")
        self.med_end_date = self.page.locator("(//input[@placeholder='Choose Date'])[2]")
        self.med_provider_input = self.page.get_by_placeholder("Select Provider")
        self.med_note_input = self.page.get_by_placeholder("Type here")
        self.med_success = self.page.get_by_text("Medication created successfully")

        # ROS Template
        self.ros_btn = self.page.get_by_role("button", name="ROS Template")
        self.ros_template_title = self.page.locator("//p[text()='ROS Templates']")
        self.ros_speciality = self.page.get_by_placeholder("Speciality")
        self.ros_template_select = self.page.get_by_placeholder("Select Template")
        self.ros_export_btn = self.page.get_by_role("button", name="Export to Note")
        self.ros_success = self.page.get_by_text("Template updated successfully")

        # Vitals
        self.bp_sys_input = self.page.get_by_placeholder("Sys", exact=True)
        self.bp_dia_input = self.page.get_by_placeholder("Dia", exact=True)
        self.spo2_input = self.page.get_by_placeholder("%")
        self.height_input = self.page.get_by_placeholder("cm", exact=True)
        self.bmi_input = self.page.get_by_placeholder("kg/m^2")
        self.bpm_input = self.page.get_by_placeholder("BPM", exact=True)
        self.weight_input = self.page.get_by_placeholder("lbs", exact=True)
        self.temp_input = self.page.get_by_placeholder("f", exact=True)

        # Save & Sign
        self.save_sign_btn = self.page.get_by_role("button", name="Save & Sign Notes")
        self.sign_btn = self.page.get_by_role("button", name="Sign")
        self.provider_note_input = self.page.locator("//textarea[@name='providerNote']")
        self.signature_canvas = self.page.get_by_title("Sign And Lock Diagnosis And Treatment Plan").locator("canvas")
        self.sign_lock_btn = self.page.get_by_role("button", name="Sign & Lock")
        self.signoff_success = self.page.get_by_text("Encounter SignOff Successfully")
        self.status_signoff_cell = page.get_by_role("cell", name=appointmnt_status[3]).get_by_text(appointmnt_status[3])
        
        # PE Template
        self.pe_template_btn = page.get_by_role("button", name="PE Template")
        self.pe_templates_heading = page.locator("//p[text()='PE Templates']")
        self.speciality_dropdown = page.get_by_placeholder("Speciality")
        self.template_dropdown = page.get_by_placeholder("Select Template")
        self.export_to_note_btn = page.get_by_role("button", name="Export to Note")
        self.template_success_msg = page.get_by_text("Template updated successfully")

        # Psych Template Menu
        self.psych_template_btn = page.get_by_role("button", name="Psych Template")
        self.menuitem_phq9 = page.get_by_role("menuitem", name="PHQ-9")
        self.menuitem_gad7 = page.get_by_role("menuitem", name="GAD-7")
        self.menuitem_mdq = page.get_by_role("menuitem", name="MDQ")
        self.menuitem_cage = page.get_by_role("menuitem", name="CAGE")
        self.menuitem_substance_abuse = page.get_by_role("menuitem", name="Substance Abuse")
        
        # Assessment Titles
        self.phq9_title = page.get_by_text("Phq9 Assessment")
        self.gad7_title = page.get_by_text("Gad7 Assessment")
        self.mdq_title = page.get_by_text("Mdq Assessment")
        self.cage_title = page.get_by_text("Cage Assessment")
        self.substance_abuse_title = page.get_by_text("Substance Abuse Assessment")
        
        self.done_with_exam_btn = page.get_by_role("button", name="Done With Exam")
        self.sign_notes_btn = page.get_by_role("button", name="Save & Sign Notes")
        self.sign_btn = page.get_by_role("button", name="Sign")
        self.sign_lock_btn = page.get_by_role("button", name="Sign & Lock")

        self.provider_input = page.locator("//input[@name='provider']")
        self.provider_note = page.locator("//textarea[@name='providerNote']")
        self.signature_canvas = page.get_by_title("Sign And Lock Diagnosis And Treatment Plan").locator("canvas")

        self.icd_input = page.get_by_placeholder("Search & Select ICD Codes")
        self.chief_complaint_click = page.get_by_text("Chief Complaint")
        self.cpt_input = page.locator("//p[text()='Proc']/following::input[@placeholder='Select CPT Codes']")
        self.care_plan_input = page.locator("//input[@name='carePlan']")
        self.follow_up_input = page.locator("//textarea[@name='followUp']")

        self.search_by_patient_input = page.locator("(//p[text()='Search By Patient']/following::div[1]//input[@placeholder='Search & Select'])")
        self.search_by_provider_input = page.locator("(//p[text()='Search By Provider']/following::div[1]//input[@placeholder='Search & Select'])")
        self.fullscreen_icon = page.get_by_test_id("FullscreenOutlinedIcon")
        self.leave_session_btn = page.get_by_role("button", name="Leave session")
        self.no_show_text = page.get_by_text("No Show", exact=True)
        self.no_btn = page.get_by_role("button", name="No")

        self.drag_widget = page.locator("//div[@class='MuiBox-root css-p2lvj0']")
        self.rows_per_page = page.locator("//p[text()='Rows per page:']")

        self.visit_details_tab = page.locator("(//p[text()='Visit Details'])[1]")
        
        
    def encounter_flow(self, appointment: dict) -> None:
        self.scheduling_tab.click()
        self.appointments_tab.click()
        self.page.wait_for_timeout(500)

        # Schedule Appointment
        self.schedule_appointment_btn.click()
        self.appointment_type_menuitem.click()
        self.schedule_appointment_heading.click(click_count=3)

        self.search_patient_input.click()
        self.page.get_by_role("option", name=appointment.get("patient_name")).click()
        print(f"New Appointment (Selected Patient): {appointment.get('patient_name')}")

        self.appointment_type_input.click()  # Appointment Type
        self.page.get_by_role("option", name=constants.appointment_type[0]).click()
        
        self.reason_input.fill(appointment.get("cheif_complaint"))

        self.timezone_input.click()
        self.timezone_option.click()

        self.visit_type_button.click()  # Visit type

        self.search_provider_input.fill(local_data.provider1)
        self.provider_option.click()

        self.view_availability_btn.click()
        self.slot_day_cell.click()
        print("schedule_slot: ", data.slot_time)
        self.slot_time_btn.click()

        self.appointment_note_input.fill(appointment.get("new_appointment_note"))
        self.save_close_btn.click()
        self.success_toast.click(click_count=3)
        self.page.wait_for_timeout(1000)

        self.search_by_patient_tab.click()
        self.patient_search_select.click()
        self.page.get_by_role("option", name=appointment.get("patient_name")).click()

        self.search_by_provider_tab.click()
        self.provider_search_select.click()
        self.page.get_by_role("option", name=local_data.provider1).click()

        self.appointment_type_btn.click()
        self.appointment_type_checkbox.check()
        self.page.wait_for_timeout(2000)

        namewithid = self.page.locator("//p[@class='MuiTypography-root MuiTypography-body1 css-1fi2nf3']").inner_text()
        patientId = namewithid.split('(')[1].split(')')[0]

        self.page.get_by_role("cell", name=f"{data.scheduleTime} | 15 Mins").get_by_text(data.scheduleTime).click()
        self.page.get_by_role("cell", name=constants.visit_type[1]).click()

        assert self.page.get_by_text(f"{appointment.get('patient_name')} ({patientId})").is_visible(), "Patient Name & ID is Not Visible"

        self.page.get_by_role("cell", name=constants.appointment_type[0]).click()
        self.page.get_by_role("cell", name=f"{local_data.provider1} Multispecialty").get_by_text(local_data.provider1).click()
        self.page.get_by_role("cell", name=appointment.get("cheif_complaint")).click()
        self.page.get_by_role("cell", name=appointmnt_status[0]).get_by_text(appointmnt_status[0]).click()

        # Scheduled
        verify_appointment_and_patient_details(self.page, appointmnt_status[0], data.scheduleTime, patientId)
        appointment_details(self.page, appointmnt_status[0])
        print("Appointment booked successfully & verified")

        # Reschedule
        self.reschedule_button.click()
        self.reschedule_heading.click()

        if (
            self.page.locator(f"//p[text()='Patient Name']/following::p[text()='{appointment.get('patient_name')}']").is_visible()
            and self.page.locator(f"//p[text()='Provider Name']/following::p[text()='{local_data.provider1}']").is_visible()
            and self.page.get_by_title("Reschedule Appointment").locator(f"//p[text()='Appointment Status']/following::p[text()='{appointmnt_status[0]}']").is_visible()
            and self.page.get_by_title("Reschedule Appointment").locator(f"//p[text()='Appointment Type']/following::p[text()='{constants.appointment_type[0]}']").is_visible()
            and self.page.get_by_title("Reschedule Appointment").locator(f"//p[text()='Visit Type']/following::p[text()='{constants.visit_type[1]}']").is_visible()
        ):
            self.slot_day_cell.click()
            print("reschedule_slot: ", data.reschedule_slot)
            self.page.get_by_role("button", name=data.reschedule_slot).click()
            self.save_close_btn.click()

        self.confirm_button.click()
        self.confirm_success_toast.click()
        self.status_confirmed_cell.click()

        verify_appointment_and_patient_details(self.page, appointmnt_status[1], data.rescheduleTime, patientId)
        appointment_details(self.page, appointmnt_status[1])
        print("Appointment Updated successfully & verified")

        # Check-in
        self.start_checkin_button.click()
        self.checkin_text.click()
        self.checkin_visit_type.click()
        self.checkin_appointment_type_label.click()
        self.checkin_appointment_type.click()
        self.checkin_provider_label.click()
        self.checkin_provider.click()
        self.checkin_reason_label.click()
        self.page.get_by_title("Check In").get_by_text(appointment.get("cheif_complaint")).click()
        self.page.get_by_role("button", name="Complete Check In").click()
        self.page.wait_for_timeout(1000)

        # Audio/Video simulation
        self.unmute_btn.click()
        self.page.wait_for_timeout(1000)
        self.mute_btn.click()
        self.page.wait_for_timeout(1000)
        self.unmute_btn.click()

        self.start_camera_btn.click()
        self.page.wait_for_timeout(1000)
        self.stop_camera_btn.click()
        self.page.wait_for_timeout(1000)
        self.start_camera_btn.click()

        self.ready_to_join_text.click()
        self.start_appointment_btn.click()

        self.page.get_by_text(f"{appointment.get('patient_name')} Appointment With Provider {local_data.provider1}").click()

        self.unmute_btn.click()
        self.page.wait_for_timeout(1000)
        self.mute_btn.click()
        self.page.wait_for_timeout(1000)
        self.unmute_btn.click()

        self.start_camera_btn.click()
        self.page.wait_for_timeout(1000)
        self.stop_camera_btn.click()
        self.page.wait_for_timeout(1000)
        self.start_camera_btn.click()
        self.start_encounter_btn.click()
        
        self.soap_note_btn.click()
        self.psychiatric_note_option.click()
        self.page.wait_for_timeout(500)
        self.problem_input.fill(diagnosis_data.get("problem1"))

        self.add_allergy_btn.click()
        self.allergy_name_input.fill(allergy_data.get("allergy_name"))
        self.allergy_severity_dropdown.click()
        self.page.get_by_role("option", name=allergy_data.get("allergy_severity")).click()
        self.allergy_reaction_input.fill(allergy_data.get("allergy_reaction"))
        self.date_picker.click()
        self.date_picker.fill("03-22-2020")
        self.allergy_status_dropdown.click()
        self.page.get_by_role("option", name="Inactive").click()
        self.allergy_note_input.fill(allergy_data.get("allergy_note"))
        self.save_btn.click()
        self.allergy_success.click()
        self.page.wait_for_timeout(1000)

        self.add_pmh_btn.click()
        self.pmh_condition_input.fill(history_data["condition1"])
        self.date_picker.click()
        self.date_picker.fill(history_data["condition1_date"][0])
        self.pmh_note_input.fill(history_data["condition1_note"])
        self.save_btn.click()
        self.pmh_success.click()
        self.page.wait_for_timeout(1000)

        self.add_psh_btn.click()
        self.psh_name_input.fill(history_data["surgery1_name"])
        self.date_picker.click()
        self.date_picker.fill(history_data['surgery1_date'][0])
        self.psh_note_input.fill(history_data["surgery1_note"])
        self.save_btn.click()
        self.psh_success_msg.click()
        self.page.wait_for_timeout(1000)

        self.add_fh_btn.click()
        self.fh_problem_input.fill(history_data["problem1_name"][1])
        self.page.get_by_role("option", name=history_data["problem1_name"][0]).click()
        self.fh_relative_dropdown.click()
        self.page.get_by_role("option", name="Grandparent", exact=True).click()
        self.fh_age_input.fill("65")
        self.fh_note_input.fill(history_data["problem1_note"])
        self.save_btn.click()
        self.fh_success.click()

        self.habbits_input.fill(history_data['habits'])

        self.add_med_btn.click()
        self.med_search_dropdown.click()
        self.page.get_by_role("option", name=medication_data["medicine1"]).click()
        self.med_quantity_input.fill("100")
        self.med_dosage_unit.click()
        self.page.get_by_role("option", name="Tablet (s)", exact=True).click()
        self.med_frequency.click()
        self.page.get_by_role("option", name="Every Day").click()
        self.med_when.click()
        self.page.get_by_role("option", name="Before Meal").click()
        self.med_time.click()
        self.page.get_by_role("option", name="Oral").click()
        self.med_start_date.click()
        self.med_start_date.fill(medication_data['medication1_start_date'][0])
        self.med_end_date.click()
        self.med_end_date.fill("11-20-2024")
        self.med_provider_input.click()
        self.med_provider_input.fill(local_data.provider1)
        self.page.get_by_role("option", name=local_data.provider1).click()
        self.med_note_input.click()
        self.med_note_input.fill(medication_data["medication_note1"])
        self.save_btn.click()
        self.med_success.click()

        self.ros_btn.click()
        self.ros_template_title.click()
        self.ros_speciality.click()
        self.page.get_by_role("option", name=constants.speciality[2]).click()
        self.ros_template_select.click()
        self.page.get_by_role("option", name=local_data.ros_template).click()
        self.ros_export_btn.click()
        self.ros_success.click()

        self.bp_sys_input.fill("125")
        self.bp_dia_input.fill("90")
        self.spo2_input.fill("92")
        self.height_input.fill("177")
        self.bmi_input.fill("24")
        self.bpm_input.fill("60")
        self.weight_input.fill("143")
        self.temp_input.fill("96")

        # PE Template
        self.pe_template_btn.click()
        self.pe_templates_heading.click()
        self.speciality_dropdown.click()
        self.page.get_by_role("option", name=constants.speciality[0]).click()
        self.template_dropdown.click()
        self.page.get_by_role("option", name=local_data.pe_template).click()
        self.export_to_note_btn.click()
        self.template_success_msg.click()

        self.psych_template_btn.click()
        self.menuitem_phq9.click()
        self.phq9_title.click(click_count=3)
        Phq9_btn = ["2", "7", "10", "16", "17", "22", "25", "30", "33"]
        for btn in Phq9_btn:
            self.page.locator(f"(//input[@type='radio'])[{btn}]").click()
        self.save_btn.click()    

        self.psych_template_btn.click()
        self.page.get_by_role("menuitem", name="GAD-7").click()
        self.gad7_title.click(click_count=3)
        Gad7_btn = ["2", "7", "12", "14", "17", "23", "25"]
        for btn in Gad7_btn:
            self.page.locator(f"(//input[@type='radio'])[{btn}]").click()
        self.save_btn.click()    

        self.save_start_exam_btn.click()
        self.page.wait_for_timeout(2000)
        self.leave_session_btn.click()
        self.leave_no_btn.click()
        self.page.wait_for_timeout(1000)
        self.leave_yes_btn.click()
        self.leave_confirm_yes_btn.click()

        self.collaboration_tab.click()
        self.open_encounters_tab.click()

        self.more_options_icon.click()
        self.complete_encounter_text.click()

        self.start_appointment_btn.click()
        self.start_encounter_btn.click()

        self.encounter_date.click()
        self.encounter_time.click()
        self.provider_selection.click()
        self.visit_type_note.click()
        
        self.icd_input.fill(appointment.get("icd_code")[0])
        self.page.get_by_role("option", name=f"{appointment.get('icd_code')[0]} - {appointment.get('icd_code')[1]}").click()
        self.page.wait_for_timeout(1000)
        self.chief_complaint_click.click()

        self.cpt_input.fill(appointment.get("cpt_code")[0])
        self.page.get_by_role("option", name=f"{appointment.get('cpt_code')[0]} - {appointment.get('cpt_code')[1]}").click()
        self.care_plan_input.fill(appointment.get("carePlan"))
        self.follow_up_input.fill(appointment.get("followUp"))
        self.done_with_exam_btn.click()
        
        print("Exam: Encounter Summary Updated Successfully")
        self.page.wait_for_timeout(2000)
    
        self.page.locator(f"//p[text()='CHIEF COMPLAINT']/following::p[text()='{appointment.get('cheif_complaint')}']").click(click_count=3)
        self.page.locator(f"//p[text()='PROBLEM']/following::p[text()='{diagnosis_data.get('problem1')}']").click(click_count=3)
        assert self.page.locator(f"//p[text()='ALLERGIES']/following::p[text()='1. {allergy_data.get('allergy_name')}']").is_visible(), "Allergy not visible"       
    
        self.page.locator(f"//p[text()='HISTORY']/following::p[text()='Past Medical History']/following::p[text()='1. {history_data['condition1']}']/following::textarea[text()='{history_data['condition1_date'][1]}']").click(click_count=3)
        self.page.locator(f"//p[text()='HISTORY']/following::p[text()='Past Surgical History']/following::p[text()='1. {history_data['surgery1_name']}']/following::textarea[text()='{history_data['surgery1_date'][1]}']").click(click_count=3)
        self.page.locator(f"//p[text()='HISTORY']/following::p[text()='Family History']/following::p[text()='1. Grandparent']/following::textarea[text()='{history_data['problem1_name'][0]}']").click(click_count=3)
        self.page.locator(f"//p[text()='HISTORY']/following::p[text()='Habits']/following::textarea[text()='{history_data['habits']}']").click(click_count=3)
        self.page.locator(f"//p[text()='HISTORY']/following::p[text()='Medications']/following::p[text()='1.  {medication_data['medicine1']}']/following::textarea[text()='{medication_data['medication1_start_date'][1]}']").click(click_count=3)
        # page.locator(f"//p[text()='REVIEW OF SYSTEM']/following::p[text()='1. GENERAL']/following::textarea[text()='Testing ROS Template']").click(click_count=3)
        # page.locator(f"//p[text()='PHYSICAL EXAM']/following::p[text()='1. GENERAL']/following::textarea[text()='Testing PE Template']").click(click_count=3)    
        self.page.locator(f"//p[text()='ASSESSMENT']/following::p[text()='1. {appointment.get('icd_code')[0]}']").click(click_count=3)
        self.page.locator(f"//p[text()='CAREPLAN']/following::textarea[text()='{appointment.get('carePlan')}']").click(click_count=3)
        self.page.locator(f"//p[text()='FOLLOW UP']/following::textarea[text()='{appointment.get('followUp')}']").click(click_count=3)

        self.sign_notes_btn.click()
        self.sign_btn.click()
        self.provider_note_input.fill(appointment.get("signOffNote"))
        canvas = self.signature_canvas
        for y in range(90, 160, 3): 
            canvas.click(position={"x": 155, "y": y})
        for x in range(154, 120, -3): 
            canvas.click(position={"x": x, "y": 160})
        for y in range(159, 145, -3): 
            canvas.click(position={"x": 120, "y": y})
        for y in range(90, 160, 3): 
            canvas.click(position={"x": 175, "y": y})
        for x in range(175, 210, 3): 
            canvas.click(position={"x": x, "y": 90})
        for x in range(175, 210, 3): 
            canvas.click(position={"x": x, "y": 125})
        for x in range(175, 210, 3): 
            canvas.click(position={"x": x, "y": 160})
        
        self.sign_lock_btn.click()
        if (self.signoff_success.is_visible(timeout=3000)):
            print(self.signoff_success)
        self.page.wait_for_timeout(5000)
        self.close_btn.click()
        self.page.wait_for_timeout(3000)

        self.drag_widget.drag_to(self.rows_per_page)

        self.search_by_patient_input.fill(appointment.get("patient_name"))
        self.page.get_by_role("option", name=appointment.get("patient_name")).click()
        
    
        self.search_by_provider_input.fill(local_data.provider1)
        self.page.get_by_role("option", name=local_data.provider1).click()
        self.page.wait_for_timeout(3000)

        self.status_signoff_cell.click()

        # Signed Off
        verify_appointment_and_patient_details(self.page, appointmnt_status[3], data.rescheduleTime, patientId)
        appointment_details(self.page, appointmnt_status[3])
        # insurance_details(page)
        self.page.get_by_role("heading", name=appointmnt_status[3]).get_by_test_id("CloseIcon").click()

        self.page.locator(f"//p[text()='{appointment.get('patient_name')} ({patientId})']").click()

        self.visit_details_tab.click()
        self.page.wait_for_timeout(400)
        self.page.get_by_role("cell", name=f"{data.formatted_date}, {data.rescheduleTime}").click()
        self.page.get_by_role("cell", name=local_data.provider1).click()
        self.page.get_by_role("cell", name="NEW").click()
        self.page.get_by_role("cell", name=appointment.get("cheif_complaint")).click()
        self.page.get_by_role("cell", name=appointmnt_status[3]).click()
        print("Visit Details verified successfully")

        self.fullscreen_icon.click()
        self.leave_session_btn.click()
        self.no_show_text.click()
        self.page.get_by_text("Patient Didn't Joined the Call, are you want to Change the Status to No Show and").click()
        self.no_btn.click()
        return patientId