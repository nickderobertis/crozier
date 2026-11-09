

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetDeviceDfuStatusRequestFirmwareType(enum.StrEnum):
    HOST = "host"
    NOTECARD = "notecard"

    def visit(self, host: typing.Callable[[], T_Result], notecard: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDeviceDfuStatusRequestFirmwareType.HOST:
            return host()
        if self is GetDeviceDfuStatusRequestFirmwareType.NOTECARD:
            return notecard()
