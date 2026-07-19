

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PipelinesPreviewPipelineRequestIntegrationType(enum.StrEnum):
    SLACK = "slack"

    def visit(self, slack: typing.Callable[[], T_Result]) -> T_Result:
        if self is PipelinesPreviewPipelineRequestIntegrationType.SLACK:
            return slack()
