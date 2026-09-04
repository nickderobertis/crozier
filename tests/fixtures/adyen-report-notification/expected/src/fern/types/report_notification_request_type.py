

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReportNotificationRequestType(enum.StrEnum):
    """
    Type of webhook.
    """

    BALANCE_PLATFORM_REPORT_CREATED = "balancePlatform.report.created"

    def visit(self, balance_platform_report_created: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReportNotificationRequestType.BALANCE_PLATFORM_REPORT_CREATED:
            return balance_platform_report_created()
