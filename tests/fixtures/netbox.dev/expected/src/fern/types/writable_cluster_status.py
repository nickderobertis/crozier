

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WritableClusterStatus(enum.StrEnum):
    PLANNED = "planned"
    STAGING = "staging"
    ACTIVE = "active"
    DECOMMISSIONING = "decommissioning"
    OFFLINE = "offline"

    def visit(
        self,
        planned: typing.Callable[[], T_Result],
        staging: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        decommissioning: typing.Callable[[], T_Result],
        offline: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableClusterStatus.PLANNED:
            return planned()
        if self is WritableClusterStatus.STAGING:
            return staging()
        if self is WritableClusterStatus.ACTIVE:
            return active()
        if self is WritableClusterStatus.DECOMMISSIONING:
            return decommissioning()
        if self is WritableClusterStatus.OFFLINE:
            return offline()
