

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionRoleReclassifyExpectedRoleEight(enum.StrEnum):
    HAIR_FRONT = "hair-front"

    def visit(self, hair_front: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionRoleReclassifyExpectedRoleEight.HAIR_FRONT:
            return hair_front()
