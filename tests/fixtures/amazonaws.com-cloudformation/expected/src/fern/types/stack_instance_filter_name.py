

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StackInstanceFilterName(enum.StrEnum):
    DETAILED_STATUS = "DETAILED_STATUS"
    LAST_OPERATION_ID = "LAST_OPERATION_ID"

    def visit(
        self, detailed_status: typing.Callable[[], T_Result], last_operation_id: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is StackInstanceFilterName.DETAILED_STATUS:
            return detailed_status()
        if self is StackInstanceFilterName.LAST_OPERATION_ID:
            return last_operation_id()
