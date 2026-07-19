

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AgentsSearchDeployedAgentsRequestCombinator(enum.StrEnum):
    AND = "AND"

    def visit(self, and_: typing.Callable[[], T_Result]) -> T_Result:
        if self is AgentsSearchDeployedAgentsRequestCombinator.AND:
            return and_()
