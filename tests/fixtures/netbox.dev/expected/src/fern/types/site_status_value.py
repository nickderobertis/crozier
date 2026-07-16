

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SiteStatusValue(str, enum.Enum):
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
        if self is SiteStatusValue.PLANNED:
            return planned()
        if self is SiteStatusValue.STAGING:
            return staging()
        if self is SiteStatusValue.ACTIVE:
            return active()
        if self is SiteStatusValue.DECOMMISSIONING:
            return decommissioning()
        if self is SiteStatusValue.RETIRED:
            return retired()
