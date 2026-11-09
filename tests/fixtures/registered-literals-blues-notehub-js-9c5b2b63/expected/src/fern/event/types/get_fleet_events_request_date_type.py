

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetFleetEventsRequestDateType(enum.StrEnum):
    CAPTURED = "captured"
    UPLOADED = "uploaded"

    def visit(self, captured: typing.Callable[[], T_Result], uploaded: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetFleetEventsRequestDateType.CAPTURED:
            return captured()
        if self is GetFleetEventsRequestDateType.UPLOADED:
            return uploaded()
