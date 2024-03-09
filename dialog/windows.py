from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Button, Start, Cancel, Back
from aiogram_dialog.widgets.input.text import TextInput

from dialog.states import PatientDataInput
from dialog import kbs
from dialog import selected
from dialog import getters
from dialog import variants_with_id


def greet_window() -> Window:
    return Window(
        Const('Привет, это бот для расчетов в акушерской анестезиологии, '
              'Задайте клиническую задачу.'),
        kbs.group_kb(selected.on_choosen_func, 'c_func', 's_funcs', 'funcs'),
        Cancel(Const('никаких задач')),
        state=PatientDataInput.func_menu,
        getter=getters.get_funcs,
    )


def bleed_window() -> Window:
    return Window(
        Const('Бот может посчитать предполагаемый ОЦК пациентки. Введите показатели.'),
        kbs.group_kb(selected.on_chosen_patient_data,
                     'g_bleed', 's_bleed', 'bleed_categories'),
        Back(Const('<< назад')),
        state=PatientDataInput.input_patient_data_for_bleed,
        getter=getters.get_categories_for_bleed,
    )


def input_window() -> Window:
    return Window(
        Format('{category.answer}'),
        TextInput(id='enter_data',
                  on_success=selected.on_entered_data),
        Back(Const('<< назад')),
        state=PatientDataInput.input_data,
        getter=getters.get_topics_for_input,
    )


# def input_name_window() -> Window:
#    return Window(
#            Const('Введите имя пациентки'),
#            (on_click=selected.input_name),
#            Back(Const('<<< назад')),
#            state=PatientDataInput.input_patient_data,
#
#        )


dialog = Dialog(greet_window(), bleed_window(), input_window())
