

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConnectionStatusMessageConnectionStatusStatus(enum.StrEnum):
    """
    Whether the connection check passed.
    """

    SUCCEEDED = "succeeded"
    FAILED = "failed"

    def visit(self, succeeded: typing.Callable[[], T_Result], failed: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConnectionStatusMessageConnectionStatusStatus.SUCCEEDED:
            return succeeded()
        if self is ConnectionStatusMessageConnectionStatusStatus.FAILED:
            return failed()
