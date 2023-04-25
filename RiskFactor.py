from Menu import Menu
class RiskFactor:
    def __init__(self, name, data):
        self.name = name
        self.risk_factor_dict = data['risk_factor_dict']
        if 'description' in data:
            self.description = data['description']

        self.risk_factor_data = {'name': self.name}

    def get_bmi_risk_count(self, bmi):
        for k in self.risk_factor_dict:
            if bmi < k:
                self.risk_factor_data['interpretation'] = self.risk_factor_dict[k]['inter']
                self.risk_factor_data['count'] = self.risk_factor_dict[k]['count']
                return self.risk_factor_data

    def find_risk_factor_with_answer(self, answer):
        self.risk_factor_data['interpretation'] = self.risk_factor_dict[answer]['inter']
        self.risk_factor_data['count'] = self.risk_factor_dict[answer]['count']
        return self.risk_factor_data

    def input_risk_factor_and_get_count(self):
        interpretaiton_list = {k: self.risk_factor_dict[k]['inter'] for k in self.risk_factor_dict}
        menu = Menu(variants=interpretaiton_list, description=self.description)
        menu.print_variants()
        answer = menu.get_user_answer()
        self.risk_factor_data['interpretation'] = answer
        self.risk_factor_data['count'] = {k: self.risk_factor_dict[k] for k in self.risk_factor_dict if answer in self.risk_factor_dict[k]}['count']
        return self.risk_factor_data
