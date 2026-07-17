

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WritableJournalEntryKind(enum.StrEnum):
    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    DANGER = "danger"

    def visit(
        self,
        info: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
        warning: typing.Callable[[], T_Result],
        danger: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableJournalEntryKind.INFO:
            return info()
        if self is WritableJournalEntryKind.SUCCESS:
            return success()
        if self is WritableJournalEntryKind.WARNING:
            return warning()
        if self is WritableJournalEntryKind.DANGER:
            return danger()
