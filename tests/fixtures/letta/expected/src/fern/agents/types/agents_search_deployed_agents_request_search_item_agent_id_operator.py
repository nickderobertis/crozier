

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AgentsSearchDeployedAgentsRequestSearchItemAgentIdOperator(enum.StrEnum):
    EQ = "eq"

    def visit(self, eq: typing.Callable[[], T_Result]) -> T_Result:
        if self is AgentsSearchDeployedAgentsRequestSearchItemAgentIdOperator.EQ:
            return eq()
