from Patient import Patient
from data import bupivacaine_dosage

A = Patient(patient_name='', height=165, weight=120)
#A = Patient()
A.input_patient_data()
A.count_risk_factors(answers={'fetus': 'n', 'bladder': 'n', 'back_discomfort': 'y'})
#A.count_risk_factors(answers={})
print(A.get_bupivacaine_dose(A.count_a_sum(), bupivacaine_dosage))
# while True:
    # сделай datetime
    # диалог о написании статистики, еще надо сделать чтобы можно было заполнить для других теток данные по времени и дате
A.write_patient_data_to_file(questionnaire_flag=True)

