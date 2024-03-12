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
        kbs.group_kb(selected.on_choosen_func, 'g_func', 's_funcs', 'funcs'),
        Cancel(Const('никаких задач'),
               on_click=selected.bye_and_get_result),
        state=PatientDataInput.func_menu,
        getter=getters.get_funcs,
    )


def input_patient_data_window() -> Window:
    return Window(
        Const('Бот может посчитать предполагаемый ОЦК пациентки. Введите показатели.'),
        kbs.group_kb(selected.on_chosen_patient_data,
                     'g_bleed', 's_bleed', 'patient_parameters'),
        Back(Const('<< назад')),
        state=PatientDataInput.input_patient_data_menu,
        getter=getters.get_variants,
    )


def input_window() -> Window:
    return Window(
        Format('{category.answer}'),
        TextInput(id='enter_data',
                  on_success=selected.on_entered_data),
        Back(Const('<< назад')),
        state=PatientDataInput.input_parameter,
        getter=getters.get_topics_for_input,
    )


def report_window() -> Window:
    return Window(
        Format("{func_result}"),
        Button(Const('<< изменить параметры'),
               id='b_to_input_menu',
               on_click=selected.back_to_input_menu),
        Button(Const('<< назад в меню функций'),
               id='b_to_main_menu',
               on_click=selected.back_to_main_menu),
        Cancel(Const('задача решена!')),
        state=PatientDataInput.report,
        getter=getters.get_report)


dialog = Dialog(greet_window(), input_patient_data_window(), input_window(), report_window())
