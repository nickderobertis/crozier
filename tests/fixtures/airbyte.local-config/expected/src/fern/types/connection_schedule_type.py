

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ConnectionScheduleType(str, enum.Enum):
    """
    determine how the schedule data should be interpreted
    """

    MANUAL = "manual"
    BASIC = "basic"
    CRON = "cron"

    def visit(
        self,
        manual: typing.Callable[[], T_Result],
        basic: typing.Callable[[], T_Result],
        cron: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConnectionScheduleType.MANUAL:
            return manual()
        if self is ConnectionScheduleType.BASIC:
            return basic()
        if self is ConnectionScheduleType.CRON:
            return cron()
