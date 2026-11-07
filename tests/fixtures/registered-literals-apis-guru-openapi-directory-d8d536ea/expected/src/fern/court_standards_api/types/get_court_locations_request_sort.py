

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCourtLocationsRequestSort(enum.StrEnum):
    NAME = "name"

    def visit(self, name: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetCourtLocationsRequestSort.NAME:
            return name()
