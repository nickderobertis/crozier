

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateFirmwareRequestFirmwareType(enum.StrEnum):
    HOST = "host"

    def visit(self, host: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateFirmwareRequestFirmwareType.HOST:
            return host()
