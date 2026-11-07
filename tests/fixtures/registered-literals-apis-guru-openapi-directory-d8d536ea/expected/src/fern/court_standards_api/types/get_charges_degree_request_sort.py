

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChargesDegreeRequestSort(enum.StrEnum):
    NAME = "name"

    def visit(self, name: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetChargesDegreeRequestSort.NAME:
            return name()
