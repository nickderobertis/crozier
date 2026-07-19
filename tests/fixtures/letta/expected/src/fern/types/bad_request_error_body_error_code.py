

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BadRequestErrorBodyErrorCode(enum.StrEnum):
    PIPELINE_DISABLED = "pipelineDisabled"
    SYNC_FAILED = "syncFailed"

    def visit(
        self, pipeline_disabled: typing.Callable[[], T_Result], sync_failed: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is BadRequestErrorBodyErrorCode.PIPELINE_DISABLED:
            return pipeline_disabled()
        if self is BadRequestErrorBodyErrorCode.SYNC_FAILED:
            return sync_failed()
