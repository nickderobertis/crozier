

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlertSeverity(enum.StrEnum):
    """
    Alert severity level.

    |Severity|Description|
    |:---|:---|
    |Information|Better to fix but it is operating accurately.|
    |Warning|Should fix it asap.|
    |Critical|Starting prohibited without repair.|
    """

    INFORMATION = "Information"
    WARNING = "Warning"
    CRITICAL = "Critical"

    def visit(
        self,
        information: typing.Callable[[], T_Result],
        warning: typing.Callable[[], T_Result],
        critical: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AlertSeverity.INFORMATION:
            return information()
        if self is AlertSeverity.WARNING:
            return warning()
        if self is AlertSeverity.CRITICAL:
            return critical()
