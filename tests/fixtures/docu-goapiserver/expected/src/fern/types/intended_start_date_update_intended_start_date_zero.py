

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IntendedStartDateUpdateIntendedStartDateZero(enum.StrEnum):
    TBD = "TBD"

    def visit(self, tbd: typing.Callable[[], T_Result]) -> T_Result:
        if self is IntendedStartDateUpdateIntendedStartDateZero.TBD:
            return tbd()
