

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AgentsSearchDeployedAgentsRequestSearchItemIdentityOperator(enum.StrEnum):
    EQ = "eq"

    def visit(self, eq: typing.Callable[[], T_Result]) -> T_Result:
        if self is AgentsSearchDeployedAgentsRequestSearchItemIdentityOperator.EQ:
            return eq()
