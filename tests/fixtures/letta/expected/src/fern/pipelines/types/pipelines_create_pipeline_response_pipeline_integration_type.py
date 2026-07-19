

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PipelinesCreatePipelineResponsePipelineIntegrationType(enum.StrEnum):
    SLACK = "slack"

    def visit(self, slack: typing.Callable[[], T_Result]) -> T_Result:
        if self is PipelinesCreatePipelineResponsePipelineIntegrationType.SLACK:
            return slack()
