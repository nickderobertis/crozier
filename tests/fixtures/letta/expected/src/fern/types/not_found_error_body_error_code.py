

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NotFoundErrorBodyErrorCode(enum.StrEnum):
    PIPELINE_NOT_FOUND = "pipelineNotFound"

    def visit(self, pipeline_not_found: typing.Callable[[], T_Result]) -> T_Result:
        if self is NotFoundErrorBodyErrorCode.PIPELINE_NOT_FOUND:
            return pipeline_not_found()
