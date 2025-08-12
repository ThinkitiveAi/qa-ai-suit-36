from playwright.sync_api import Page

from Automation.utils import creds, data, local_data

class TaskPage:
    def __init__(self, page: Page):
        self.page = page
        self.collaboration_tab = page.get_by_role("tab", name="Collaboration")
        self.tasks_link = page.get_by_text("Tasks")
        self.add_task_button = page.get_by_role("button", name="Add Task")
        self.add_task_heading = page.get_by_role("heading", name="Add Task")
        self.title_input = page.get_by_placeholder("Enter Title")
        self.priority_dropdown = page.get_by_label("Priority *")
        self.action_dropdown = page.get_by_label("Action *")
        self.due_date_input = page.get_by_placeholder("Choose Date")
        self.due_time_input = page.get_by_placeholder("hh:mm:aa")
        self.assignee_input = page.get_by_placeholder("Search Assignee")
        self.description_input = page.get_by_placeholder("Task Description")
        self.save_button = page.get_by_role("button", name="Save")
        self.update_button = page.get_by_role("button", name="Update")
        self.task_added_success_msg = page.get_by_text("Task added successfully.")
        self.task_updated_success_msg = page.get_by_text("task updated successfully")
        self.provider_centric_tab = page.get_by_role("tab", name="Provider Centric Tasks")
        self.patient_centric_tab = page.get_by_role("tab", name="Patient Centric Tasks")
        self.more_options_menu = page.get_by_test_id("MoreVertIcon")
        self.edit_menu_item = page.get_by_role("menuitem", name="Edit")
        self.close_dialog_button = page.get_by_test_id("CloseIcon")
        self.search_input = page.get_by_placeholder(" Assign To, Task Title")
        self.my_task_checkbox = page.get_by_label("My Tasks")
        self.todo_task_checkbox = page.get_by_label("To-Do Task")
        self.clockIcon = page.get_by_test_id("ClockIcon")
        self.assign_checkbox = page.get_by_label("Assign task to Provider")
        self.patient_input = page.get_by_placeholder("Search Patient")
        self.reassign_menu_item = page.get_by_role("menuitem", name="Reassign", exact=True)
        self.resolve_menu_item = page.get_by_role("menuitem", name="Resolve")   
        self.delete_menu_item = page.get_by_role("menuitem", name="Delete")   
        self.date_input = page.get_by_placeholder("MM-DD-YYYY")
        self.note_textbox = page.get_by_role("textbox", name="Note")
        self.assign_btn = page.get_by_role("button", name="Assign", exact=True)
        self.reassign_task_success_msg = page.get_by_text("Task reassigned successfully")
        self.resolve_btn = page.get_by_role("button", name="Resolved", exact=True)
        self.resolve_task_success_msg = page.get_by_text("Task resolved successfully")
        self.delete_task_success_msg = page.get_by_text("Task archived successfully.")
        self.batch_reassign_btn = page.get_by_role("button", name="Batch Reassign")
        self.batch_resolve_btn = page.get_by_role("button", name="Batch Resolve")
        self.batch_reassign_heading = page.get_by_role("heading", name="Reassign Task")
        self.batch_resolve_heading = page.get_by_role("heading", name="Batch Resolve").get_by_text("Batch Resolve")


    def navigate_to_tasks(self):
        self.collaboration_tab.click()
        self.tasks_link.click()

    def open_add_task_dialog(self):
        self.add_task_button.click()
        self.add_task_heading.wait_for()

    def fill_task_form(self, task: dict):
        if self.assign_checkbox.is_checked()==False:
            self.assign_checkbox.check()
        self.title_input.fill(task['TASK_TITLE'])
        self.priority_dropdown.click()
        self.page.get_by_role("option", name=task['TASK_PRIORITY']).click()
        self.action_dropdown.click()
        self.page.get_by_role("option", name=task['TASK_ACTION']).click()
        self.due_date_input.click()
        self.due_date_input.fill(data.dt_format(task['TASK_DUE_DAY'], "-"))
        self.due_time_input.click()
        self.clockIcon.click()
        self.page.get_by_role("option", name=task['TASK_HRS'], exact=True).click()
        self.page.get_by_role("option", name=task['TASK_MIN']).click()
        self.page.get_by_role("option", name=task['TASK_AM_PM']).click()
        if self.assignee_input.is_disabled()==False:
            self.assignee_input.fill(task['TASK_ASSIGNEE'])
            self.page.get_by_role("option", name=task['TASK_ASSIGNEE']).click()
        self.description_input.fill(task['TASK_DESCRIPTION'])

    def save_task(self):
        self.save_button.click()
        self.task_added_success_msg.click()
        
    def close_add_task_dialog(self):
         self.close_dialog_button.click()

    def edit_task(self):
        self.more_options_menu.click()
        self.edit_menu_item.click()
        
    def update_task(self):
        self.update_button.click()
        self.task_updated_success_msg.click()

    def view_provider_centric_tasks(self, verifyTask: dict):
        self.provider_centric_tab.click()
        self.my_task_checkbox.uncheck()
        self.search_input.fill(verifyTask['TASK_TITLE'])
        self.page.wait_for_timeout(1000)
        self.page.get_by_title(verifyTask['TASK_TITLE']).click(click_count=3)
        self.page.get_by_text(data.dt_format(verifyTask['TASK_DUE_DAY'], "/")).click(click_count=3)
        # self.page.get_by_text("Acknowledged").click(click_count=3)
        self.page.get_by_title(verifyTask['TASK_PRIORITY'].upper()).click(click_count=3)
        self.page.locator(f"//p[text()='{local_data.provider1}']/following::span[text()='{verifyTask['TASK_ASSIGNEE']}']").click(click_count=3)
        self.page.get_by_title(verifyTask['TASK_DESCRIPTION']).click(click_count=3)
        
    def reassign_task_menuitem(self):
        self.more_options_menu.click()
        self.reassign_menu_item.click()
        
    def reassign_task_form(self, reassign: dict):
        self.assignee_input.fill(f"{reassign['TASK_ASSIGNEE']}")
        self.page.get_by_role("option", name=f"{reassign['TASK_ASSIGNEE']}").click()
        self.date_input.fill(data.dt_format(reassign['TASK_DUE_DAY'], "-"))
        self.note_textbox.fill(f"{reassign['TASK_REASSIGN_NOTE']}")
        
    def assign_task_btn(self):
        self.assign_btn.click()
        self.reassign_task_success_msg.click()
        self.my_task_checkbox.check()
        
    def resolve_task_menuitem(self):
        self.more_options_menu.click()
        self.resolve_menu_item.click()
        
    def resolve_task_form(self, reassign: dict):
        self.note_textbox.fill(f"{reassign['TASK_RESOLVE_NOTE']}")
        
    def resolve_task_btn(self):
        self.resolve_btn.click()
        self.resolve_task_success_msg.click()    
        
    def resolve_task_verify(self, task: dict, reassign: dict):
        self.todo_task_checkbox.uncheck()
        self.page.locator(f"//div[text()='{task['TASK_TITLE']}']/following::p[text()='{data.dt_format(reassign['TASK_DUE_DAY'], '/')}']/following::div[text()='RESOLVED']").click(click_count=3)
        self.todo_task_checkbox.check()
        
        
    # ====================================================================================    
    def fill_task_form_patient(self, task: dict):
        self.assign_checkbox.uncheck()
        self.title_input.fill(task['TASK_TITLE'])
        self.priority_dropdown.click()
        self.page.get_by_role("option", name=task['TASK_PRIORITY']).click()
        self.patient_input.fill("")
        self.patient_input.fill(f"{task.get('patient_name')}")
        self.page.get_by_role("option", name=f"{task.get('patient_name')}").click()
        self.action_dropdown.click()
        self.page.get_by_role("option", name=task['TASK_ACTION']).click()
        self.due_date_input.click()
        self.due_date_input.fill(data.dt_format(task['TASK_DUE_DAY'], "-"))
        self.clockIcon.click()
        self.page.get_by_role("option", name=task['TASK_HRS'], exact=True).click()
        self.page.get_by_role("option", name=task['TASK_MIN']).click()
        self.page.get_by_role("option", name=task['TASK_AM_PM']).click()
        if self.assignee_input.is_disabled()==False:
            self.assignee_input.fill(task['TASK_ASSIGNEE'])
            self.page.get_by_role("option", name=task['TASK_ASSIGNEE']).click()
        self.description_input.fill(task['TASK_DESCRIPTION'])

    def save_task(self):
        self.save_button.click()
        self.task_added_success_msg.click()

    def view_patient_centric_tasks(self, verifyTask: dict):
        self.patient_centric_tab.click()
        self.my_task_checkbox.uncheck()
        self.search_input.fill(verifyTask['TASK_TITLE'])
        self.page.wait_for_timeout(1000)
        self.page.get_by_title(verifyTask['TASK_TITLE']).click(click_count=3)
        self.page.get_by_text(verifyTask['patient_name']).hover()
        self.page.get_by_text(data.dt_format(verifyTask['TASK_DUE_DAY'], "/")).click(click_count=3)
        # self.page.get_by_text("Acknowledged").click(click_count=3)
        self.page.get_by_title(verifyTask['TASK_PRIORITY'].upper()).click(click_count=3)
        self.page.locator(f"//p[text()='{local_data.provider1}']/following::span[text()='{verifyTask['TASK_ASSIGNEE']}']").click(click_count=3)
        self.page.get_by_title(verifyTask['TASK_DESCRIPTION']).click(click_count=3)
        
    
    def delete_task(self):
        self.more_options_menu.click()
        self.delete_menu_item.click()
        self.page.get_by_text("Are You Sure?").click()
        self.page.get_by_text("you want to delete Task").click()
        self.page.get_by_role("button", name="Yes,Sure").click()
        self.delete_task_success_msg.click()
        

    def batch_reassign(self):
        self.batch_reassign_btn.click()
        self.batch_reassign_heading.click()
        self.assignee_input.click()
        self.page.get_by_role("option", name=local_data.provider1).click()
        self.page.get_by_role("textbox", name="Note").fill("Note for Batch Reassign")
        self.assign_btn.click()
        self.reassign_task_success_msg.click()
        
        
    def batch_resolve(self):
        self.batch_resolve_btn.click()
        self.batch_resolve_heading.click()
        self.page.get_by_role("textbox", name="Note").click()
        self.page.get_by_role("textbox", name="Note").fill("Note for Batch Resolve")
        self.resolve_btn.click()
        self.resolve_task_success_msg.click()