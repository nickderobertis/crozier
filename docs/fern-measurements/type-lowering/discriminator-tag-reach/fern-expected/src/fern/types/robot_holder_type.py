

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RobotHolderType(enum.StrEnum):
    ROBOT = "ROBOT"

    def visit(self, robot: typing.Callable[[], T_Result]) -> T_Result:
        if self is RobotHolderType.ROBOT:
            return robot()
