

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoDataframeSearchInputDefSchema0Type(enum.StrEnum):
    GROUP = "group"

    def visit(self, group: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarimoDataframeSearchInputDefSchema0Type.GROUP:
            return group()
