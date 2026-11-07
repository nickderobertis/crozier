

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlanName(enum.StrEnum):
    """
    A plan defines how much CPU and memory is required to run an instance of your game server.

    `tiny`: shared core, 1gb memory

    `small`: 1 core, 2gb memory

    `medium`: 2 core, 4gb memory

    `large`: 4 core, 8gb memory
    """

    TINY = "tiny"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"

    def visit(
        self,
        tiny: typing.Callable[[], T_Result],
        small: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        large: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PlanName.TINY:
            return tiny()
        if self is PlanName.SMALL:
            return small()
        if self is PlanName.MEDIUM:
            return medium()
        if self is PlanName.LARGE:
            return large()
