

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InstallingPackageAlertNotificationLogStatus(enum.StrEnum):
    APPEND = "append"
    DONE = "done"
    START = "start"

    def visit(
        self,
        append: typing.Callable[[], T_Result],
        done: typing.Callable[[], T_Result],
        start: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InstallingPackageAlertNotificationLogStatus.APPEND:
            return append()
        if self is InstallingPackageAlertNotificationLogStatus.DONE:
            return done()
        if self is InstallingPackageAlertNotificationLogStatus.START:
            return start()
