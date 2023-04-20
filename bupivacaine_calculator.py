from Patient import Patient
from data import bupivacaine_dosage
import DataBase
# нужно сделать заполнениеDataBase c использованием класс меню
# задроч с кейборд интеррапт на написании имени пациентки

# mенюшка новый пациент
A = Patient(height=160, weight=57)
#A = Patient()
A.input_patient_data()
A.count_risk_factors(answers={'fetus': '', 'bladder': '', 'back_discomfort': ''})
#A.count_risk_factors(answers={})
A.get_bupivacaine_dose(A.count_a_sum(), bupivacaine_dosage)

# менюшка на запись статистики: варианты now, later
db = DataBase.DataBase()
#now
try:
    questionnaire_flag = True if input("Do you answer a some questions? Press y or n and enter\n: ") == 'y' else False
    db.write_patient_data_to_file(A.patient_data, questionnaire_flag)
except KeyboardInterrupt:
    db.write_patient_data_to_file(A.patient_data, questionnaire_flag=False)

#later = exit

#db.change_patient_with_missing_data()

