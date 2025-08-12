from datetime import datetime, timedelta
from faker import Faker
import string
import random

fake = Faker()
first_name = fake.first_name_male()
last_name = fake.last_name()

def generate_random_digits(length):
    digit = string.digits
    return ''.join(random.choice(digit[1:]) for _ in range(length))

def generate_random_string(length):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_website():
    domain_name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(2, 10)))
    tlds = ['.com', '.net', '.org']
    tld = random.choice(tlds)
    website = f'https://{domain_name}{tld}'
    return website

current_date = datetime.now().date()
today_date = current_date.strftime("%m-%d-%Y")      # ex: 02-16-2024
formatted_date = current_date.strftime("%m/%d/%Y")        # ex: 02/16/2024
formatted_date_1 = current_date.strftime("%A %b %d")        # ex: Thursday Feb 06
day = current_date.strftime("%d").lstrip("0")      # ex: 6
weekday = current_date.strftime("%A")       # ex: Sunday
month = current_date.strftime("%b")     # Feb
month_name = current_date.strftime("%B")     # February
year = current_date.year        # 2025
two_days_ago = (current_date - timedelta(days=2)).strftime("%m-%d-%Y")
two_month_after = current_date + timedelta(days=60)
one_month_after = current_date + timedelta(days=30)

def insurance_dt(action, range):
    date = (current_date - timedelta(days=30)) if range == "month" else (current_date + timedelta(days=335))
    if action == "-":
        return date.strftime("%m-%d-%Y")
    return date.strftime("%m/%d/%Y")

def dt_format(date, format):
    if format == "-":
        return date.strftime("%m-%d-%Y")
    return date.strftime("%m/%d/%Y")
    
# Get current time and round to the next 15-minute mark
now = datetime.now()
# now = datetime.strptime("2025-02-24 12:01:51.493289", "%Y-%m-%d %H:%M:%S.%f")
minutes_to_next_slot = (15 - now.minute % 15) % 15
start_time = now + timedelta(minutes=minutes_to_next_slot)

# Generate future times in 15-minute intervals
time_list = [start_time + timedelta(minutes=15 * i) for i in range(10)]

time = []
# Format and display times with differences
for x in range(len(time_list)):
    formatted_time = time_list[x].strftime("%I:%M %p")
    time.append(formatted_time)
slot_time = f"{time[2]} - {time[3]}"
scheduleTime = time[2]
reschedule_slot = f"{time[1]} - {time[2]}"
rescheduleTime = time[1]
