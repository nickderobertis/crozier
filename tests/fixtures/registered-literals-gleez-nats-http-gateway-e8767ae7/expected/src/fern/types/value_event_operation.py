

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ValueEventOperation(enum.StrEnum):
    PUT = "PUT"
    DEL = "DEL"
    PURGE = "PURGE"

    def visit(
        self,
        put: typing.Callable[[], T_Result],
        del_: typing.Callable[[], T_Result],
        purge: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ValueEventOperation.PUT:
            return put()
        if self is ValueEventOperation.DEL:
            return del_()
        if self is ValueEventOperation.PURGE:
            return purge()
