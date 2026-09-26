

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataTriggerOp(enum.StrEnum):
    """
    The operator of the trigger function.
    """

    EQUALS_TO = "equalsTo"
    GREATER_THAN = "greaterThan"
    LOWER_THAN = "lowerThan"
    INCLUDED_IN = "includedIn"
    ON_CHANGE = "onChange"

    def visit(
        self,
        equals_to: typing.Callable[[], T_Result],
        greater_than: typing.Callable[[], T_Result],
        lower_than: typing.Callable[[], T_Result],
        included_in: typing.Callable[[], T_Result],
        on_change: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DataTriggerOp.EQUALS_TO:
            return equals_to()
        if self is DataTriggerOp.GREATER_THAN:
            return greater_than()
        if self is DataTriggerOp.LOWER_THAN:
            return lower_than()
        if self is DataTriggerOp.INCLUDED_IN:
            return included_in()
        if self is DataTriggerOp.ON_CHANGE:
            return on_change()
