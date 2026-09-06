

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BuildSystemSharedDtoParameterMappingSourceType(enum.StrEnum):
    """
    The source type used for supplying the parameter
    """

    CONSTANT = "Constant"
    VARIABLE = "Variable"

    def visit(self, constant: typing.Callable[[], T_Result], variable: typing.Callable[[], T_Result]) -> T_Result:
        if self is BuildSystemSharedDtoParameterMappingSourceType.CONSTANT:
            return constant()
        if self is BuildSystemSharedDtoParameterMappingSourceType.VARIABLE:
            return variable()
