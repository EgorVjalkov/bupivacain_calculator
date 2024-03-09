funcs = [
    ('спинальная анестезия', 'count_sma'),
    ('острая кровопотеря', 'count_bleed')
]

general_patient_data = [
    ('рост', 'height'),
    ('вес', 'weight'),
]

accessory_patient_data_for_bleed = [
    ('вес до беременности', 'weight_before')
]

accessory_patient_data_for_sma = [
    ('плод', 'fetus'),
    ('плодный пузырь', 'bladder'),
    ('дискомфорт в положении лежа на спине', 'discomfort')
]

bleed_vars = general_patient_data.copy()
bleed_vars.extend(accessory_patient_data_for_bleed)
sma_vars = general_patient_data.copy()
sma_vars.extend(accessory_patient_data_for_sma)

variants = {
    'funcs': funcs,
    'bleed_categories': bleed_vars,
    'sma_categories': sma_vars,
}

answers = {
    'height': 'роста в см',
    'weight': 'веса в кг',
    'weight_before': 'веса до беременности (текущий вес минус прибавка) в кг'
}


def get_dict_with_variants(key: str) -> dict:
    return {key: variants[key]}


class PatientData:
    def __init__(self, for_func: str):
        self.for_func = for_func
        self.necessary_keys = [i[1] for i in variants[self.for_func]]

    def filled(self, data_from_ctx: dict):
        for i in self.necessary_keys:
            if i not in data_from_ctx:
                return False
        return True


patient_data_for_bleed = PatientData('bleed_categories')


class Category:
    def __init__(self, name):
        self.name = name

    @property
    def answer(self):
        return f'Введите показатель {answers[self.name]}'


def get_dict_with_answer(key: str) -> dict:
    return {key: f'Введите показатель {answers[key]}'}
