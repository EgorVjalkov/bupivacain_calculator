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

        self.blood_volume = 0
        self.clinical_bleed = 0
        self.critical_bleed = 0

        self.risk_factors = ('bmi', 'fetus', 'bladder', 'back_discomfort')
        self.factors_count_dict = {}
        self.sum_of_factors = 0
        self.patient_data_for_spinal = \
            {'datetime': self.datetime, 'name': self.patient_name, 'height': self.height, 'weight': self.weight}
        self.patient_data_for_bleeding = self.patient_data_for_spinal.copy()
        self.patient_data_for_print = {'рост': 'height', 'вес': 'weight', 'ИМТ': 'bmi',
                'ОЦК': 'blood_vol', 'потеря 10-15% ОЦК': 'clinical_bleed', 'потеря 25-30% ОЦК': 'critical_bleed'}
# сделай мини фyнкцию чтоб обновлять словари

    def refresh_data_dicts(self, key, value, data_dict='all'):
        if data_dict == 'spinal':
            self.patient_data_for_spinal[key] = value
        elif data_dict == 'bleeding':
            self.patient_data_for_bleeding[key] = value
        elif data_dict == 'all':
            self.patient_data_for_spinal[key] = value
            self.patient_data_for_bleeding[key] = value


    def input_patient_data(self):
        if not self.height:
            menu = Menu(topic='Введите показатель роста в сантиметрах', variants=0)
            menu.print_a_topic()
            self.height = menu.get_user_answer()
            self.refresh_data_dicts('height', self.height)
        if not self.weight:
            menu = Menu(topic='Введите показатель веса в килограммах', variants=0)
            menu.print_a_topic()
            self.weight = menu.get_user_answer()
            self.refresh_data_dicts('weight', self.weight)

        return self.height, self.weight, self.blood_volume, self.clinical_bleed, self.critical_bleed

    def count_patient_data(self):
        if not self.bmi:
            self.bmi = self.get_bmi(self.weight)
            self.refresh_data_dicts('bmi', self.bmi)

        if not self.blood_volume:
            self.blood_volume = self.count_blood_volume()
            if self.blood_volume:
                self.refresh_data_dicts('blood_vol', self.blood_volume, 'bleeding')
                self.clinical_bleed = f"{'-'.join(self.count_bleed_volume((10, 15)))}"
                self.refresh_data_dicts('clinical_bleed', self.clinical_bleed, 'bleeding')
                self.critical_bleed = f"{'-'.join(self.count_bleed_volume((25, 30)))}"
                self.refresh_data_dicts('critical_bleed', self.critical_bleed, 'bleeding')

        return self.bmi, self.blood_volume, self.clinical_bleed, self.critical_bleed

    def print_patient_data(self):
        print()
        for k in self.patient_data_for_print:
            translate_key = self.patient_data_for_print[k]
            if translate_key in self.patient_data_for_bleeding:
                print(f'{k} - {self.patient_data_for_bleeding[translate_key]}')
        print()

    # bmi
    def get_bmi(self, weight):
        self.bmi = round(weight/pow(self.height/100, 2), 1)
        return self.bmi

    # counting sum of factors
    def count_risk_factors(self, answers=()):
        for rf in self.risk_factors:
            rf = RiskFactor(rf, risk_factor_dict)
            if rf.name == 'bmi':
                rf_dict = rf.get_bmi_risk_count(self.bmi)
                print(f'bmi is {self.bmi} ({rf_dict["interpretation"]})')

            else:
                if rf.name in answers and answers[rf.name]:
                    rf_dict = rf.find_risk_factor_with_answer(answers[rf.name])
                else:
                    rf_dict = rf.input_risk_factor_and_get_count()

            print(f'{rf.name} riskfactor is {rf_dict["count"]}', '\n')
            self.factors_count_dict.update({rf.name: rf_dict['count']})
            self.patient_data_for_spinal.update({f'{rf.name}_{k}': rf_dict[k] for k in rf_dict if k in ['interpretation', 'count']})

        return self.risk_factors

    def count_a_sum(self):
        back_discomfort_count = self.factors_count_dict.pop('back_discomfort')
        self.sum_of_factors = sum(list(self.factors_count_dict.values()))
        # присмотрись протестируй
        if self.sum_of_factors <= 0 and back_discomfort_count:
            self.sum_of_factors += back_discomfort_count
        elif self.sum_of_factors > 0 and back_discomfort_count:
            self.patient_data_for_spinal['back_discomfort_count'] = 'not using'
            print('back_discomfort riskfactor is not used')

        self.patient_data_for_spinal['sum'] = self.sum_of_factors
        self.patient_data_for_spinal['limiting sum'] = False

        if self.sum_of_factors >= 4:
            self.sum_of_factors = 4
            self.patient_data_for_spinal['limiting sum'] = 4

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
        self.patient_data_for_spinal['counted dose'] = counted_dose
        print(f'0,5% spinal heavy bupivacaine dose is {counted_dose}ml\n')

        return counted_dose

    def count_blood_volume(self):
        m = Menu(topic='Что использовать для подсчета ОЦК?', variants=data.blood_vol_menu.keys())
        m.print_a_topic()
        m.print_variants()
        answer = m.get_user_answer()
        if 'нет необходимости' in answer:
            return 0
        m2 = Menu(topic=f'Введите {answer} в кг', variants=0)
        m2.print_a_topic()
        answer2 = m2.get_user_answer()
        weight_before_pregnancy = eval(data.blood_vol_menu[answer])
        bmi = self.get_bmi(weight_before_pregnancy)
        blood_vol_coef = RiskFactor('bmi', data.risk_factor_dict).get_bmi_risk_count(bmi, 'blood vol')
        self.blood_volume = blood_vol_coef * weight_before_pregnancy
        return self.blood_volume

    def count_bleed_volume(self, percents=()):
        get_bleed_vol = lambda i: (i/100) * self.blood_volume
        vol_list = [str(get_bleed_vol(percent)) for percent in percents]
        return vol_list

# pat = Patient(height=0, weight=0)
# pat.input_patient_data()
# pat.count_patient_data()
# pat.print_patient_data()

#print(pat.count_blood_volume())
