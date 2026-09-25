

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Heading2BlockGroupType(enum.StrEnum):
    HEADING2 = "HEADING_2"

    def visit(self, heading2: typing.Callable[[], T_Result]) -> T_Result:
        if self is Heading2BlockGroupType.HEADING2:
            return heading2()
