

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JournalEntryKindLabel(enum.StrEnum):
    INFO = "Info"
    SUCCESS = "Success"
    WARNING = "Warning"
    DANGER = "Danger"

    def visit(
        self,
        info: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
        warning: typing.Callable[[], T_Result],
        danger: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JournalEntryKindLabel.INFO:
            return info()
        if self is JournalEntryKindLabel.SUCCESS:
            return success()
        if self is JournalEntryKindLabel.WARNING:
            return warning()
        if self is JournalEntryKindLabel.DANGER:
            return danger()
