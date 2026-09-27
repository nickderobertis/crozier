

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BodyFiveType(enum.StrEnum):
    PARAMETERS = "PARAMETERS"

    def visit(self, parameters: typing.Callable[[], T_Result]) -> T_Result:
        if self is BodyFiveType.PARAMETERS:
            return parameters()
