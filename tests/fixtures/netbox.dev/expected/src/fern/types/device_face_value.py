

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeviceFaceValue(enum.StrEnum):
    FRONT = "front"
    REAR = "rear"

    def visit(self, front: typing.Callable[[], T_Result], rear: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeviceFaceValue.FRONT:
            return front()
        if self is DeviceFaceValue.REAR:
            return rear()
