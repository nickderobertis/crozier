

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAttorneyRepresentationTypesRequestOrder(enum.StrEnum):
    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetAttorneyRepresentationTypesRequestOrder.ASC:
            return asc()
        if self is GetAttorneyRepresentationTypesRequestOrder.DESC:
            return desc()
