risk_factor_dict = {
    'bmi': {
        'risk_factor_dict': {
            18.5: {'inter': 'deficit', 'count': -1},
            25.0: {'inter': 'normal', 'count': -1},
            30.0: {'inter': 'overage', 'count': 0},
            35.0: {'inter': 'obesity 1', 'count': 1},
            40.0: {'inter': 'obesity 2', 'count': 2},
            100.0: {'inter': 'obesity 3', 'count': 3}}},

    'fetus': {
        'risk_factor_dict': {
            'b': {'inter': 'big (fetus weight > 4kg)', 'count': 1},
            'n': {'inter': 'normal (fetus weight > 2.5kg and < 4kg)', 'count': 0},
            's': {'inter': 'small (fetus weight < 2.5kg)', 'count': -1}},
        'description': 'fetus is'},

    'bladder': {
        'risk_factor_dict': {
            'r': {'inter': 'raptured or oligohydramnios', 'count': -1},
            'n': {'inter': 'intact, no polyhydramnios', 'count': 0},
            'p': {'inter': 'intact, polyhydramnios', 'count': 1}},
        'description': 'bladder is'},

    'back_discomfort': {
        'risk_factor_dict': {
            'y': {'inter': 'discomfort in the position on the back', 'count': 1},
            'n': {'inter': 'NOT discomfort in the position on the back', 'count': 0}},
        'description': 'pregnant has'}
}

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

block_level_list = ['>=T4'] + list('T' + str(i) for i in range(5, 9)) + ['<=T10']
patient_file_questionnaire = {
    'position for puncture': ('lying', 'sitting'),
    'dose of 0.5% heavy bupivacaine, ml': 0,
    'dose of 0.005% fentanyl, if using, ml': 0,
    'sensory block level in 5 min': block_level_list,
    'events for raising/lowering block level': ('raising head of operating table', 'lowering head of operating table', 'no need'),
    'dose of 0.005% fenylefrine BEFORE delivering, ml': 0,
    'sensory block level AFTER delivering': block_level_list,
    'dose of 0.005% fenylefrine AFTER delivering, ml': 0,
    'estimation': (1, 2, 3, 4, 5),
    'remark': ''
}






