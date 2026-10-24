

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetricMaterializationStatus(enum.StrEnum):
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    PARTIAL = "partial"
    QUARANTINED = "quarantined"
    FAILED = "failed"

    def visit(
        self,
        running: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        partial: typing.Callable[[], T_Result],
        quarantined: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MetricMaterializationStatus.RUNNING:
            return running()
        if self is MetricMaterializationStatus.SUCCEEDED:
            return succeeded()
        if self is MetricMaterializationStatus.PARTIAL:
            return partial()
        if self is MetricMaterializationStatus.QUARANTINED:
            return quarantined()
        if self is MetricMaterializationStatus.FAILED:
            return failed()
