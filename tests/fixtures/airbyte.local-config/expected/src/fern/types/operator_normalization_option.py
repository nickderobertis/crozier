

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OperatorNormalizationOption(str, enum.Enum):
    BASIC = "basic"

    def visit(self, basic: typing.Callable[[], T_Result]) -> T_Result:
        if self is OperatorNormalizationOption.BASIC:
            return basic()
