

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatMessagePolicyViolationVerdictDetails(enum.StrEnum):
    NONE = "none"
    ALLOW = "allow"
    BLOCK = "block"
    OVERRIDE = "override"
    FALSE_POSITIVE = "falsePositive"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        allow: typing.Callable[[], T_Result],
        block: typing.Callable[[], T_Result],
        override: typing.Callable[[], T_Result],
        false_positive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatMessagePolicyViolationVerdictDetails.NONE:
            return none()
        if self is ChatMessagePolicyViolationVerdictDetails.ALLOW:
            return allow()
        if self is ChatMessagePolicyViolationVerdictDetails.BLOCK:
            return block()
        if self is ChatMessagePolicyViolationVerdictDetails.OVERRIDE:
            return override()
        if self is ChatMessagePolicyViolationVerdictDetails.FALSE_POSITIVE:
            return false_positive()
