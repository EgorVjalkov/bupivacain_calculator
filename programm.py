class ChoosingVariantFromDict:

    def __init__(self, dict_, description):
        for k in dict_:
            interpretation = dict_[k]['inter']
            print(f'press "{k}" if {description} {interpretation}')
        while True:
            self.answer = input()
            if self.answer in dict_:
                break
        self.count = dict_[self.answer]['count']
        self.mark = dict_[self.answer]['mark']


class InputChecking:
    def __init__(self, parameter, checking):
        while True:
            if checking == 'num':
                if parameter.isnumeric():
                    break
            if checking == 'str':
                if parameter.isalpha():
                    break
            else:
                print('incorrect input')
                parameter = input('repeat input\n:')
        self.is_correct = parameter

class Patient:

    def __init__(self):
        self.name = 'new patient'
        self.height = 0
        self.weight = 0
        self.bmi = {}
        self.fetus = {}
        self.bladder = {}
        self.back_discomfort = {}
        self.risk_factors_list = []
        self.sum_of_risk = 0
        self.bupivacaine_dose = 0

    def input_patient(self):
        name = input('pregnant`s name?\n')
        if name:
            self.name = name
        height = InputChecking(input('pregnant`s height?\n'), 'num')
        self.height = int(height.is_correct)
        weight = InputChecking(input('pregnant`s weight?\n'), 'num')
        self.weight = int(weight.is_correct)
        return self.name, self.height, self.weight

    def input_patient_like_code(self):
        code = input("Input a code. Code example: hhh.www.f.b.bd, where:"
                     "\nh - pregnant`s height,"
                     "\nw - pregnant`s weight,"
                     "\nf - fetus mark,"
                     "\nb - fetal bladder mark,"
                     "\nbd - back discomfort mark")

    def get_bmi(self):
        self.bmi['mark'] = round(self.weight/pow(self.height/100, 2), 1)
        return self.bmi

    def get_bmi_count(self):
        bmi_interpretation_dict = {
            18.5: {'inter': 'deficit', 'count': -1},
            25.0: {'inter': 'normal', 'count': -1},
            30.0: {'inter': 'overage', 'count': 0},
            35.0: {'inter': 'obesity 1', 'count': 1},
            40.0: {'inter': 'obesity 2', 'count': 2},
            100.0: {'inter': 'obesity 3', 'count': 3}
        }
        for k in bmi_interpretation_dict:
            if self.bmi['mark'] < k:
                self.bmi['inter'] = bmi_interpretation_dict[k]['inter']
                self.bmi['count'] = bmi_interpretation_dict[k]['count']
                return self.bmi

        # fetus
    def get_fetus_count(self):
        fetus_weight_dict = {
            'b': {'inter': 'big (fetus weight > 4kg)', 'mark': 'big', 'count': 1},
            'n': {'inter': 'normal (fetus weight > 2.5kg and < 4kg)', 'mark': 'normal', 'count': 0},
            's': {'inter': 'small (fetus weight < 2.5kg)', 'mark': 'small', 'count': -1}
        }
        fetus = ChoosingVariantFromDict(fetus_weight_dict, 'fetus is')
        self.fetus = {'mark': fetus.mark, 'count': fetus.count}
        return self.fetus

    def get_bladder_count(self):
        bladder_condition = {
            'r': {'inter': 'raptured or oligohydramnios', 'mark': 'oligo', 'count': 0},
            'n': {'inter': 'intact, no polyhydramnios', 'mark': 'normal', 'count': 0},
            'p': {'inter': 'intact, polyhydramnios', 'mark': 'poly', 'count': 1},
        }
        bladder = ChoosingVariantFromDict(bladder_condition, 'bladder is')
        self.bladder = {'mark': bladder.mark, 'count': bladder.count}

    def get_back_discomfort_count(self):
        back_discomfort_dict = {
            'y': {'inter': 'discomfort in the position on the back', 'mark': 'discomfort', 'count': 1},
            'n': {'inter': 'NOT discomfort in the position on the back', 'mark': 'NO discomfort', 'count': 0}
        }
        back = ChoosingVariantFromDict(back_discomfort_dict, 'pregnant has')
        self.back_discomfort = {'mark': back.mark, 'count': back.count}

    def count_a_sum_of_risk(self):
        self.get_bmi()
        self.get_bmi_count()
        self.risk_factors_list.append(self.bmi['count'])
        self.get_fetus_count()
        self.risk_factors_list.append(self.fetus['count'])
        self.get_bladder_count()
        self.risk_factors_list.append(self.bladder['count'])
        self.get_back_discomfort_count()

        if sum(self.risk_factors_list) <= 0:
            self.risk_factors_list.append(self.back_discomfort['count'])
        else:
            self.back_discomfort['count'] = 'not using'

        if sum(self.risk_factors_list) > 4:
            self.sum_of_risk = 4
        else:
            self.sum_of_risk = sum(self.risk_factors_list)

        print(self.name)
        print(self.bmi)
        print(self.fetus)
        print(self.bladder)
        print(self.back_discomfort)
        print(self.risk_factors_list)

        return self.sum_of_risk

    def get_bupivacaine_dose(self):
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
        self.bupivacaine_dose = bupivacaine_dosage[rounded_height][self.sum_of_risk+2]

        return self.bupivacaine_dose
#
#     def get_bupivacaine_fastly(self, code):
#         code_list = code.split()
#         code_keys = [self.height, self.weight, self.fetus, self.bladder, self.back_discomfort]
#
# code = 123.45.f.b.d

# new_patient = Patient()
# risk_factors = new_patient.count_risk_factors()
# print(new_patient.count_risk_factors(), new_patient.get_bupivacaine_dose(risk_factors))
