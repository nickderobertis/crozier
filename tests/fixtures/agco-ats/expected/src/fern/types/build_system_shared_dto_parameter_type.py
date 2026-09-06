

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BuildSystemSharedDtoParameterType(enum.StrEnum):
    """
    The data type of the parameter
    """

    STRING = "String"
    BOOLEAN = "Boolean"
    INTEGER = "Integer"
    FLOAT = "Float"
    STRING_DICTIONARY = "StringDictionary"

    def visit(
        self,
        string: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
        integer: typing.Callable[[], T_Result],
        float_: typing.Callable[[], T_Result],
        string_dictionary: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BuildSystemSharedDtoParameterType.STRING:
            return string()
        if self is BuildSystemSharedDtoParameterType.BOOLEAN:
            return boolean()
        if self is BuildSystemSharedDtoParameterType.INTEGER:
            return integer()
        if self is BuildSystemSharedDtoParameterType.FLOAT:
            return float_()
        if self is BuildSystemSharedDtoParameterType.STRING_DICTIONARY:
            return string_dictionary()
