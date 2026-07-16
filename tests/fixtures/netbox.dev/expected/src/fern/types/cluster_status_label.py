

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ClusterStatusLabel(str, enum.Enum):
    PLANNED = "Planned"
    STAGING = "Staging"
    ACTIVE = "Active"
    DECOMMISSIONING = "Decommissioning"
    OFFLINE = "Offline"

    def visit(
        self,
        planned: typing.Callable[[], T_Result],
        staging: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        decommissioning: typing.Callable[[], T_Result],
        offline: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ClusterStatusLabel.PLANNED:
            return planned()
        if self is ClusterStatusLabel.STAGING:
            return staging()
        if self is ClusterStatusLabel.ACTIVE:
            return active()
        if self is ClusterStatusLabel.DECOMMISSIONING:
            return decommissioning()
        if self is ClusterStatusLabel.OFFLINE:
            return offline()
