

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BuildSystemSharedDtoParameterValueDirection(enum.StrEnum):
    """
    The parameter direction (Input or Output)
    """

    INPUT = "Input"
    OUTPUT = "Output"

    def visit(self, input: typing.Callable[[], T_Result], output: typing.Callable[[], T_Result]) -> T_Result:
        if self is BuildSystemSharedDtoParameterValueDirection.INPUT:
            return input()
        if self is BuildSystemSharedDtoParameterValueDirection.OUTPUT:
            return output()
