

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UasZoneVersionType(enum.StrEnum):
    USPACE = "USPACE"
    PROHIBITED = "PROHIBITED"
    REQ_AUTHORIZATION = "REQ_AUTHORIZATION"
    CONDITIONAL = "CONDITIONAL"
    NO_RESTRICTION = "NO_RESTRICTION"

    def visit(
        self,
        uspace: typing.Callable[[], T_Result],
        prohibited: typing.Callable[[], T_Result],
        req_authorization: typing.Callable[[], T_Result],
        conditional: typing.Callable[[], T_Result],
        no_restriction: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UasZoneVersionType.USPACE:
            return uspace()
        if self is UasZoneVersionType.PROHIBITED:
            return prohibited()
        if self is UasZoneVersionType.REQ_AUTHORIZATION:
            return req_authorization()
        if self is UasZoneVersionType.CONDITIONAL:
            return conditional()
        if self is UasZoneVersionType.NO_RESTRICTION:
            return no_restriction()
