

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListInternalRunsRequestDurationOperator(enum.StrEnum):
    GT = "gt"
    LT = "lt"
    EQ = "eq"

    def visit(
        self, gt: typing.Callable[[], T_Result], lt: typing.Callable[[], T_Result], eq: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is ListInternalRunsRequestDurationOperator.GT:
            return gt()
        if self is ListInternalRunsRequestDurationOperator.LT:
            return lt()
        if self is ListInternalRunsRequestDurationOperator.EQ:
            return eq()
