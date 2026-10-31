

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WorkflowParameterDirection(enum.StrEnum):
    IN = "in"
    OUT = "out"
    INOUT = "inout"

    def visit(
        self,
        in_: typing.Callable[[], T_Result],
        out: typing.Callable[[], T_Result],
        inout: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WorkflowParameterDirection.IN:
            return in_()
        if self is WorkflowParameterDirection.OUT:
            return out()
        if self is WorkflowParameterDirection.INOUT:
            return inout()
