import csv
from data import patient_file_questionnaire
from Menu import Menu

# здесь нужно придумать с базой данный. чтоб при проблемах с фреймом пилил новую и все!
class DataBase:
    def __init__(self, database_path=''):
        if not database_path:
            self.database_path = 'patients/patients.csv'
        with open(self.database_path, 'r') as database:
            self.db = list(csv.reader(database, delimiter=','))
            if not self.db:
                self.head = []
                self.patients_with_missing_data = {}
            else:
                self.head = self.db[0]
                #print(self.head)
                get_patient_id = lambda i: ' '.join(i[:2])
                self.db = {get_patient_id(i): i for i in self.db}

    def get_patients_with_missing_data(self):
        patients_with_missing_data = {k: self.db[k] for k in self.db if len(self.db[k]) < len(self.head)}
        return patients_with_missing_data

    def change_patient_with_missing_data_and_get_index(self, patients_with_missing_data):
        if not patients_with_missing_data:
            return False
        else:
            menu = Menu(question='Change a patient', variants=list(patients_with_missing_data.keys()))
            menu.print_a_question()
            menu.print_variants()
            changed_patient_id = menu.get_user_answer()
            return changed_patient_id

    def answer_the_questionnaire(self, questionnaire):
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
            print()
            return answers_dict
        return answers_dict

    def write_patient_data_to_file(self, patient_data={}, behavior='new', questionnaire_flag=False):
        if behavior == 'new':
            head_of_frame = list(patient_data.keys()) + list(patient_file_questionnaire)
            with open(self.database_path, 'a') as database:
                database_writer = csv.writer(database)

                if not self.head:
                    database_writer.writerow(head_of_frame)
                else:
                    if self.head != head_of_frame:
                        print('head of frame is not matched with patient data')
                        #database_writer.writerow(['*']*len(head_of_frame))
                        database_writer.writerow(head_of_frame)
                if questionnaire_flag:
                    if patient_data['name'] == 'noname':
                        patient_data['name'] = input('Enter patient`s name\n: ')
                    patient_answers = list(patient_data.values())
                    patient_answers.extend(list(self.answer_the_questionnaire(patient_file_questionnaire).values()))
                else:
                    patient_answers = list(patient_data.values())

                database_writer.writerow(patient_answers)

        elif behavior == 'add':
            patient_id = self.change_patient_with_missing_data_and_get_index(self.get_patients_with_missing_data())
            if not patient_id:
                print('You don`t have patients with missing data\n')
                return
            patient_answers = self.db[patient_id]
            missing_questions = self.head[len(patient_answers):]
            missing_questions = {k: patient_file_questionnaire[k] for k in missing_questions}
            patient_answers = [input('Enter patient`s name\n: ') if i == 'noname' else i for i in patient_answers]
            patient_answers.extend(list(self.answer_the_questionnaire(missing_questions).values()))
            def replacer(patient_id, row, new_row):
                row_id = ' '.join(row[:2])
                if row_id == patient_id:
                    row = new_row
                return row

            with open(self.database_path, 'r') as database:
                db_reader = csv.reader(database)
                db_reader = [replacer(patient_id, row, patient_answers) for row in db_reader]
            with open(self.database_path, 'w') as database:
                database_writer = csv.writer(database)
                database_writer.writerows(db_reader)

    def refactor(self):
        self.head = self.db['datetime name']
        self.write_patient_data_to_file(behavior='add')
        # здесь сложно. нужно отработать через дикт райтер как таблицу
