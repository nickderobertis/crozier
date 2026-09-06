

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BuildSystemSharedDtoParameterDirection(enum.StrEnum):
    """
    The parameter direction (Input or Output)
    """

    INPUT = "Input"
    OUTPUT = "Output"

    def visit(self, input: typing.Callable[[], T_Result], output: typing.Callable[[], T_Result]) -> T_Result:
        if self is BuildSystemSharedDtoParameterDirection.INPUT:
            return input()
        if self is BuildSystemSharedDtoParameterDirection.OUTPUT:
            return output()
