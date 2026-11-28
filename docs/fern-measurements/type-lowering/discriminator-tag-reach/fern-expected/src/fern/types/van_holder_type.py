

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VanHolderType(enum.StrEnum):
    VAN = "VAN"

    def visit(self, van: typing.Callable[[], T_Result]) -> T_Result:
        if self is VanHolderType.VAN:
            return van()
