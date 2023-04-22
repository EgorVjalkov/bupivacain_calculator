from Patient import Patient
from data import bupivacaine_dosage
import DataBase

# mенюшка новый пациент
A = Patient(height=0, weight=0)
#A = Patient()
A.input_patient_data()
A.count_risk_factors(answers={'fetus': '', 'bladder': '', 'back_discomfort': ''})
#A.count_risk_factors(answers={})
A.get_bupivacaine_dose(A.count_a_sum(), bupivacaine_dosage)

db = DataBase.DataBase()

try:
    q_flag = True if input("Do you answer a some questions? Press y or n and enter\n: ") == 'y' else False
    db.write_patient_data_to_file(A.patient_data, 'new', questionnaire_flag=q_flag)
except KeyboardInterrupt:
    db.write_patient_data_to_file(A.patient_data, 'new')
