

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JournalEntryKindValue(enum.StrEnum):
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
        if self is JournalEntryKindValue.INFO:
            return info()
        if self is JournalEntryKindValue.SUCCESS:
            return success()
        if self is JournalEntryKindValue.WARNING:
            return warning()
        if self is JournalEntryKindValue.DANGER:
            return danger()
