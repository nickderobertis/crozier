

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutMockserverClearRequestType(enum.StrEnum):
    ALL = "all"
    LOG = "log"
    EXPECTATIONS = "expectations"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        log: typing.Callable[[], T_Result],
        expectations: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PutMockserverClearRequestType.ALL:
            return all_()
        if self is PutMockserverClearRequestType.LOG:
            return log()
        if self is PutMockserverClearRequestType.EXPECTATIONS:
            return expectations()
