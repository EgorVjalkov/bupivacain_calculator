from aiogram import Router
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Select

from dialog.states import PatientDataInput


async def on_choosen_func(c: CallbackQuery,
                          w: Select,
                          dm: DialogManager,
                          item_id: str,
                          **kwargs) -> None:
    ctx = dm.current_context()
    ctx.dialog_data.update(category_id=item_id)
    await dm.switch_to(state=PatientDataInput.func_menu)


async def input_patient_data(c: CallbackQuery,
                             w: Select,
                             dm: DialogManager,
                             item_id: str,
                             **kwargs) -> None:

    if item_id == 'pat_n':
        await dm.switch_to(state=PatientDataInput.input_name)
        await c.message.answer('Введите имя пациентки')

    elif item_id == 'pat_h':
        await dm.switch_to(state=PatientDataInput.input_height)
        await c.message.answer('Введите показатель роста в см')

    elif item_id == 'pat_w':
        await dm.switch_to(state=PatientDataInput.input_height)
        await c.message.answer('Введите показатель веса в кг')


input_patient_data_router = Router()


@input_patient_data_router.message(PatientDataInput.input_name)
async def input_name(message: Message, dm: DialogManager):
    ctx = dm.current_context()
    ctx.dialog_data.update(category_id=message.text)
    data = await ctx.dialog_data
    print(data)
    await dm.switch_to(state=PatientDataInput.input_general_patient_data)






