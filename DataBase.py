import csv
import os
from data import patient_file_questionnaire


class DataBase:
    def __init__(self, database_path=''):
        if not database_path:
            self.database_path = 'patients/patients.csv'
        self.fool_flag = True if not os.stat(self.database_path).st_size else False
        with open(self.database_path, 'r+') as database:
            self.database_reader = list(csv.reader(database, delimiter=','))
            self.head_of_db = self.database_reader[0]
            self.not_finished_patients = [i for i in self.database_reader if len(i) < len(self.head_of_db)]
            # недописанные записи надо сделать чтоб дописывал, т.е. снова кидал их в цикл анкеты

    def answer_the_questionnaire(self, questionnaire):
        answers_dict = {}
        try:
            for question in questionnaire:
                variants_of_answer = questionnaire[question]
                if not variants_of_answer:
                    if type(variants_of_answer) == int:
                        while True:
                            try:
                                answer = input(f'{question}? Enter a num\n: ')
                                answer = answer.replace(',', '.') if ',' in answer else answer
                                answers_dict[question] = float(answer)
                                break
                            except ValueError:
                                print('*********input error*********')
                    else:
                        answers_dict[question] = input(f'{question}?\n: ')
                else:
                    variants_of_answer = dict(enumerate(variants_of_answer, 1))
                    while True:
                        try:
                            print(question)
                            print_variants = {print(f'press {k} if {variants_of_answer[k]}') for k in variants_of_answer}
                            answers_dict[question] = variants_of_answer[int(input(': '))]
                            break
                        except KeyError:
                            print('*********input error!*********')
                        except ValueError:
                            print('*********input error!*********')
        except KeyboardInterrupt:
            return answers_dict
        return answers_dict

    def write_patient_data_to_file(self, patient_data, questionnaire_flag):
        head_of_frame = list(patient_data.keys()) + list(patient_file_questionnaire)
        with open(self.database_path, 'a+') as database:
            database_writer = csv.writer(database)

            if self.fool_flag:
                database_writer.writerow(head_of_frame)
            else:
                if self.head_of_db != head_of_frame:
                    #print(self.head_of_db == head_of_frame)
                    #print(self.head_of_db)
                    #print(head_of_frame)
                    database_writer.writerow(['*']*len(head_of_frame))
                    database_writer.writerow(head_of_frame)

                if questionnaire_flag:
                    if not patient_data['name']:
                        patient_data['name'] = input('Enter a patient`s name\n: ')
                    patient_answers = list(patient_data.values())
                    patient_answers.extend(list(self.answer_the_questionnaire(patient_file_questionnaire).values()))
                else:
                    patient_answers = list(patient_data.values())

                database_writer.writerow(patient_answers)
