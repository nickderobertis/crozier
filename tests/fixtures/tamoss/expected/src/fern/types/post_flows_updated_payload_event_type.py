

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostFlowsUpdatedPayloadEventType(enum.StrEnum):
    FLOWS_UPDATED = "flows/updated"

    def visit(self, flows_updated: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostFlowsUpdatedPayloadEventType.FLOWS_UPDATED:
            return flows_updated()
