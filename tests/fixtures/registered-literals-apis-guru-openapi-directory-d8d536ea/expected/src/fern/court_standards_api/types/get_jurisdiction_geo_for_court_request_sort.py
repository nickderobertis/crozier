

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetJurisdictionGeoForCourtRequestSort(enum.StrEnum):
    STATE = "state"

    def visit(self, state: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetJurisdictionGeoForCourtRequestSort.STATE:
            return state()
