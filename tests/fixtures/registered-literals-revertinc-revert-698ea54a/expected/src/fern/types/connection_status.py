

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConnectionStatus(enum.StrEnum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"

    def visit(self, success: typing.Callable[[], T_Result], failed: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConnectionStatus.SUCCESS:
            return success()
        if self is ConnectionStatus.FAILED:
            return failed()
