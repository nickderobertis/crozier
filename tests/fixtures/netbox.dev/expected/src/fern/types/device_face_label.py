

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeviceFaceLabel(enum.StrEnum):
    FRONT = "Front"
    REAR = "Rear"

    def visit(self, front: typing.Callable[[], T_Result], rear: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeviceFaceLabel.FRONT:
            return front()
        if self is DeviceFaceLabel.REAR:
            return rear()
