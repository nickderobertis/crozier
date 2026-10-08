

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InlineResponse2003DefinitionWidth(enum.StrEnum):
    """
    The width of a configuration value
    """

    NONE = "NONE"
    SHORT = "SHORT"
    MEDIUM = "MEDIUM"
    LONG = "LONG"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        short: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        long_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InlineResponse2003DefinitionWidth.NONE:
            return none()
        if self is InlineResponse2003DefinitionWidth.SHORT:
            return short()
        if self is InlineResponse2003DefinitionWidth.MEDIUM:
            return medium()
        if self is InlineResponse2003DefinitionWidth.LONG:
            return long_()
