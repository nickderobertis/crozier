

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthorizationCodesSharedModelsValidationFieldType(enum.StrEnum):
    """
    The type for this validation field.
    """

    BOOLEAN = "Boolean"
    FLOAT = "Float"
    INT = "Int"
    STRING_CASE_INSENSITIVE = "StringCaseInsensitive"
    STRING_CASE_SENSITIVE = "StringCaseSensitive"

    def visit(
        self,
        boolean: typing.Callable[[], T_Result],
        float_: typing.Callable[[], T_Result],
        int_: typing.Callable[[], T_Result],
        string_case_insensitive: typing.Callable[[], T_Result],
        string_case_sensitive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthorizationCodesSharedModelsValidationFieldType.BOOLEAN:
            return boolean()
        if self is AuthorizationCodesSharedModelsValidationFieldType.FLOAT:
            return float_()
        if self is AuthorizationCodesSharedModelsValidationFieldType.INT:
            return int_()
        if self is AuthorizationCodesSharedModelsValidationFieldType.STRING_CASE_INSENSITIVE:
            return string_case_insensitive()
        if self is AuthorizationCodesSharedModelsValidationFieldType.STRING_CASE_SENSITIVE:
            return string_case_sensitive()
