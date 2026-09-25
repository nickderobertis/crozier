

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CollisionDetailsSide(enum.StrEnum):
    """
    Indicates the side of the collision
    """

    FRONT = "Front"
    REAR = "Rear"
    LATERAL = "Lateral"

    def visit(
        self,
        front: typing.Callable[[], T_Result],
        rear: typing.Callable[[], T_Result],
        lateral: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CollisionDetailsSide.FRONT:
            return front()
        if self is CollisionDetailsSide.REAR:
            return rear()
        if self is CollisionDetailsSide.LATERAL:
            return lateral()
