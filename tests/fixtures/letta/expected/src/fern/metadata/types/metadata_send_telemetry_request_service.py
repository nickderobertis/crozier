

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MetadataSendTelemetryRequestService(enum.StrEnum):
    LETTA_CODE = "letta-code"

    def visit(self, letta_code: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetadataSendTelemetryRequestService.LETTA_CODE:
            return letta_code()
