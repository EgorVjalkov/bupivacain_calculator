import csv
import os
from data import patient_file_questionnaire
from Menu import Menu


class DataBase:
    def __init__(self, database_path=''):
        if not database_path:
            self.database_path = 'patients/patients.csv'
        with open(self.database_path, 'r+') as database:
            self.db = list(csv.reader(database, delimiter=','))
            if not self.db:
                self.head = []
            else:
                self.head = self.db[0]
                get_patient_id = lambda i: ' '.join(i[:2])
                self.db = {get_patient_id(i): i for i in self.db}
                self.not_finished_patients = {k: self.db[k] for k in self.db if len(self.db[k]) < len(self.head)}
            # недописанные записи надо сделать чтоб дописывал, т.е. снова кидал их в цикл анкеты

    def change_patient_with_missing_data_and_get_index(self):
        if not self.not_finished_patients:
            print('You don`t have patients with missing data')
            return False
        else:
            menu = Menu(question='Change a patient', variants=list(self.not_finished_patients.keys()))
            menu.print_a_question()
            menu.print_variants()
            changed_patient = menu.get_user_answer()
            changed_patient_index = list(self.db.keys()).index(changed_patient)
            return changed_patient_index

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

    def write_patient_data_to_file(self, patient_data, behavior, questionnaire_flag):
        if behavior == 'new':
            head_of_frame = list(patient_data.keys()) + list(patient_file_questionnaire)
            with open(self.database_path, 'a+') as database:
                database_writer = csv.writer(database)

                if not self.head:
                    database_writer.writerow(head_of_frame)
                else:
                    if self.head != head_of_frame:
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
        else:
            pass