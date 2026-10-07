

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StartupLogsNotificationStatus(enum.StrEnum):
    APPEND = "append"
    DONE = "done"
    START = "start"

    def visit(
        self,
        append: typing.Callable[[], T_Result],
        done: typing.Callable[[], T_Result],
        start: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StartupLogsNotificationStatus.APPEND:
            return append()
        if self is StartupLogsNotificationStatus.DONE:
            return done()
        if self is StartupLogsNotificationStatus.START:
            return start()
