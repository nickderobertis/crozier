

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DeviceFaceValue(str, enum.Enum):
    FRONT = "front"
    REAR = "rear"

    def visit(self, front: typing.Callable[[], T_Result], rear: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeviceFaceValue.FRONT:
            return front()
        if self is DeviceFaceValue.REAR:
            return rear()
