

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoFileDataKind(enum.StrEnum):
    BUTTON = "button"
    AREA = "area"

    def visit(self, button: typing.Callable[[], T_Result], area: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarimoFileDataKind.BUTTON:
            return button()
        if self is MarimoFileDataKind.AREA:
            return area()
