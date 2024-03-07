from aiogram.filters.state import State, StatesGroup


class PatientDataInput(StatesGroup):
    input_general_patient_data = State()
    input_name = State()
    input_height = State()
    input_weight = State()
    func_menu = State()
    input_acc_patient_data_for_bleed = State()
    input_acc_patient_data_for_sma = State()

    input_puncture_position = State()
