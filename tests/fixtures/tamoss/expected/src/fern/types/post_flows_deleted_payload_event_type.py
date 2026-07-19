

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostFlowsDeletedPayloadEventType(enum.StrEnum):
    FLOWS_DELETED = "flows/deleted"

    def visit(self, flows_deleted: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostFlowsDeletedPayloadEventType.FLOWS_DELETED:
            return flows_deleted()
