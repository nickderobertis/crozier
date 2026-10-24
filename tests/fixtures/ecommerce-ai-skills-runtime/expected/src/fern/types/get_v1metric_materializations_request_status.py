

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetV1MetricMaterializationsRequestStatus(enum.StrEnum):
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
        if self is GetV1MetricMaterializationsRequestStatus.RUNNING:
            return running()
        if self is GetV1MetricMaterializationsRequestStatus.SUCCEEDED:
            return succeeded()
        if self is GetV1MetricMaterializationsRequestStatus.PARTIAL:
            return partial()
        if self is GetV1MetricMaterializationsRequestStatus.QUARANTINED:
            return quarantined()
        if self is GetV1MetricMaterializationsRequestStatus.FAILED:
            return failed()
