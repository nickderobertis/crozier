

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostFlowsSegmentsDeletedPayloadEventType(enum.StrEnum):
    FLOWS_SEGMENTS_DELETED = "flows/segments_deleted"

    def visit(self, flows_segments_deleted: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostFlowsSegmentsDeletedPayloadEventType.FLOWS_SEGMENTS_DELETED:
            return flows_segments_deleted()
