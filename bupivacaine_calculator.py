from Patient import Patient
from data import bupivacaine_dosage
import DataBase
from Menu import Menu

try:
    while True:
        print('Greetings!\n')
        main_m = Menu(topic='С чего начать работу?',
                      variants=('новый пациент', 'выбрать пациента из базы данных, чтобы заполнить анкету', 'выход'))
        main_m.print_a_topic()
        main_m.print_variants()
        main_a = main_m.get_user_answer()
        db = DataBase.DataBase()
        if main_a == 'новый пациент':
            A = Patient(height=170, weight=70)
            #A = Patient()
            A.input_patient_data()
            A.count_patient_data()
            A.print_patient_data()

            while True:
                second_m = Menu(topic='Клническая ситуация?',
                                variants=('спинальная анестезия', 'острая кровопотеря', 'назад в основное меню'))
                second_m.print_a_topic()
                second_m.print_variants()
                second_a = second_m.get_user_answer()

                if second_a == 'спинальная анестезия':
                    # A.count_risk_factors(answers={})
                    A.count_risk_factors(answers={'fetus': 'n', 'bladder': 'n', 'back_discomfort': 'n'})
                    A.get_bupivacaine_dose(A.count_a_sum(), bupivacaine_dosage)
                    # здесь нужно пересмотреть Menu
                    third_m = Menu(topic="Хотите ли Вы заполнить анкету?", variants=('да', 'нет'))
                    third_m.print_a_topic()
                    third_m.print_variants()
                    third_a = third_m.get_user_answer()
                    quest_flag = True if third_a == 'да' else False
                    db.write_patient_data_to_default_db(A.patient_data_for_spinal, 'new', questionnaire_flag=quest_flag)

                elif second_a == 'острая кровопотеря':
                    A.count_patient_data()
                    A.print_patient_data()
                    pass # сюда можно всписать градацию шока на основе кровопотери, индекс алговера, расчеты по препаратам и всякое

                else:
                    break

        elif 'выбрать пациента из базы данных' in main_a:
            db.write_patient_data_to_default_db(behavior='add')

        elif main_a == 'выход':
            print('See you!')
            break
except KeyboardInterrupt:
    print()
    print('See you')
