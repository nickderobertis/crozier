

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemNineteenOp(enum.StrEnum):
    ADD = "add"

    def visit(self, add: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemNineteenOp.ADD:
            return add()
