

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeliveryChoiceOneMethod(enum.StrEnum):
    DOORSTEP = "doorstep"

    def visit(self, doorstep: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeliveryChoiceOneMethod.DOORSTEP:
            return doorstep()
