

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchProjectSettingsSpanFieldOrderItemLayoutZero(enum.StrEnum):
    FULL = "full"

    def visit(self, full: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchProjectSettingsSpanFieldOrderItemLayoutZero.FULL:
            return full()
