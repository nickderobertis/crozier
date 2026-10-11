

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FindSlotsRequestCrossingOne(enum.StrEnum):
    NEXT = "next"

    def visit(self, next: typing.Callable[[], T_Result]) -> T_Result:
        if self is FindSlotsRequestCrossingOne.NEXT:
            return next()
