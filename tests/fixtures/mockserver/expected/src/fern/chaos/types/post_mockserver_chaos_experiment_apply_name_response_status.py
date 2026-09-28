

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostMockserverChaosExperimentApplyNameResponseStatus(enum.StrEnum):
    STARTED = "started"

    def visit(self, started: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostMockserverChaosExperimentApplyNameResponseStatus.STARTED:
            return started()
