

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CrossingBoardingNoticePhase(enum.StrEnum):
    """
    Where the crossing stands.
    """

    BOARDING = "boarding"

    def visit(self, boarding: typing.Callable[[], T_Result]) -> T_Result:
        if self is CrossingBoardingNoticePhase.BOARDING:
            return boarding()
