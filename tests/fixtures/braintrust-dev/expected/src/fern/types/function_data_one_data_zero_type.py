

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionDataOneDataZeroType(enum.StrEnum):
    BUNDLE = "bundle"

    def visit(self, bundle: typing.Callable[[], T_Result]) -> T_Result:
        if self is FunctionDataOneDataZeroType.BUNDLE:
            return bundle()
