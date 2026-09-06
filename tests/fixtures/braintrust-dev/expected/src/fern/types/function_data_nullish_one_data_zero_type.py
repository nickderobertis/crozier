

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionDataNullishOneDataZeroType(enum.StrEnum):
    BUNDLE = "bundle"

    def visit(self, bundle: typing.Callable[[], T_Result]) -> T_Result:
        if self is FunctionDataNullishOneDataZeroType.BUNDLE:
            return bundle()
