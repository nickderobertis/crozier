

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StateMachineStateProcessResultDtoStateProcessType(enum.StrEnum):
    SUCCESS = "SUCCESS"
    FAIL = "FAIL"
    RESUBMIT = "RESUBMIT"
    UNKNOWN = "UNKNOWN"

    def visit(
        self,
        success: typing.Callable[[], T_Result],
        fail: typing.Callable[[], T_Result],
        resubmit: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StateMachineStateProcessResultDtoStateProcessType.SUCCESS:
            return success()
        if self is StateMachineStateProcessResultDtoStateProcessType.FAIL:
            return fail()
        if self is StateMachineStateProcessResultDtoStateProcessType.RESUBMIT:
            return resubmit()
        if self is StateMachineStateProcessResultDtoStateProcessType.UNKNOWN:
            return unknown()
