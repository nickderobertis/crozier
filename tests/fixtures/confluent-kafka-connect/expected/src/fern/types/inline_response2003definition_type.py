

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InlineResponse2003DefinitionType(enum.StrEnum):
    """
    The config types
    """

    NONE = "NONE"
    BOOLEAN = "BOOLEAN"
    INT = "INT"
    SHORT = "SHORT"
    LONG = "LONG"
    DOUBLE = "DOUBLE"
    STRING = "STRING"
    LIST = "LIST"
    ENUM = "ENUM"
    PASSWORD = "PASSWORD"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
        int_: typing.Callable[[], T_Result],
        short: typing.Callable[[], T_Result],
        long_: typing.Callable[[], T_Result],
        double: typing.Callable[[], T_Result],
        string: typing.Callable[[], T_Result],
        list_: typing.Callable[[], T_Result],
        enum: typing.Callable[[], T_Result],
        password: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InlineResponse2003DefinitionType.NONE:
            return none()
        if self is InlineResponse2003DefinitionType.BOOLEAN:
            return boolean()
        if self is InlineResponse2003DefinitionType.INT:
            return int_()
        if self is InlineResponse2003DefinitionType.SHORT:
            return short()
        if self is InlineResponse2003DefinitionType.LONG:
            return long_()
        if self is InlineResponse2003DefinitionType.DOUBLE:
            return double()
        if self is InlineResponse2003DefinitionType.STRING:
            return string()
        if self is InlineResponse2003DefinitionType.LIST:
            return list_()
        if self is InlineResponse2003DefinitionType.ENUM:
            return enum()
        if self is InlineResponse2003DefinitionType.PASSWORD:
            return password()
