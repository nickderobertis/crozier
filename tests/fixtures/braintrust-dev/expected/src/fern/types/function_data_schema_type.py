

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionDataSchemaType(enum.StrEnum):
    PARAMETERS = "parameters"

    def visit(self, parameters: typing.Callable[[], T_Result]) -> T_Result:
        if self is FunctionDataSchemaType.PARAMETERS:
            return parameters()
