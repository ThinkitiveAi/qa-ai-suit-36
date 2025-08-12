import os
from dotenv import load_dotenv
load_dotenv()

admin_url = os.getenv("ADMIN_URL")
admin_email = os.getenv("ADMIN_EMAIL")
admin_password = os.getenv("ADMIN_PASSWORD")

provider_url = os.getenv("PROVIDER_URL")
provider_email = os.getenv("PROVIDER_EMAIL")
provider_password = os.getenv("PROVIDER_PASSWORD")

# To test practice settings
url = os.getenv("URL")
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# csv
provider_data_csv = "./Automation/utils/uploads/Sample_Provider_Data.csv"
cpt_code_csv = "./Automation/utils/uploads/Sample_CPT_Code.csv"
icd_code_csv = "./Automation/utils/uploads/Sample_ICD_10_Code.csv"
hcpcs_code_csv = "./Automation/utils/uploads/Sample_HCPCS_Code.csv"
loinc_code_csv = "./Automation/utils/uploads/Sample_LOINC_Code.csv"
patient_data_csv = "./Automation/utils/uploads/Sample_Patient_Data.csv"

#pdf
order_data_pdf = "./Automation/utils/uploads/test.pdf"
