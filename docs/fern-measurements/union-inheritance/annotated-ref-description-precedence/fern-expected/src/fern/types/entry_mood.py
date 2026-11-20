

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntryMood(enum.StrEnum):
    """
    The mood's wording.
    """

    CALM = "calm"
    BRISK = "brisk"

    def visit(self, calm: typing.Callable[[], T_Result], brisk: typing.Callable[[], T_Result]) -> T_Result:
        if self is EntryMood.CALM:
            return calm()
        if self is EntryMood.BRISK:
            return brisk()
