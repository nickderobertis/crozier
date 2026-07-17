

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ClusterStatusValue(enum.StrEnum):
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
        if self is ClusterStatusValue.PLANNED:
            return planned()
        if self is ClusterStatusValue.STAGING:
            return staging()
        if self is ClusterStatusValue.ACTIVE:
            return active()
        if self is ClusterStatusValue.DECOMMISSIONING:
            return decommissioning()
        if self is ClusterStatusValue.OFFLINE:
            return offline()
