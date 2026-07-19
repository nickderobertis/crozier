

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AgentsSearchDeployedAgentsRequestSortBy(enum.StrEnum):
    CREATED_AT = "created_at"
    LAST_RUN_COMPLETION = "last_run_completion"

    def visit(
        self, created_at: typing.Callable[[], T_Result], last_run_completion: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is AgentsSearchDeployedAgentsRequestSortBy.CREATED_AT:
            return created_at()
        if self is AgentsSearchDeployedAgentsRequestSortBy.LAST_RUN_COMPLETION:
            return last_run_completion()
