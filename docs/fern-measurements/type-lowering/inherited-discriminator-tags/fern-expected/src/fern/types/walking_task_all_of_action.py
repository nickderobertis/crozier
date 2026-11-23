

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WalkingTaskAllOfAction(enum.StrEnum):
    """
    Walk a pet.
    """

    WALKING = "walking"

    def visit(self, walking: typing.Callable[[], T_Result]) -> T_Result:
        if self is WalkingTaskAllOfAction.WALKING:
            return walking()
