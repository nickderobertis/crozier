

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GroomingTaskAllOfAction(enum.StrEnum):
    """
    Groom a pet.
    """

    GROOMING = "grooming"

    def visit(self, grooming: typing.Callable[[], T_Result]) -> T_Result:
        if self is GroomingTaskAllOfAction.GROOMING:
            return grooming()
