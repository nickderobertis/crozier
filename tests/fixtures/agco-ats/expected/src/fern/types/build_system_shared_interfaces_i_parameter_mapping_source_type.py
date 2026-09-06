

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BuildSystemSharedInterfacesIParameterMappingSourceType(enum.StrEnum):
    """
    SourceType
    """

    CONSTANT = "Constant"
    VARIABLE = "Variable"

    def visit(self, constant: typing.Callable[[], T_Result], variable: typing.Callable[[], T_Result]) -> T_Result:
        if self is BuildSystemSharedInterfacesIParameterMappingSourceType.CONSTANT:
            return constant()
        if self is BuildSystemSharedInterfacesIParameterMappingSourceType.VARIABLE:
            return variable()
