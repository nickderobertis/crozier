

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssemblySharedAssemblyType(enum.StrEnum):
    CLONING = "CLONING"
    CONCATENATION = "CONCATENATION"

    def visit(self, cloning: typing.Callable[[], T_Result], concatenation: typing.Callable[[], T_Result]) -> T_Result:
        if self is AssemblySharedAssemblyType.CLONING:
            return cloning()
        if self is AssemblySharedAssemblyType.CONCATENATION:
            return concatenation()
