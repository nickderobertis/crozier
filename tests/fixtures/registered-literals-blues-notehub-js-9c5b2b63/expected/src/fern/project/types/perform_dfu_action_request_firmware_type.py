

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PerformDfuActionRequestFirmwareType(enum.StrEnum):
    HOST = "host"
    NOTECARD = "notecard"

    def visit(self, host: typing.Callable[[], T_Result], notecard: typing.Callable[[], T_Result]) -> T_Result:
        if self is PerformDfuActionRequestFirmwareType.HOST:
            return host()
        if self is PerformDfuActionRequestFirmwareType.NOTECARD:
            return notecard()
