

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SailboatHull(enum.StrEnum):
    SAIL = "sail"

    def visit(self, sail: typing.Callable[[], T_Result]) -> T_Result:
        if self is SailboatHull.SAIL:
            return sail()
