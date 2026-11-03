

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HerbKind(enum.StrEnum):
    HERB = "herb"

    def visit(self, herb: typing.Callable[[], T_Result]) -> T_Result:
        if self is HerbKind.HERB:
            return herb()
