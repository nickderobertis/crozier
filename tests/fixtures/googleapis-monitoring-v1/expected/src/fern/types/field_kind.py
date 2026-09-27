

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FieldKind(enum.StrEnum):
    """
    The field type.
    """

    TYPE_UNKNOWN = "TYPE_UNKNOWN"
    TYPE_DOUBLE = "TYPE_DOUBLE"
    TYPE_FLOAT = "TYPE_FLOAT"
    TYPE_INT64 = "TYPE_INT64"
    TYPE_UINT64 = "TYPE_UINT64"
    TYPE_INT32 = "TYPE_INT32"
    TYPE_FIXED64 = "TYPE_FIXED64"
    TYPE_FIXED32 = "TYPE_FIXED32"
    TYPE_BOOL = "TYPE_BOOL"
    TYPE_STRING = "TYPE_STRING"
    TYPE_GROUP = "TYPE_GROUP"
    TYPE_MESSAGE = "TYPE_MESSAGE"
    TYPE_BYTES = "TYPE_BYTES"
    TYPE_UINT32 = "TYPE_UINT32"
    TYPE_ENUM = "TYPE_ENUM"
    TYPE_SFIXED32 = "TYPE_SFIXED32"
    TYPE_SFIXED64 = "TYPE_SFIXED64"
    TYPE_SINT32 = "TYPE_SINT32"
    TYPE_SINT64 = "TYPE_SINT64"

    def visit(
        self,
        type_unknown: typing.Callable[[], T_Result],
        type_double: typing.Callable[[], T_Result],
        type_float: typing.Callable[[], T_Result],
        type_int64: typing.Callable[[], T_Result],
        type_uint64: typing.Callable[[], T_Result],
        type_int32: typing.Callable[[], T_Result],
        type_fixed64: typing.Callable[[], T_Result],
        type_fixed32: typing.Callable[[], T_Result],
        type_bool: typing.Callable[[], T_Result],
        type_string: typing.Callable[[], T_Result],
        type_group: typing.Callable[[], T_Result],
        type_message: typing.Callable[[], T_Result],
        type_bytes: typing.Callable[[], T_Result],
        type_uint32: typing.Callable[[], T_Result],
        type_enum: typing.Callable[[], T_Result],
        type_sfixed32: typing.Callable[[], T_Result],
        type_sfixed64: typing.Callable[[], T_Result],
        type_sint32: typing.Callable[[], T_Result],
        type_sint64: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FieldKind.TYPE_UNKNOWN:
            return type_unknown()
        if self is FieldKind.TYPE_DOUBLE:
            return type_double()
        if self is FieldKind.TYPE_FLOAT:
            return type_float()
        if self is FieldKind.TYPE_INT64:
            return type_int64()
        if self is FieldKind.TYPE_UINT64:
            return type_uint64()
        if self is FieldKind.TYPE_INT32:
            return type_int32()
        if self is FieldKind.TYPE_FIXED64:
            return type_fixed64()
        if self is FieldKind.TYPE_FIXED32:
            return type_fixed32()
        if self is FieldKind.TYPE_BOOL:
            return type_bool()
        if self is FieldKind.TYPE_STRING:
            return type_string()
        if self is FieldKind.TYPE_GROUP:
            return type_group()
        if self is FieldKind.TYPE_MESSAGE:
            return type_message()
        if self is FieldKind.TYPE_BYTES:
            return type_bytes()
        if self is FieldKind.TYPE_UINT32:
            return type_uint32()
        if self is FieldKind.TYPE_ENUM:
            return type_enum()
        if self is FieldKind.TYPE_SFIXED32:
            return type_sfixed32()
        if self is FieldKind.TYPE_SFIXED64:
            return type_sfixed64()
        if self is FieldKind.TYPE_SINT32:
            return type_sint32()
        if self is FieldKind.TYPE_SINT64:
            return type_sint64()
