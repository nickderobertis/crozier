

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OperatorNormalizationOption(enum.StrEnum):
    BASIC = "basic"

    def visit(self, basic: typing.Callable[[], T_Result]) -> T_Result:
        if self is OperatorNormalizationOption.BASIC:
            return basic()
