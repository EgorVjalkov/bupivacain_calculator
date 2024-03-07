import operator

from aiogram_dialog.widgets.kbd import ScrollingGroup, Select, Column, Row, Button, Back
from aiogram_dialog.widgets.text import Const, Format


SCROLLING_HEIGHT = 1


def column_kb(on_click):
    return Column(
        Select(
            Format('{item[0]}'),
            id='gen_pat_data',
            item_id_getter=operator.itemgetter(1),
            items='patient_general_categories',
            on_click=on_click
        ),
        id='func_ids',
    )


def row_save_back(on_click, category):
    return Row(
        Button(Const('save'),
               id=f'save_{category}',
               on_click=on_click),
        Back(Const('back'))
    )


def paginated_kb(on_click):
    return ScrollingGroup(
        Select(
            Format('{item[0]}'),
            id='s_scroll_funcs',
            item_id_getter=operator.itemgetter(1),
            items='funcs',
            on_click=on_click
        ),
        id='func_ids',
        width=1, height=SCROLLING_HEIGHT,
    )
