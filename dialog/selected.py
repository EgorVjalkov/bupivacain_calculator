from aiogram import Router
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Select
from aiogram_dialog.widgets.input.text import TextInput

from dialog.states import PatientDataInput


async def on_choosen_func(c: CallbackQuery,
                          w: Select,
                          dm: DialogManager,
                          item_id: str,
                          **kwargs) -> None:
    ctx = dm.current_context()
    ctx.dialog_data.update(category_id=item_id)
    if item_id == 'count_bleed':
        await dm.switch_to(state=PatientDataInput.input_patient_data_for_bleed)
    elif item_id == 'count_sma':
        await dm.switch_to(state=PatientDataInput.input_patient_data_for_sma)


async def on_chosen_patient_data(c: CallbackQuery,
                                 w: Select,
                                 dm: DialogManager,
                                 item_id: str,
                                 **kwargs) -> None:

    ctx = dm.current_context()
    ctx.dialog_data.update(patient_data=item_id)
    print(ctx.dialog_data)
    await dm.switch_to(state=PatientDataInput.input_data)


async def on_entered_data(m: Message,
                          w: TextInput,
                          dm: DialogManager,
                          input_data: str,
                          **kwargs) -> None:

    if not input_data.isdigit():
        await m.answer('Задайте число.')
        return

    ctx = dm.current_context()
    input_data = int(input_data)
    patient_data = ctx.dialog_data.get('patient_data') # <- здесь еще нужны лимиты типа женщина не может весить 20 кг и т.д
    ctx.dialog_data.update({patient_data: input_data})
    await dm.switch_to(PatientDataInput.input_patient_data_for_bleed)

