

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostV1ShapeRequestReplica(enum.StrEnum):
    DEFAULT = "default"
    FULL = "full"

    def visit(self, default: typing.Callable[[], T_Result], full: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostV1ShapeRequestReplica.DEFAULT:
            return default()
        if self is PostV1ShapeRequestReplica.FULL:
            return full()
