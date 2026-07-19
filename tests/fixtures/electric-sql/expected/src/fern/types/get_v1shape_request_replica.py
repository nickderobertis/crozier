

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetV1ShapeRequestReplica(enum.StrEnum):
    DEFAULT = "default"
    FULL = "full"

    def visit(self, default: typing.Callable[[], T_Result], full: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetV1ShapeRequestReplica.DEFAULT:
            return default()
        if self is GetV1ShapeRequestReplica.FULL:
            return full()
