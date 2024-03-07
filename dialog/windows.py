from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button, Start, Cancel, Back

from dialog.states import PatientDataInput
from dialog import kbs
from dialog import selected
from dialog import getters


def greet_window() -> Window:
    return Window(
        Const('Привет, это бот для расчетов в акушерской анестезиологии, '
              'таких как предполагаемый объём кровототери или доза анестетика для СМА. Введите данные пациента'),
        kbs.column_kb(selected.input_patient_data),
        Cancel(Const('Выход')),
        state=PatientDataInput.func_menu,
        getter=getters.get_general_patient_categories,
    )


def input_name_window() -> Window:
    return Window(
            Const('Введите имя пациентки'),
            Button(on_click=selected.input_name),
            Back(Const('назад')),
            state=PatientDataInput.input_name,
        )


dialog = Dialog(greet_window())

