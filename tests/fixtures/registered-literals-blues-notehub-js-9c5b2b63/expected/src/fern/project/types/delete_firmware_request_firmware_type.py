

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DeleteFirmwareRequestFirmwareType(enum.StrEnum):
    HOST = "host"

    def visit(self, host: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeleteFirmwareRequestFirmwareType.HOST:
            return host()
