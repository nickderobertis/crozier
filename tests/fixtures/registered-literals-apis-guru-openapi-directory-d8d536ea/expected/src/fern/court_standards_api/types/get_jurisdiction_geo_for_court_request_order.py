

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetJurisdictionGeoForCourtRequestOrder(enum.StrEnum):
    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetJurisdictionGeoForCourtRequestOrder.ASC:
            return asc()
        if self is GetJurisdictionGeoForCourtRequestOrder.DESC:
            return desc()
