

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CastingDeviceProtocol(enum.StrEnum):
    DLNA = "dlna"

    def visit(self, dlna: typing.Callable[[], T_Result]) -> T_Result:
        if self is CastingDeviceProtocol.DLNA:
            return dlna()
