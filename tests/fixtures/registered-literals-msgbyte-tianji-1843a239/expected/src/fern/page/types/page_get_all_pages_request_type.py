

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PageGetAllPagesRequestType(enum.StrEnum):
    STATUS = "status"
    STATIC = "static"
    ALL = "all"

    def visit(
        self,
        status: typing.Callable[[], T_Result],
        static: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PageGetAllPagesRequestType.STATUS:
            return status()
        if self is PageGetAllPagesRequestType.STATIC:
            return static()
        if self is PageGetAllPagesRequestType.ALL:
            return all_()
