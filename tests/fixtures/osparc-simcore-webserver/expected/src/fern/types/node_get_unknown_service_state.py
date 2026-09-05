

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NodeGetUnknownServiceState(enum.StrEnum):
    UNKNOWN = "unknown"

    def visit(self, unknown: typing.Callable[[], T_Result]) -> T_Result:
        if self is NodeGetUnknownServiceState.UNKNOWN:
            return unknown()
