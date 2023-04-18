from Patient import Patient
from data import bupivacaine_dosage
import DataBase


db = DataBase.DataBase()

A = Patient(patient_name='', height=0, weight=0)
#A = Patient()
A.input_patient_data()
A.count_risk_factors(answers={'fetus': '', 'bladder': '', 'back_discomfort': ''})
#A.count_risk_factors(answers={})
A.get_bupivacaine_dose(A.count_a_sum(), bupivacaine_dosage)
db.write_patient_data_to_file(A.patient_data, questionnaire_flag=True)

