

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetDevicesDfuStatusRequestFirmwareType(enum.StrEnum):
    HOST = "host"
    NOTECARD = "notecard"

    def visit(self, host: typing.Callable[[], T_Result], notecard: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDevicesDfuStatusRequestFirmwareType.HOST:
            return host()
        if self is GetDevicesDfuStatusRequestFirmwareType.NOTECARD:
            return notecard()
