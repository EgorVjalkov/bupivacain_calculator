
class RiskFactor:
    def __init__(self, name, risk_factor_dict, description):
        self.risk_factor_dict = risk_factor_dict
        self.description = description

        self.risk_factor_data = {'name': name}

    def get_bmi_risk_count(self, bmi):
        for k in self.risk_factor_dict:
            if bmi < k:
                self.risk_factor_data['interpretation'] = self.risk_factor_dict[k]['inter']
                self.risk_factor_data['count'] = self.risk_factor_dict[k]['count']
                return self.risk_factor_data

    def input_risk_factor_and_get_count(self):
        for k in self.risk_factor_dict:
            interpretation = self.risk_factor_dict[k]['inter']
            print(f'press "{k}" if {self.description} {interpretation}')
        while True:
            answer = input()
            if answer in self.risk_factor_dict:
                self.risk_factor_data['interpretation'] = self.risk_factor_dict[answer]['inter']
                self.risk_factor_data['count'] = self.risk_factor_dict[answer]['count']
                break
        return self.risk_factor_data


class Patient:

    def __init__(self):
        self.patient_name = input('pregnant`s name?\n')
        self.height = int(input('pregnant`s height?\n'))
        self.weight = int(input('pregnant`s weight?\n'))
        self.bmi = 0.0

        self.risk_factors_dict = {'bmi': {}, 'fetus': {}, 'bladder': {}, 'back_discomfort': {}}
        self.sum_of_factors = 0

    # bmi
    def get_bmi(self):
        self.bmi = round(self.weight/pow(self.height/100, 2), 1)
        return self.bmi

    # counting sum of factors
    def count_risk_factors(self):
        for rf in self.risk_factors_dict:
            rf = RiskFactor(rf,)
            if rf.name == 'bmi':
                pass # остановился здесь. итерирую словарь класса пациент. надо сделать подвязку из файла data

        sum_factors = sum(self.risk_factors_list) if sum(self.risk_factors_list) < 4 else 4
        return sum_factors

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

    #def get_bupivacaine_fastly(self, code):
        code_list = code.split()
        code_keys = [self.height, self.weight, self.fetus, self.bladder, self.back_discomfort]

