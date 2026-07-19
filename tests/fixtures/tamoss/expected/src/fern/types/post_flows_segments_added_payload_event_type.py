

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostFlowsSegmentsAddedPayloadEventType(enum.StrEnum):
    FLOWS_SEGMENTS_ADDED = "flows/segments_added"

    def visit(self, flows_segments_added: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostFlowsSegmentsAddedPayloadEventType.FLOWS_SEGMENTS_ADDED:
            return flows_segments_added()
