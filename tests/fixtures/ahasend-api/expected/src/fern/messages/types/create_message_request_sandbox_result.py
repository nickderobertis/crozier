

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateMessageRequestSandboxResult(enum.StrEnum):
    """
    The result of the sandbox send
    """

    DELIVER = "deliver"
    BOUNCE = "bounce"
    DEFER = "defer"
    FAIL = "fail"
    SUPPRESS = "suppress"

    def visit(
        self,
        deliver: typing.Callable[[], T_Result],
        bounce: typing.Callable[[], T_Result],
        defer: typing.Callable[[], T_Result],
        fail: typing.Callable[[], T_Result],
        suppress: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateMessageRequestSandboxResult.DELIVER:
            return deliver()
        if self is CreateMessageRequestSandboxResult.BOUNCE:
            return bounce()
        if self is CreateMessageRequestSandboxResult.DEFER:
            return defer()
        if self is CreateMessageRequestSandboxResult.FAIL:
            return fail()
        if self is CreateMessageRequestSandboxResult.SUPPRESS:
            return suppress()
