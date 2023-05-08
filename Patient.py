import data
from data import risk_factor_dict
from RiskFactor import RiskFactor
from datetime import datetime
from Menu import Menu


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
        self.blood_volume = 0

    def input_patient_data(self):
        if not self.height:
            menu = Menu(question='patient`s height', variants=0)
            menu.print_a_question()
            self.height = menu.get_user_answer()
            self.patient_data['height'] = self.height
        if not self.weight:
            menu = Menu(question='patient`s weight', variants=0)
            menu.print_a_question()
            self.weight = menu.get_user_answer()
            self.patient_data['weight'] = self.weight
        self.blood_volume = self.count_blood_volume()
        if self.blood_volume:
            blood_volume_15 = self.get_clinical_bleed_volume()
            print(f'patient`s blood volume is {self.blood_volume}')
            print(f'clinical bleed volume is {blood_volume_15}')
            print(f'critical bleed volume is {blood_volume_15 * 2}\n')

        return self.height, self.weight, self.blood_volume

    # bmi
    def get_bmi(self, weight):
        self.bmi = round(weight/pow(self.height/100, 2), 1)
        return self.bmi

    # counting sum of factors
    def count_risk_factors(self, answers=()):
        for rf in self.risk_factors:
            rf = RiskFactor(rf, risk_factor_dict)
            if rf.name == 'bmi':
                self.get_bmi(self.weight)
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

    def count_blood_volume(self):
        m = Menu(question='What parameter use for counting blood volume?', variants=data.blood_vol_menu.keys())
        m.print_a_question()
        m.print_variants()
        answer = m.get_user_answer()
        if answer == 'pass':
            return 0
        m2 = Menu(question=answer, variants=0)
        answer2 = m2.get_user_answer()
        weight_before_pregnancy = eval(data.blood_vol_menu[answer])
        bmi = self.get_bmi(weight_before_pregnancy)
        blood_vol_coef = RiskFactor('bmi', data.risk_factor_dict).get_bmi_risk_count(bmi, 'blood vol')
        self.blood_volume = blood_vol_coef * weight_before_pregnancy
        return self.blood_volume

    def get_clinical_bleed_volume(self):
        blood_volume_15 = 0.15 * self.blood_volume
        return blood_volume_15

pat = Patient(height=150, weight=78)
#print(pat.count_blood_volume())
