

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TrustRuleSuggestRequestIntent(enum.StrEnum):
    AUTO_APPROVE = "auto_approve"
    ESCALATE = "escalate"

    def visit(self, auto_approve: typing.Callable[[], T_Result], escalate: typing.Callable[[], T_Result]) -> T_Result:
        if self is TrustRuleSuggestRequestIntent.AUTO_APPROVE:
            return auto_approve()
        if self is TrustRuleSuggestRequestIntent.ESCALATE:
            return escalate()
