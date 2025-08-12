from playwright.sync_api import Playwright, sync_playwright, Page
from Automation.pages.collaboration.referral_page import ReferralPage
from Automation.pages.collaboration.task_page import TaskPage
from Automation.pages.patient.req_patient_page import add_patient
from Automation.test_data import patient_data
from Automation.utils import creds, data, local_data
from Automation.utils.browser import login, open_browser
from Automation.test_data.task_data import add_task_data, edit_task_data, reassign_task_data
from Automation.test_data.referall_data import add_referall_data, referral_in_add_patient_data

def test_add_and_edit_task(page: Page, playwright: Playwright):

    page = open_browser(playwright)
    credential = {
        "url": creds.provider_url,
        "email": creds.provider_email,
        "password": creds.provider_password
    }
    login(page, credential)
    add_patient(page, patient_data.patient_data)

    # Navigate to Tasks
    task_page = TaskPage(page)
    task_page.navigate_to_tasks()

# Provider Centric Tasks
# Add a new task
    task_page.open_add_task_dialog()
    task_page.fill_task_form(add_task_data)
    task_page.save_task()
    task_page.view_provider_centric_tasks(add_task_data)
# Edit the task
    task_page.edit_task()
    task_page.fill_task_form(edit_task_data)
    task_page.update_task()
    task_page.view_provider_centric_tasks(edit_task_data)
# Reassign the task
    task_page.reassign_task_menuitem()
    task_page.reassign_task_form(reassign_task_data)
    task_page.assign_task_btn()
# Resolved the task
    task_page.resolve_task_menuitem()
    task_page.resolve_task_form(reassign_task_data)
    task_page.resolve_task_btn()
    task_page.resolve_task_verify(edit_task_data, reassign_task_data)
    
# Patient Centric Tasks
# Add a new task
    task_page.open_add_task_dialog()
    task_page.fill_task_form_patient(add_task_data)
    task_page.save_task()
    task_page.view_patient_centric_tasks(add_task_data)
# Edit the task
    task_page.edit_task()
    task_page.fill_task_form_patient(edit_task_data)
    task_page.update_task()
    task_page.view_patient_centric_tasks(edit_task_data)
# Reassign the task
    task_page.reassign_task_menuitem()
    task_page.reassign_task_form(reassign_task_data)
    task_page.assign_task_btn()
# Resolved the task
    task_page.resolve_task_menuitem()
    task_page.resolve_task_form(reassign_task_data)
    task_page.resolve_task_btn()
    task_page.resolve_task_verify(edit_task_data, reassign_task_data)
    
    
# Navigate to Referral
    referral_page = ReferralPage(page)
    referral_page.navigate_to_referral()
# Referral Out
    referral_page.add_referral_out(add_referall_data)
    referral_page.referral_out_list(patient_data.patient_data, add_referall_data)
    # referral_page.referral_out_edit()
    
# Referral In
    referral_page.referral_in_add_patient(referral_in_add_patient_data)
    referral_page.add_referral_in(referral_in_add_patient_data, add_referall_data)
    referral_page.referral_in_list(referral_in_add_patient_data, add_referall_data)
