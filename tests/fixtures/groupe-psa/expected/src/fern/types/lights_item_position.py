

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LightsItemPosition(enum.StrEnum):
    FRONT = "Front"
    REAR = "Rear"

    def visit(self, front: typing.Callable[[], T_Result], rear: typing.Callable[[], T_Result]) -> T_Result:
        if self is LightsItemPosition.FRONT:
            return front()
        if self is LightsItemPosition.REAR:
            return rear()
