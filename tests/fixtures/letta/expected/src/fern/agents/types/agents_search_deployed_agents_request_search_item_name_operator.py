

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AgentsSearchDeployedAgentsRequestSearchItemNameOperator(enum.StrEnum):
    EQ = "eq"
    CONTAINS = "contains"

    def visit(self, eq: typing.Callable[[], T_Result], contains: typing.Callable[[], T_Result]) -> T_Result:
        if self is AgentsSearchDeployedAgentsRequestSearchItemNameOperator.EQ:
            return eq()
        if self is AgentsSearchDeployedAgentsRequestSearchItemNameOperator.CONTAINS:
            return contains()
