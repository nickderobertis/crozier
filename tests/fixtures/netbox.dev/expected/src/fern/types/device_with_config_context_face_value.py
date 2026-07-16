

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DeviceWithConfigContextFaceValue(str, enum.Enum):
    FRONT = "front"
    REAR = "rear"

    def visit(self, front: typing.Callable[[], T_Result], rear: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeviceWithConfigContextFaceValue.FRONT:
            return front()
        if self is DeviceWithConfigContextFaceValue.REAR:
            return rear()
