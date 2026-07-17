

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SignalResourceInputStatus(enum.StrEnum):
    """
    The status of the signal, which is either success or failure. A failure signal causes CloudFormation to immediately fail the stack creation or update.
    """

    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"

    def visit(self, success: typing.Callable[[], T_Result], failure: typing.Callable[[], T_Result]) -> T_Result:
        if self is SignalResourceInputStatus.SUCCESS:
            return success()
        if self is SignalResourceInputStatus.FAILURE:
            return failure()
