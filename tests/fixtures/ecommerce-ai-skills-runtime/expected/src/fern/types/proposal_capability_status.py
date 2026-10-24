

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProposalCapabilityStatus(enum.StrEnum):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"
    BLOCKED = "blocked"

    def visit(
        self,
        available: typing.Callable[[], T_Result],
        unavailable: typing.Callable[[], T_Result],
        blocked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProposalCapabilityStatus.AVAILABLE:
            return available()
        if self is ProposalCapabilityStatus.UNAVAILABLE:
            return unavailable()
        if self is ProposalCapabilityStatus.BLOCKED:
            return blocked()
