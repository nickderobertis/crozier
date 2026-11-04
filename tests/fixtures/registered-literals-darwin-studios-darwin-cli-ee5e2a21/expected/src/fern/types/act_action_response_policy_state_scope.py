

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActActionResponsePolicyStateScope(enum.StrEnum):
    ACTION = "ACTION"
    CAPABILITY = "CAPABILITY"
    LISTING = "LISTING"
    AI = "AI"
    ACCOUNT = "ACCOUNT"

    def visit(
        self,
        action: typing.Callable[[], T_Result],
        capability: typing.Callable[[], T_Result],
        listing: typing.Callable[[], T_Result],
        ai: typing.Callable[[], T_Result],
        account: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActActionResponsePolicyStateScope.ACTION:
            return action()
        if self is ActActionResponsePolicyStateScope.CAPABILITY:
            return capability()
        if self is ActActionResponsePolicyStateScope.LISTING:
            return listing()
        if self is ActActionResponsePolicyStateScope.AI:
            return ai()
        if self is ActActionResponsePolicyStateScope.ACCOUNT:
            return account()
