

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostFlowsCreatedPayloadEventType(enum.StrEnum):
    FLOWS_CREATED = "flows/created"

    def visit(self, flows_created: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostFlowsCreatedPayloadEventType.FLOWS_CREATED:
            return flows_created()
