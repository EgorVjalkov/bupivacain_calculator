import csv
import os
from data import patient_file_questionnaire
from Menu import Menu


class DataBase:
    def __init__(self, database_path=''):
        if not database_path:
            self.database_path = 'patients/patients.csv'
        with open(self.database_path, 'r+') as database:
            self.database_reader = list(csv.reader(database, delimiter=','))
            if not self.database_reader:
                self.head_of_db = []
            else:
                self.head_of_db = self.database_reader[0]
            self.not_finished_patients = [i for i in self.database_reader if len(i) < len(self.head_of_db)]
            # недописанные записи надо сделать чтоб дописывал, т.е. снова кидал их в цикл анкеты

    def change_patient_with_missing_data(self):
        if not self.not_finished_patients:
            print('You don`t have patients with missing data')
            return False
        else:
            print('Change a patient')
            print(self.not_finished_patients)
            patients = dict(enumerate(self.not_finished_patients, 1))
            print(patients)
            while True:
                try:
                    for_print = {print(f'press {k} for change {" ".join(patients[k][:2])}') for k in patients}
                    changed_patient = patients[int(input(': '))]
                    break
                except KeyError:
                    print('*********input error!*********')
                except ValueError:
                    print('*********input error!*********')
            return changed_patient

    def answer_the_questionnaire(self, questionnaire, patient_with_missing_data=()):
        # добавь логику, чтоб анткета старотовала не сначала, добавь командв чтоб можно было б дописать или переписать
        answers_dict = {}
        try:
            for question in questionnaire:
                variants_of_answer = questionnaire[question]
                menu = Menu(question, variants_of_answer)
                menu.print_a_question()
                if variants_of_answer:
                    menu.print_variants()
                answers_dict[question] = menu.get_user_answer()
        except KeyboardInterrupt:
            return answers_dict
        return answers_dict

    def write_patient_data_to_file(self, patient_data, questionnaire_flag):
        head_of_frame = list(patient_data.keys()) + list(patient_file_questionnaire)
        with open(self.database_path, 'a+') as database:
            database_writer = csv.writer(database)

            if not self.head_of_db:
                database_writer.writerow(head_of_frame)
            else:
                if self.head_of_db != head_of_frame:
                    #print(self.head_of_db == head_of_frame)
                    #print(self.head_of_db)
                    #print(head_of_frame)
                    database_writer.writerow(['*']*len(head_of_frame))
                    database_writer.writerow(head_of_frame)

                if questionnaire_flag:
                    if patient_data['name'] == 'noname':
                        patient_data['name'] = input('Enter a patient`s name\n: ')
                    patient_answers = list(patient_data.values())
                    patient_answers.extend(list(self.answer_the_questionnaire(patient_file_questionnaire).values()))
                else:
                    patient_answers = list(patient_data.values())

                database_writer.writerow(patient_answers)

# сделай новую фенкцию чтоб переписывать данные
#                 if not variants_of_answer:
#                     if type(variants_of_answer) == int:
#                         while True:
#                             try:
#                                 answer = input(f'{question}? Enter a num\n: ')
#                                 answer = answer.replace(',', '.') if ',' in answer else answer
#                                 answers_dict[question] = float(answer)
#                                 break
#                             except ValueError:
#                                 print('*********input error*********')
#                     else:
#                         answers_dict[question] = input(f'{question}?\n: ')
#                 else:
#                     variants_of_answer = dict(enumerate(variants_of_answer, 1))
#                     while True:
#                         try:
#                             print(question)
#                             print_variants = {print(f'press {k} if {variants_of_answer[k]}') for k in variants_of_answer}
#                             answers_dict[question] = variants_of_answer[int(input(': '))]
#                             break
#                         except KeyError:
#                             print('*********input error!*********')
#                         except ValueError:
#                             print('*********input error!*********')
