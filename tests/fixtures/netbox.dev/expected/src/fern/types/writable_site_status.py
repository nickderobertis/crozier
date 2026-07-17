

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WritableSiteStatus(enum.StrEnum):
    PLANNED = "planned"
    STAGING = "staging"
    ACTIVE = "active"
    DECOMMISSIONING = "decommissioning"
    RETIRED = "retired"

    def visit(
        self,
        planned: typing.Callable[[], T_Result],
        staging: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        decommissioning: typing.Callable[[], T_Result],
        retired: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableSiteStatus.PLANNED:
            return planned()
        if self is WritableSiteStatus.STAGING:
            return staging()
        if self is WritableSiteStatus.ACTIVE:
            return active()
        if self is WritableSiteStatus.DECOMMISSIONING:
            return decommissioning()
        if self is WritableSiteStatus.RETIRED:
            return retired()
