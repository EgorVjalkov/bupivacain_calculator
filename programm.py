class FindCount:

    def __init__(self, dict_, description):
        for k in dict_:
            interpretation = dict_[k]['inter']
            print(f'press "{k}" if {description} {interpretation}')
        while True:
            self.answer = input()
            if self.answer in dict_:
                break
        self.count = dict_[self.answer]['count']


class Patient:

    def __init__(self):
        self.risk_factors_list = []
        self.patient_name = input('pregnant`s name?\n')
        self.height = int(input('pregnant`s height?\n'))
        self.weight = int(input('pregnant`s weight?\n'))

    # bmi
    def get_bmi(self):
        return round(self.weight/pow(self.height/100, 2), 1)

    def get_bmi_risk_count(self, bmi):
        bmi_interpretation_dict = {
            18.5: {'inter': 'deficit', 'count': -1},
            25.0: {'inter': 'normal', 'count': -1},
            30.0: {'inter': 'overage', 'count': 0},
            35.0: {'inter': 'obesity 1', 'count': 1},
            40.0: {'inter': 'obesity 2', 'count': 2},
            100.0: {'inter': 'obesity 3', 'count': 3}
        }
        for k in bmi_interpretation_dict:
            if bmi < k:
                bmi_count = bmi_interpretation_dict[k]['count']
                bmi_interpretation = bmi_interpretation_dict[k]['inter']
                return {'inter': bmi_interpretation, 'count': bmi_count}

        # fetus
        fetus_weight_dict = {
            'b': {'inter': 'big (fetus weight > 4kg)', 'count': 1},
            'n': {'inter': 'normal (fetus weight > 2.5kg and < 4kg)', 'count': 0},
            's': {'inter': 'small (fetus weight < 2.5kg)', 'count': -1}
        }
        fetus = FindCount(fetus_weight_dict, 'fetus is')
        self.fetus = fetus.answer
        self.fetus_count = fetus.count
        self.risk_factors_list.append(self.fetus_count)

        # fetal bladder
        bladder_condition = {
            'r': {'inter': 'raptured or oligohydramnios', 'count': 0},
            'n': {'inter': 'intact, no polyhydramnios', 'count': 0},
            'p': {'inter': 'intact, polyhydramnios', 'count': 1},
        }
        bladder = FindCount(bladder_condition, 'bladder is')
        self.bladder = bladder.answer
        self.bladder_count = bladder.count
        self.risk_factors_list.append(self.bladder_count)

        # discomfort in position on the back
        back_discomfort_dict = {
            'y': {'inter': 'discomfort in the position on the back', 'count': 1},
            'n': {'inter': 'NOT discomfort in the position on the back', 'count': 0}
        }
        back = FindCount(back_discomfort_dict, 'pregnant has')
        self.back_discomfort = back.answer
        self.back_discomfort_count = back.count
        if sum(self.risk_factors_list) < 0:
            self.risk_factors_list.append(self.back_discomfort_count)

        print(self.bmi, self.bmi_count, self.bmi_interpretation)
        print(self.fetus, self.fetus_count)
        print(self.bladder, self.bladder_count)
        print(self.back_discomfort, self.back_discomfort_count)
        print(self.risk_factors_list)

    # counting sum of factors
    def count_risk_factors(self):
        sum_factors = sum(self.risk_factors_list) if sum(self.risk_factors_list) < 4 else 4
        return sum_factors

    def get_bupivacaine_dose(self, sum_of_risk):
        bupivacaine_dosage = {
            145: [1.5, 1.4, 1.4, 1.3, 1.2, 1.1, 1.0],
            150: [1.9, 1.8, 1.7, 1.5, 1.4, 1.4, 1.3],
            155: [2.1, 2.0, 1.8, 1.7, 1.6, 1.5, 1.4],
            160: [2.3, 2.2, 2.0, 1.9, 1.8, 1.6, 1.5],
            165: [2.4, 2.3, 2.2, 2.0, 1.9, 1.7, 1.6],
            170: [2.6, 2.4, 2.3, 2.1, 2.0, 1.8, 1.6],
            175: [2.8, 2.6, 2.4, 2.3, 2.1, 1.9, 1.8],
            180: [2.9, 2.8, 2.5, 2.4, 2.2, 2.0, 1.9]
        }
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

    def get_bupivacaine_fastly(self, code):
        code_list = code.split()
        code_keys = [self.height, self.weight, self.fetus, self.bladder, self.back_discomfort]

# code = 123.45.f.b.d

new_patient = Patient()
risk_factors = new_patient.count_risk_factors()
print(new_patient.count_risk_factors(), new_patient.get_bupivacaine_dose(risk_factors))
