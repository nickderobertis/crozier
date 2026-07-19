

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AgentsSearchDeployedAgentsRequestSearchItemTagsOperator(enum.StrEnum):
    CONTAINS = "contains"

    def visit(self, contains: typing.Callable[[], T_Result]) -> T_Result:
        if self is AgentsSearchDeployedAgentsRequestSearchItemTagsOperator.CONTAINS:
            return contains()
