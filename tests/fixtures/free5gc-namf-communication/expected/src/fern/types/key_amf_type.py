

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class KeyAmfType(enum.StrEnum):
    KAMF = "KAMF"
    KPRIMEAMF = "KPRIMEAMF"

    def visit(self, kamf: typing.Callable[[], T_Result], kprimeamf: typing.Callable[[], T_Result]) -> T_Result:
        if self is KeyAmfType.KAMF:
            return kamf()
        if self is KeyAmfType.KPRIMEAMF:
            return kprimeamf()
