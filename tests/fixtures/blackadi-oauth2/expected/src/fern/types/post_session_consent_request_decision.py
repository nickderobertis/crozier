

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostSessionConsentRequestDecision(enum.StrEnum):
    APPROVE = "approve"
    DENY = "deny"

    def visit(self, approve: typing.Callable[[], T_Result], deny: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostSessionConsentRequestDecision.APPROVE:
            return approve()
        if self is PostSessionConsentRequestDecision.DENY:
            return deny()
