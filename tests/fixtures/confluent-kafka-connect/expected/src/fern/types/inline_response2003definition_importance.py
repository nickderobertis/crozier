

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InlineResponse2003DefinitionImportance(enum.StrEnum):
    """
    The importance level for a configuration
    """

    NONE = "NONE"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InlineResponse2003DefinitionImportance.NONE:
            return none()
        if self is InlineResponse2003DefinitionImportance.HIGH:
            return high()
        if self is InlineResponse2003DefinitionImportance.MEDIUM:
            return medium()
        if self is InlineResponse2003DefinitionImportance.LOW:
            return low()
