from Patient import Patient
from data import bupivacaine_dosage

A = Patient(patient_name='Lyalya', height=165, weight=120)
A.input_patient_data()
A.count_risk_factors(answers={'fetus': 'n', 'bladder': 'n', 'back_discomfort': 'y'})
# сделай функцию для записи статистики
print(A.get_bupivacaine_dose(A.count_a_sum(), bupivacaine_dosage))
print(A.patient_data)
A.write_patient_data_to_file()
