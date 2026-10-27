

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatMessagePolicyViolationUserAction(enum.StrEnum):
    NONE = "none"
    OVERRIDE = "override"
    REPORT_FALSE_POSITIVE = "reportFalsePositive"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        override: typing.Callable[[], T_Result],
        report_false_positive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatMessagePolicyViolationUserAction.NONE:
            return none()
        if self is ChatMessagePolicyViolationUserAction.OVERRIDE:
            return override()
        if self is ChatMessagePolicyViolationUserAction.REPORT_FALSE_POSITIVE:
            return report_false_positive()
