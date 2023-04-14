import data
from data import risk_factor_dict
from RiskFactor import RiskFactor
import csv
import os


class Patient:

    def __init__(self, patient_name='', height=0, weight=0):
        self.patient_name = patient_name
        self.height = height
        self.weight = weight
        self.bmi = 0.0

        self.risk_factors = ('bmi', 'fetus', 'bladder', 'back_discomfort')
        self.factors_count_dict = {}
        self.sum_of_factors = 0
        self.patient_data = {'name': self.patient_name, 'height': self.height, 'weight': self.weight}

    def input_patient_data(self):
        if not self.height:
            self.height = int(input('pregnant`s height?\n'))
        if not self.weight:
            self.weight = int(input('pregnant`s weight?\n'))
        return self.height, self.weight

    # bmi
    def get_bmi(self):
        self.bmi = round(self.weight/pow(self.height/100, 2), 1)
        return self.bmi

    # counting sum of factors
    def count_risk_factors(self, answers=()):
        for rf in self.risk_factors:
            rf = RiskFactor(rf, risk_factor_dict[rf])
            if rf.name == 'bmi':
                self.get_bmi()
                self.patient_data['bmi'] = self.bmi
                rf_dict = rf.get_bmi_risk_count(self.bmi)

            else:
                if rf.name in answers:
                    rf_dict = rf.find_risk_factor_with_answer(answers[rf.name])
                else:
                    rf_dict = rf.input_risk_factor_and_get_count()

            print(f'{rf.name} riskfactor is {rf_dict["count"]}', '\n')
            self.factors_count_dict.update({rf.name: rf_dict['count']})
            self.patient_data.update({f'{rf.name}_{k}': rf_dict[k] for k in rf_dict if k in ['interpretation', 'count']})

        return self.risk_factors

    def count_a_sum(self):
        self.sum_of_factors = sum(list(self.factors_count_dict.values()))
        if self.sum_of_factors > 0 and self.factors_count_dict['back_discomfort']:
            self.sum_of_factors -= 1
            self.patient_data['back_discomfort_count'] = 'not using'
            self.patient_data['sum'] = self.sum_of_factors
            self.patient_data['limiting sum'] = False
            print('back_discomfort riskfactor is not used')

        if self.sum_of_factors >= 4:
            self.sum_of_factors = 4
            self.patient_data['limiting sum'] = 4

        print(f'sum of riskfactors is {self.sum_of_factors}', '\n')
        return self.sum_of_factors

    def get_bupivacaine_dose(self, sum_of_risk, bupivacaine_dosage):
        if self.height not in bupivacaine_dosage.keys():
            if self.height < 145:
                rounded_height = 145
            elif self.height > 180:
                rounded_height = 180
            else:
                rounded_height = self.height
                while rounded_height % 5 > 0:
                    rounded_height += 1
        else:
            rounded_height = self.height

        counted_dose = bupivacaine_dosage[rounded_height][sum_of_risk+2]
        self.patient_data['counted dose'] = counted_dose

        return counted_dose

    def write_patient_data_to_file(self):
        file_path = 'patients/patients.csv'
        head_of_frame = list(self.patient_data.keys()) + list(data.patient_file_questionnaire)
        with open(file_path, 'a+') as f:
            writer = csv.writer(f)
            if not os.stat(file_path).st_size:
                writer.writerow(head_of_frame)
            else:
                # здесь опросник будет!!!
                writer.writerow()




    #def get_bupivacaine_fastly(self, code):
        # code_list = code.split()
        # code_keys = [self.height, self.weight, self.fetus, self.bladder, self.back_discomfort]

