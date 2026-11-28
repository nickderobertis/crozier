

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InventoryPlateTableNotePartMode(enum.StrEnum):
    CREATE_AND_FILL = "create_and_fill"
    FILL = "fill"
    UPDATE = "update"

    def visit(
        self,
        create_and_fill: typing.Callable[[], T_Result],
        fill: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InventoryPlateTableNotePartMode.CREATE_AND_FILL:
            return create_and_fill()
        if self is InventoryPlateTableNotePartMode.FILL:
            return fill()
        if self is InventoryPlateTableNotePartMode.UPDATE:
            return update()
