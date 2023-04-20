from data import risk_factor_dict
from RiskFactor import RiskFactor
from datetime import datetime


class Patient:

    def __init__(self, patient_name='noname', height=0, weight=0):
        dt = datetime.today()
        self.datetime = dt.strftime('%d.%m.%Y %H:%M')
        self.patient_name = patient_name
        self.height = height
        self.weight = weight
        self.bmi = 0.0

        self.risk_factors = ('bmi', 'fetus', 'bladder', 'back_discomfort')
        self.factors_count_dict = {}
        self.sum_of_factors = 0
        self.patient_data = {'datetime': self.datetime, 'name': self.patient_name, 'height': self.height, 'weight': self.weight}

    def input_patient_data(self):
        if not self.height:# сделвй инпуты через меню
            self.height = int(input('pregnant`s height?\n'))
            self.patient_data['height'] = self.height
        if not self.weight:
            self.weight = int(input('pregnant`s weight?\n'))
            self.patient_data['weight'] = self.weight
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
                print(f'bmi is {self.bmi} ({rf_dict["interpretation"]})')

            else:
                if rf.name in answers and answers[rf.name]:
                    rf_dict = rf.find_risk_factor_with_answer(answers[rf.name])
                else:
                    rf_dict = rf.input_risk_factor_and_get_count()

            print(f'{rf.name} riskfactor is {rf_dict["count"]}', '\n')
            self.factors_count_dict.update({rf.name: rf_dict['count']})
            self.patient_data.update({f'{rf.name}_{k}': rf_dict[k] for k in rf_dict if k in ['interpretation', 'count']})

        return self.risk_factors

    def count_a_sum(self):
        back_discomfort_count = self.factors_count_dict.pop('back_discomfort')
        self.sum_of_factors = sum(list(self.factors_count_dict.values()))
        # присмотрись протестируй
        if self.sum_of_factors <= 0 and back_discomfort_count:
            self.sum_of_factors += back_discomfort_count
        elif self.sum_of_factors > 0 and back_discomfort_count:
            self.patient_data['back_discomfort_count'] = 'not using'
            print('back_discomfort riskfactor is not used')

        self.patient_data['sum'] = self.sum_of_factors
        self.patient_data['limiting sum'] = False

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
        print(f'0,5% spinal heavy bupivacaine dose is {counted_dose}ml\n')

        return counted_dose


    # def get_bupivacaine_fastly(self, code):
        # code_list = code.split()
        # code_keys = [self.height, self.weight, self.fetus, self.bladder, self.back_discomfort]

