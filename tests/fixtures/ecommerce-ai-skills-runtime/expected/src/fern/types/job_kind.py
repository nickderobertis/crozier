

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobKind(enum.StrEnum):
    AGENT_RUN_EXECUTE = "agent_run.execute"

    def visit(self, agent_run_execute: typing.Callable[[], T_Result]) -> T_Result:
        if self is JobKind.AGENT_RUN_EXECUTE:
            return agent_run_execute()
