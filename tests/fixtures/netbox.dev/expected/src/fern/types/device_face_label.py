

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DeviceFaceLabel(str, enum.Enum):
    FRONT = "Front"
    REAR = "Rear"

    def visit(self, front: typing.Callable[[], T_Result], rear: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeviceFaceLabel.FRONT:
            return front()
        if self is DeviceFaceLabel.REAR:
            return rear()
