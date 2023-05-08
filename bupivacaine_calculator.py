from Patient import Patient
from data import bupivacaine_dosage
import DataBase
from Menu import Menu
# здесь нужно поменять очередность расчетов: зачем считать факторы риска для СМА если у нас кровопотеря!

try:
    while True:
        print('Greetings in the bupivacaine calculator')
        gm = Menu(variants=('new patient', 'choose last patient and fill questionnaire', 'exit'))
        gm.print_variants()
        answer = gm.get_user_answer()
        db = DataBase.DataBase()
        if answer == 'new patient':
            A = Patient(height=170, weight=70)
            A.count_risk_factors(answers={'fetus': 'n', 'bladder': 'n', 'back_discomfort': 'n'})
            # A = Patient()
            # A.count_risk_factors(answers={})
            A.input_patient_data()

            while True:
                sm = Menu(question='What do you want?',
                          variants=('count dose of local anesthetic', 'patient is bleeding', 'back to main menu'))
                sm.print_a_question()
                sm.print_variants()
                second_answer = sm.get_user_answer()

                if second_answer == 'count dose of local anesthetic':
                    A.get_bupivacaine_dose(A.count_a_sum(), bupivacaine_dosage)
                    try:
                        q = True if input("Do you answer a some questions? Press 'y' or 'n' and enter\n: ") == 'y' else False
                        db.write_patient_data_to_file(A.patient_data, 'new', questionnaire_flag=q)
                    except KeyboardInterrupt:
                        db.write_patient_data_to_file(A.patient_data, 'new')

                elif second_answer == 'patient is bleeding':
                    pass # сюда можно всписать градацию шока на основе кровопотери, индекс алговера, расчеты по препаратам и всякое

                else:
                    break

        elif answer == 'choose last patient and fill questionnaire':
            db.write_patient_data_to_file(behavior='add')

        elif answer == 'exit':
            print('See you!')
            break
except KeyboardInterrupt:
    print()
    print('See you')
