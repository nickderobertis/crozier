

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SelectionMarkType(enum.StrEnum):
    CHECKBOX = "checkbox"
    RADIO = "radio"
    OTHER = "other"

    def visit(
        self,
        checkbox: typing.Callable[[], T_Result],
        radio: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SelectionMarkType.CHECKBOX:
            return checkbox()
        if self is SelectionMarkType.RADIO:
            return radio()
        if self is SelectionMarkType.OTHER:
            return other()
