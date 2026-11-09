

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IndexConfigurationDtoDecision(enum.StrEnum):
    NO_ACCESS = "NO_ACCESS"
    FULL_ACCESS = "FULL_ACCESS"
    PARTIAL_ACCESS = "PARTIAL_ACCESS"
    NOT_FOUND = "NOT_FOUND"

    def visit(
        self,
        no_access: typing.Callable[[], T_Result],
        full_access: typing.Callable[[], T_Result],
        partial_access: typing.Callable[[], T_Result],
        not_found: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IndexConfigurationDtoDecision.NO_ACCESS:
            return no_access()
        if self is IndexConfigurationDtoDecision.FULL_ACCESS:
            return full_access()
        if self is IndexConfigurationDtoDecision.PARTIAL_ACCESS:
            return partial_access()
        if self is IndexConfigurationDtoDecision.NOT_FOUND:
            return not_found()
