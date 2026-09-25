

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Heading3BlockGroupType(enum.StrEnum):
    HEADING3 = "HEADING_3"

    def visit(self, heading3: typing.Callable[[], T_Result]) -> T_Result:
        if self is Heading3BlockGroupType.HEADING3:
            return heading3()
