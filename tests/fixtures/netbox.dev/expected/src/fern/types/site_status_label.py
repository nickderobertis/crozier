

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SiteStatusLabel(enum.StrEnum):
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
        if self is SiteStatusLabel.PLANNED:
            return planned()
        if self is SiteStatusLabel.STAGING:
            return staging()
        if self is SiteStatusLabel.ACTIVE:
            return active()
        if self is SiteStatusLabel.DECOMMISSIONING:
            return decommissioning()
        if self is SiteStatusLabel.RETIRED:
            return retired()
