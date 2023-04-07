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

        self.risk_factors_dict = {'bmi': {}, 'fetus': {}, 'bladder': {}, 'back_discomfort': {}}
        self.factors_count_dict = {}
        self.sum_of_factors = 0

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
        for rf in self.risk_factors_dict:
            rf = RiskFactor(rf, risk_factor_dict[rf])
            if rf.name == 'bmi':
                self.get_bmi()
                rf_dict = rf.get_bmi_risk_count(self.bmi)
            else:
                if rf.name in answers:
                    rf_dict = rf.find_risk_factor_with_answer(answers[rf.name])
                else:
                    rf_dict = rf.input_risk_factor_and_get_count()

            print(f'{rf.name} riskfactor is {rf_dict["count"]}', '\n')
            self.factors_count_dict.update({rf.name: rf_dict['count']})
            self.risk_factors_dict[rf.name].update(rf_dict)

        return self.risk_factors_dict

    def count_a_sum(self):
        self.sum_of_factors = sum(list(self.factors_count_dict.values()))
        if self.sum_of_factors > 0 and self.factors_count_dict['back_discomfort']:
            self.sum_of_factors -= 1
            self.factors_count_dict['back_discomfort'] = 'not using'
            print('back_discomfort riskfactor is not used')

        if self.sum_of_factors >= 4:
            self.sum_of_factors = 4

        print(f'sum of riskfactors is {self.sum_of_factors}')
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

        return bupivacaine_dosage[rounded_height][sum_of_risk+2]

    def write_patient_data_to_file(self):
        file_path = 'patients/patients.csv'
        if not os.stat(file_path).st_size:
            with open(file_path, 'a+') as f:
                writer = csv.writer(f)
                writer.writerow(['fool']) # сделай шапку цсв если файл пуст


    #def get_bupivacaine_fastly(self, code):
        # code_list = code.split()
        # code_keys = [self.height, self.weight, self.fetus, self.bladder, self.back_discomfort]

