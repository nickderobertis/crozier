

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FederationNodeStatus(enum.StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    QUARANTINED = "quarantined"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
        quarantined: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FederationNodeStatus.ACTIVE:
            return active()
        if self is FederationNodeStatus.INACTIVE:
            return inactive()
        if self is FederationNodeStatus.QUARANTINED:
            return quarantined()
