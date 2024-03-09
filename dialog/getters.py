from aiogram_dialog import DialogManager
from dialog.variants_with_id import get_dict_with_variants, Category, bleed_vars, patient_data_for_bleed
from dialog.states import PatientDataInput
from typing import Optional


async def get_funcs(dialog_manager: DialogManager,
                    **middleware_data) -> dict:
    return get_dict_with_variants('funcs')


async def get_data(dialog_manager: DialogManager,
                   **middleware_date) -> dict:
    ctx = dialog_manager.current_context()
    data = ctx.dialog_data
    return data


async def get_categories_for_bleed(dialog_manager: DialogManager,
                                   **middleware_date) -> dict:
    data = await get_data(dialog_manager, **middleware_date)
    variants = bleed_vars.copy()
    for i in variants:
        btn, btn_id = i
        if btn_id in data:
            variants[variants.index(i)] = (f'{btn}: {data[btn_id]}', btn_id)

    if patient_data_for_bleed.filled(data):
        variants.append(('рассчитать', 'count'))
    return {'bleed_categories': variants}


async def get_categories_for_sma(dialog_manager: DialogManager,
                                 **middleware_date) -> dict:
    return get_dict_with_variants('sma_categories')


async def get_topics_for_input(dialog_manager: DialogManager,
                               **middleware_date) -> Optional[dict]:
    ctx = dialog_manager.current_context()
    patient_data = ctx.dialog_data.get('patient_data')
    if not patient_data:
        await dialog_manager.event.answer('Выберите показатель для заполнения')
        await dialog_manager.switch_to(PatientDataInput.input_patient_data_for_bleed)
        return
    else:
        category = Category(patient_data)
        data = {'category': category}
        return data
