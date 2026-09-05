

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetProductRequestProductNameOne(enum.StrEnum):
    CURRENT = "current"

    def visit(self, current: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetProductRequestProductNameOne.CURRENT:
            return current()
