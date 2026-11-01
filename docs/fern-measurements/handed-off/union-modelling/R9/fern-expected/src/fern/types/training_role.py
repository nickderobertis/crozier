

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TrainingRole(enum.StrEnum):
    TRAINEE = "trainee"
    MENTOR = "mentor"

    def visit(self, trainee: typing.Callable[[], T_Result], mentor: typing.Callable[[], T_Result]) -> T_Result:
        if self is TrainingRole.TRAINEE:
            return trainee()
        if self is TrainingRole.MENTOR:
            return mentor()
