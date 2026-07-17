

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeviceWithConfigContextFaceLabel(enum.StrEnum):
    FRONT = "Front"
    REAR = "Rear"

    def visit(self, front: typing.Callable[[], T_Result], rear: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeviceWithConfigContextFaceLabel.FRONT:
            return front()
        if self is DeviceWithConfigContextFaceLabel.REAR:
            return rear()
