

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SaveConfigAutosave(enum.StrEnum):
    AFTER_DELAY = "after_delay"
    OFF = "off"

    def visit(self, after_delay: typing.Callable[[], T_Result], off: typing.Callable[[], T_Result]) -> T_Result:
        if self is SaveConfigAutosave.AFTER_DELAY:
            return after_delay()
        if self is SaveConfigAutosave.OFF:
            return off()
