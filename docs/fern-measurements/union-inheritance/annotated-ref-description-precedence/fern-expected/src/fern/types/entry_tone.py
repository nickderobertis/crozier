

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntryTone(enum.StrEnum):
    """
    The tone's wording.
    """

    CALM = "calm"
    BRISK = "brisk"

    def visit(self, calm: typing.Callable[[], T_Result], brisk: typing.Callable[[], T_Result]) -> T_Result:
        if self is EntryTone.CALM:
            return calm()
        if self is EntryTone.BRISK:
            return brisk()
