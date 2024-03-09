from Menu import Menu


class RiskFactor:
    def __init__(self, name, data):
        self.name = name
        self.risk_factor_dict = data[name]['risk_factor_dict']
        if 'description' in data[name]:
            self.description = data[name]['description']

        self.risk_factor_data = {'name': self.name}

    def get_bmi_risk_count(self,
                           bmi: float,
                           behavior: str = '') -> dict:

        for k in self.risk_factor_dict:
            if bmi < k:
                if behavior == 'blood vol':
                    return self.risk_factor_dict[k]['blood_vol_coef']
                self.risk_factor_data['interpretation'] = self.risk_factor_dict[k]['inter']
                self.risk_factor_data['count'] = self.risk_factor_dict[k]['count']
                return self.risk_factor_data

    def find_risk_factor_with_answer(self,
                                     answer: str) -> dict:

        self.risk_factor_data['interpretation'] = self.risk_factor_dict[answer]['inter']
        self.risk_factor_data['count'] = self.risk_factor_dict[answer]['count']
        return self.risk_factor_data

    def input_risk_factor_and_get_count(self):
        interpretation_list = {k: self.risk_factor_dict[k]['inter']
                               for k in self.risk_factor_dict}
        menu = Menu(variants=interpretation_list, description=self.description)
        menu.print_variants()
        answer = menu.get_user_answer()
        self.risk_factor_data['interpretation'] = answer
        for k in self.risk_factor_dict:
            if answer in self.risk_factor_dict[k].values():
                self.risk_factor_data['count'] = self.risk_factor_dict[k]['count']
        return self.risk_factor_data


#a = RiskFactor('fetus', data.risk_factor_dict)
#a.input_risk_factor_and_get_count()