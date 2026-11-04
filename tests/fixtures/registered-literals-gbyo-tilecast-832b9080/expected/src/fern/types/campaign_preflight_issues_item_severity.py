

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CampaignPreflightIssuesItemSeverity(enum.StrEnum):
    WARNING = "warning"
    ERROR = "error"

    def visit(self, warning: typing.Callable[[], T_Result], error: typing.Callable[[], T_Result]) -> T_Result:
        if self is CampaignPreflightIssuesItemSeverity.WARNING:
            return warning()
        if self is CampaignPreflightIssuesItemSeverity.ERROR:
            return error()
