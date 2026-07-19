

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CompactionSettingsInputMode(enum.StrEnum):
    """
    The type of summarization technique use.
    """

    ALL = "all"
    SLIDING_WINDOW = "sliding_window"

    def visit(self, all_: typing.Callable[[], T_Result], sliding_window: typing.Callable[[], T_Result]) -> T_Result:
        if self is CompactionSettingsInputMode.ALL:
            return all_()
        if self is CompactionSettingsInputMode.SLIDING_WINDOW:
            return sliding_window()
