

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Heading1BlockGroupType(enum.StrEnum):
    HEADING1 = "HEADING_1"

    def visit(self, heading1: typing.Callable[[], T_Result]) -> T_Result:
        if self is Heading1BlockGroupType.HEADING1:
            return heading1()
