

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OutputParameterParameterType(enum.StrEnum):
    OUTPUT = "output"

    def visit(self, output: typing.Callable[[], T_Result]) -> T_Result:
        if self is OutputParameterParameterType.OUTPUT:
            return output()
