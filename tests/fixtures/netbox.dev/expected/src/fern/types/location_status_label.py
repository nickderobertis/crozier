

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LocationStatusLabel(enum.StrEnum):
    PLANNED = "Planned"
    STAGING = "Staging"
    ACTIVE = "Active"
    DECOMMISSIONING = "Decommissioning"
    RETIRED = "Retired"

    def visit(
        self,
        planned: typing.Callable[[], T_Result],
        staging: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        decommissioning: typing.Callable[[], T_Result],
        retired: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LocationStatusLabel.PLANNED:
            return planned()
        if self is LocationStatusLabel.STAGING:
            return staging()
        if self is LocationStatusLabel.ACTIVE:
            return active()
        if self is LocationStatusLabel.DECOMMISSIONING:
            return decommissioning()
        if self is LocationStatusLabel.RETIRED:
            return retired()
