from Patient import Patient
from data import bupivacaine_dosage
import DataBase
from Menu import Menu


try:
    while True:
        gm = Menu(variants=('new patient', 'choose last patient and fill questionnaire', 'exit'))
        gm.print_variants()
        answer = gm.get_user_answer()
        db = DataBase.DataBase()
        if answer == 'new patient':
            #A = Patient(height=170, weight=70)
            A = Patient()
            A.input_patient_data()
            #A.count_risk_factors(answers={'fetus': '', 'bladder': '', 'back_discomfort': ''})
            A.count_risk_factors(answers={})
            A.get_bupivacaine_dose(A.count_a_sum(), bupivacaine_dosage)
            try:
                q = True if input("Do you answer a some questions? Press 'y' or 'n' and enter\n: ") == 'y' else False
                db.write_patient_data_to_file(A.patient_data, 'new', questionnaire_flag=q)
            except KeyboardInterrupt:
                db.write_patient_data_to_file(A.patient_data, 'new')

        elif answer == 'choose last patient and fill questionnaire':
            db.write_patient_data_to_file(behavior='add')

        elif answer == 'exit':
            print('See you!')
            break
except KeyboardInterrupt:
    print()
    print('See you')
