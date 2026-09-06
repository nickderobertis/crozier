

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthorizationCodesSharedModelsDataFieldType(enum.StrEnum):
    """
    The type of this data field.
    """

    BOOLEAN = "Boolean"
    DECIMAL = "Decimal"
    FLOAT = "Float"
    VARIABLE_LENGTH_BYTE_ARRAY = "VariableLengthByteArray"

    def visit(
        self,
        boolean: typing.Callable[[], T_Result],
        decimal: typing.Callable[[], T_Result],
        float_: typing.Callable[[], T_Result],
        variable_length_byte_array: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthorizationCodesSharedModelsDataFieldType.BOOLEAN:
            return boolean()
        if self is AuthorizationCodesSharedModelsDataFieldType.DECIMAL:
            return decimal()
        if self is AuthorizationCodesSharedModelsDataFieldType.FLOAT:
            return float_()
        if self is AuthorizationCodesSharedModelsDataFieldType.VARIABLE_LENGTH_BYTE_ARRAY:
            return variable_length_byte_array()
