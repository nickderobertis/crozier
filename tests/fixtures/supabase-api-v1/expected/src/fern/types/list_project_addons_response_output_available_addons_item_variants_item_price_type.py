

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemPriceType(enum.StrEnum):
    FIXED = "fixed"
    USAGE = "usage"

    def visit(self, fixed: typing.Callable[[], T_Result], usage: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemPriceType.FIXED:
            return fixed()
        if self is ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemPriceType.USAGE:
            return usage()
