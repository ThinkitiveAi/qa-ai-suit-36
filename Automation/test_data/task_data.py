import random
from Automation.test_data import patient_data
from Automation.utils import data, local_data

priority = ["High", "Low", "Medium"]
action = ["Call", "Email", "Message", "Other"]

add_task_data = {
    "patient_name": f"{patient_data.PATIENT_FNAME} {patient_data.PATIENT_LNAME}",
    "TASK_TITLE" : f"New Automated Task {data.generate_random_digits(5)}",
    "TASK_DESCRIPTION" : "This is a new task created by automation.",
    "TASK_PRIORITY" : random.choice(priority),
    "TASK_ACTION" : random.choice(action),
    "TASK_ASSIGNEE" : local_data.provider2,
    "TASK_DUE_DAY" : data.one_month_after,
    "TASK_HRS": "2 hours",
    "TASK_MIN": "10 minutes",
    "TASK_AM_PM": "AM",
}
edit_task_data = {
    "patient_name": f"{patient_data.PATIENT_FNAME} {patient_data.PATIENT_LNAME}",
    "TASK_TITLE" : f"Test Automated Task {data.generate_random_digits(5)}",
    "TASK_DESCRIPTION" : "This is a test task created by automation.",
    "TASK_PRIORITY" : random.choice(priority),
    "TASK_ACTION" : random.choice(action),
    "TASK_ASSIGNEE" : local_data.provider2,
    "TASK_DUE_DAY" : data.two_month_after,
    "TASK_HRS": "3 hours",
    "TASK_MIN": "15 minutes",
    "TASK_AM_PM": "PM", 
}
reassign_task_data = {
    "TASK_ASSIGNEE" : local_data.provider1,
    "TASK_DUE_DAY" : data.one_month_after,
    "TASK_REASSIGN_NOTE" : "Reassigning due to workload balance. Please prioritize completion by the due date.",
    "TASK_RESOLVE_NOTE" : "Task completed successfully. All required actions have been taken."
}
