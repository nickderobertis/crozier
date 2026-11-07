

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DisclosureType(enum.StrEnum):
    DISCLAIMER = "disclaimer"

    def visit(self, disclaimer: typing.Callable[[], T_Result]) -> T_Result:
        if self is DisclosureType.DISCLAIMER:
            return disclaimer()
