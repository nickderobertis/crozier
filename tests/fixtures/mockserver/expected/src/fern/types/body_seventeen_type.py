

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BodySeventeenType(enum.StrEnum):
    PARAMETERS = "PARAMETERS"

    def visit(self, parameters: typing.Callable[[], T_Result]) -> T_Result:
        if self is BodySeventeenType.PARAMETERS:
            return parameters()
