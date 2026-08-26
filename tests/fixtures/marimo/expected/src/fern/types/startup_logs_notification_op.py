

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StartupLogsNotificationOp(enum.StrEnum):
    STARTUP_LOGS = "startup-logs"

    def visit(self, startup_logs: typing.Callable[[], T_Result]) -> T_Result:
        if self is StartupLogsNotificationOp.STARTUP_LOGS:
            return startup_logs()
