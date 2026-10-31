

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SelectionState(enum.StrEnum):
    SELECTED = "selected"
    UNSELECTED = "unselected"
    INDETERMINATE = "indeterminate"

    def visit(
        self,
        selected: typing.Callable[[], T_Result],
        unselected: typing.Callable[[], T_Result],
        indeterminate: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SelectionState.SELECTED:
            return selected()
        if self is SelectionState.UNSELECTED:
            return unselected()
        if self is SelectionState.INDETERMINATE:
            return indeterminate()
