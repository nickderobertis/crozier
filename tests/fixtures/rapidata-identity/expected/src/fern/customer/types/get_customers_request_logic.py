

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCustomersRequestLogic(enum.StrEnum):
    AND = "and"
    OR = "or"

    def visit(self, and_: typing.Callable[[], T_Result], or_: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetCustomersRequestLogic.AND:
            return and_()
        if self is GetCustomersRequestLogic.OR:
            return or_()
