

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BuildSystemSharedInterfacesIParameterValueDirection(enum.StrEnum):
    """
    Gets or sets a value indicating whether the parameter value is an
                input to the build part or an output from the build part.
    """

    INPUT = "Input"
    OUTPUT = "Output"

    def visit(self, input: typing.Callable[[], T_Result], output: typing.Callable[[], T_Result]) -> T_Result:
        if self is BuildSystemSharedInterfacesIParameterValueDirection.INPUT:
            return input()
        if self is BuildSystemSharedInterfacesIParameterValueDirection.OUTPUT:
            return output()
