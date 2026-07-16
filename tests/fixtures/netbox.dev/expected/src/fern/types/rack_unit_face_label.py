

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class RackUnitFaceLabel(str, enum.Enum):
    FRONT = "Front"
    REAR = "Rear"

    def visit(self, front: typing.Callable[[], T_Result], rear: typing.Callable[[], T_Result]) -> T_Result:
        if self is RackUnitFaceLabel.FRONT:
            return front()
        if self is RackUnitFaceLabel.REAR:
            return rear()
