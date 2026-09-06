

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionDataNullishSchemaType(enum.StrEnum):
    PARAMETERS = "parameters"

    def visit(self, parameters: typing.Callable[[], T_Result]) -> T_Result:
        if self is FunctionDataNullishSchemaType.PARAMETERS:
            return parameters()
