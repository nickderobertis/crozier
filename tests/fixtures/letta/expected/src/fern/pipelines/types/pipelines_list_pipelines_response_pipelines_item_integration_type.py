

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PipelinesListPipelinesResponsePipelinesItemIntegrationType(enum.StrEnum):
    SLACK = "slack"

    def visit(self, slack: typing.Callable[[], T_Result]) -> T_Result:
        if self is PipelinesListPipelinesResponsePipelinesItemIntegrationType.SLACK:
            return slack()
