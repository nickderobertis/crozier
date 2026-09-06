

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchProjectSettingsSpanFieldOrderItemLayoutOne(enum.StrEnum):
    TWO_COLUMN = "two_column"

    def visit(self, two_column: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchProjectSettingsSpanFieldOrderItemLayoutOne.TWO_COLUMN:
            return two_column()
