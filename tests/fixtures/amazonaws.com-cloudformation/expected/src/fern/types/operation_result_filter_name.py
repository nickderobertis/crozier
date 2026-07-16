

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OperationResultFilterName(enum.StrEnum):
    OPERATION_RESULT_STATUS = "OPERATION_RESULT_STATUS"

    def visit(self, operation_result_status: typing.Callable[[], T_Result]) -> T_Result:
        if self is OperationResultFilterName.OPERATION_RESULT_STATUS:
            return operation_result_status()
