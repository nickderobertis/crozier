

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryStatus(enum.StrEnum):
    GUARDRAIL_BLOCKED = "guardrail_blocked"

    def visit(self, guardrail_blocked: typing.Callable[[], T_Result]) -> T_Result:
        if self is QueryStatus.GUARDRAIL_BLOCKED:
            return guardrail_blocked()
