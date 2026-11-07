

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PolicyDecisionV2ResolvedTier(enum.StrEnum):
    ROUTINE = "routine"
    STANDARD = "standard"
    ELEVATED = "elevated"
    MAXIMUM = "maximum"

    def visit(
        self,
        routine: typing.Callable[[], T_Result],
        standard: typing.Callable[[], T_Result],
        elevated: typing.Callable[[], T_Result],
        maximum: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PolicyDecisionV2ResolvedTier.ROUTINE:
            return routine()
        if self is PolicyDecisionV2ResolvedTier.STANDARD:
            return standard()
        if self is PolicyDecisionV2ResolvedTier.ELEVATED:
            return elevated()
        if self is PolicyDecisionV2ResolvedTier.MAXIMUM:
            return maximum()
