

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SpellComponentsItem(enum.StrEnum):
    V = "V"
    S = "S"
    M = "M"

    def visit(
        self, v: typing.Callable[[], T_Result], s: typing.Callable[[], T_Result], m: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is SpellComponentsItem.V:
            return v()
        if self is SpellComponentsItem.S:
            return s()
        if self is SpellComponentsItem.M:
            return m()
