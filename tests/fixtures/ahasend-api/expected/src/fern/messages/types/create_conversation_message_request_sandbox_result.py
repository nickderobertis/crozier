

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateConversationMessageRequestSandboxResult(enum.StrEnum):
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
        if self is CreateConversationMessageRequestSandboxResult.DELIVER:
            return deliver()
        if self is CreateConversationMessageRequestSandboxResult.BOUNCE:
            return bounce()
        if self is CreateConversationMessageRequestSandboxResult.DEFER:
            return defer()
        if self is CreateConversationMessageRequestSandboxResult.FAIL:
            return fail()
        if self is CreateConversationMessageRequestSandboxResult.SUPPRESS:
            return suppress()
