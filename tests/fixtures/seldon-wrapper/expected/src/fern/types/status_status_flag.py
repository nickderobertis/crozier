

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StatusStatusFlag(enum.StrEnum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"

    def visit(self, success: typing.Callable[[], T_Result], failure: typing.Callable[[], T_Result]) -> T_Result:
        if self is StatusStatusFlag.SUCCESS:
            return success()
        if self is StatusStatusFlag.FAILURE:
            return failure()
