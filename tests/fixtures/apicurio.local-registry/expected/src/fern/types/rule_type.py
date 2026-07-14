

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class RuleType(str, enum.Enum):
    """ """

    VALIDITY = "VALIDITY"
    COMPATIBILITY = "COMPATIBILITY"

    def visit(self, validity: typing.Callable[[], T_Result], compatibility: typing.Callable[[], T_Result]) -> T_Result:
        if self is RuleType.VALIDITY:
            return validity()
        if self is RuleType.COMPATIBILITY:
            return compatibility()
