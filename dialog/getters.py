from aiogram_dialog import DialogManager
from dialog.states import PatientDataInput
from typing import Optional
from program_logic.Patient import Patient
from dialog.function import PatientParameter, Function
from dialog.variants_with_id import get_dict_with_variants


async def get_funcs(dialog_manager: DialogManager,
                    **middleware_data) -> dict:
    return get_dict_with_variants('funcs')


async def get_variants(dialog_manager: DialogManager,
                       **middleware_date) -> dict:
    ctx = dialog_manager.current_context()
    data = ctx.dialog_data

    func = Function(data)
    if 'patient_data' in data:
        func.set_btn_text()

    if func.is_args_ready:
        func.variants.append_count_var()
        data['func_result'] = func()
        dialog_manager.dialog_data.update(data)

    return {'patient_parameters': func.variants.vars_with_id}


async def get_topics_for_input(dialog_manager: DialogManager,
                               **middleware_date) -> Optional[dict]:
    ctx = dialog_manager.current_context()
    patient_data = ctx.dialog_data.get('patient_data')
    if not patient_data:
        await dialog_manager.event.answer('Выберите показатель для заполнения')
        await dialog_manager.switch_to(PatientDataInput.input_patient_data_menu)
        return
    else:
        category = PatientParameter(patient_data)
        data = {'category': category}
        return data


async def get_report(dialog_manager: DialogManager,
                     **middleware_date) -> dict:
    ctx = dialog_manager.current_context()
    if 'func_result' not in ctx.dialog_data:
        return {'func_result': 'Принял, до встречи'}

    func_result = ctx.dialog_data['func_result']
    return {'func_result': func_result}
