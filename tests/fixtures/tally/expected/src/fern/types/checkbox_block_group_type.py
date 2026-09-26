

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CheckboxBlockGroupType(enum.StrEnum):
    CHECKBOXES = "CHECKBOXES"

    def visit(self, checkboxes: typing.Callable[[], T_Result]) -> T_Result:
        if self is CheckboxBlockGroupType.CHECKBOXES:
            return checkboxes()
