

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectSettingsSpanFieldOrderItemLayoutOne(enum.StrEnum):
    TWO_COLUMN = "two_column"

    def visit(self, two_column: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProjectSettingsSpanFieldOrderItemLayoutOne.TWO_COLUMN:
            return two_column()
