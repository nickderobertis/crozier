

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssembleModePageElementsItem(enum.StrEnum):
    H = "H"
    M = "M"
    NONE = "None"

    def visit(
        self, h: typing.Callable[[], T_Result], m: typing.Callable[[], T_Result], none: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is AssembleModePageElementsItem.H:
            return h()
        if self is AssembleModePageElementsItem.M:
            return m()
        if self is AssembleModePageElementsItem.NONE:
            return none()
