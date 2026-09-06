

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ReportingCurrentPackagesInUpdateGroupRequestSubscriptionTypeFilter(enum.StrEnum):
    REQUIRED_ONLY = "RequiredOnly"
    DEFAULT = "Default"
    ALL = "All"

    def visit(
        self,
        required_only: typing.Callable[[], T_Result],
        default: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReportingCurrentPackagesInUpdateGroupRequestSubscriptionTypeFilter.REQUIRED_ONLY:
            return required_only()
        if self is ReportingCurrentPackagesInUpdateGroupRequestSubscriptionTypeFilter.DEFAULT:
            return default()
        if self is ReportingCurrentPackagesInUpdateGroupRequestSubscriptionTypeFilter.ALL:
            return all_()
