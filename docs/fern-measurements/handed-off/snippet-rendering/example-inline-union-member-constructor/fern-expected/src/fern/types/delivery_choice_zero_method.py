

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeliveryChoiceZeroMethod(enum.StrEnum):
    LOCKER = "locker"

    def visit(self, locker: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeliveryChoiceZeroMethod.LOCKER:
            return locker()
