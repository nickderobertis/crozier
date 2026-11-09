

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCourtsForJurisdictionGeoRequestSort(enum.StrEnum):
    NAME = "name"

    def visit(self, name: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetCourtsForJurisdictionGeoRequestSort.NAME:
            return name()
