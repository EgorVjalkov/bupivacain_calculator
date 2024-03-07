from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command

from aiogram_dialog import StartMode, DialogManager

from dialog.states import PatientDataInput


router = Router()


@router.message(Command('start'))
async def start_dialog(message: Message,
                       dialog_manager: DialogManager) -> None:
    await dialog_manager.start(PatientDataInput.func_menu,
                               mode=StartMode.RESET_STACK)
