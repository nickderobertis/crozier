

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RuleKind(enum.StrEnum):
    """
    Rule kind
    """

    TRANSFORM = "TRANSFORM"
    CONDITION = "CONDITION"

    def visit(self, transform: typing.Callable[[], T_Result], condition: typing.Callable[[], T_Result]) -> T_Result:
        if self is RuleKind.TRANSFORM:
            return transform()
        if self is RuleKind.CONDITION:
            return condition()
