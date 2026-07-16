

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LocationStatusValue(enum.StrEnum):
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
        if self is LocationStatusValue.PLANNED:
            return planned()
        if self is LocationStatusValue.STAGING:
            return staging()
        if self is LocationStatusValue.ACTIVE:
            return active()
        if self is LocationStatusValue.DECOMMISSIONING:
            return decommissioning()
        if self is LocationStatusValue.RETIRED:
            return retired()
