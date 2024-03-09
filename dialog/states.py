from aiogram.filters.state import State, StatesGroup


class PatientDataInput(StatesGroup):
    func_menu = State()
    input_patient_data_for_bleed = State()
    input_patient_data_for_sma = State()
    input_data = State()

    input_name = State()
    input_height = State()
    input_weight = State()

    input_puncture_position = State()
