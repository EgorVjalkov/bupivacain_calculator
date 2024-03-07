from aiogram_dialog import DialogManager


async def get_funcs(dialog_manager: DialogManager,
                    **middlewere_data) -> dict:
    data = {
        'funcs': [
            ('расчет дозы м/а для спинальной анестезии', 'count_sma'),
            ('расчет ОЦК и предпологаемого объема кровопотери', 'count_bleed')
        ]
    }
    return data


async def get_general_patient_categories(dialog_manager: DialogManager,
                                         **middlewere_data) -> dict:
    data = {
        'patient_general_categories': [
            ('name', 'pat_n'),
            ('heigth', 'pat_h'),
            ('weight', 'pat_w'),
        ]
    }
    return data
