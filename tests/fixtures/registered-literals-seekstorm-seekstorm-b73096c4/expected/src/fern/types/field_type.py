

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FieldType(enum.StrEnum):
    """
    FieldType defines the type of a field in the document: u8, u16, u32, u64, i8, i16, i32, i64, f32, f64, point, string, stringset, text.
    """

    U8 = "U8"
    U16 = "U16"
    U32 = "U32"
    U64 = "U64"
    I8 = "I8"
    I16 = "I16"
    I32 = "I32"
    I64 = "I64"
    TIMESTAMP = "Timestamp"
    F32 = "F32"
    F64 = "F64"
    BOOL = "Bool"
    STRING16 = "String16"
    STRING32 = "String32"
    STRING_SET16 = "StringSet16"
    STRING_SET32 = "StringSet32"
    POINT = "Point"
    TEXT = "Text"
    JSON = "Json"
    BINARY = "Binary"

    def visit(
        self,
        u8: typing.Callable[[], T_Result],
        u16: typing.Callable[[], T_Result],
        u32: typing.Callable[[], T_Result],
        u64: typing.Callable[[], T_Result],
        i8: typing.Callable[[], T_Result],
        i16: typing.Callable[[], T_Result],
        i32: typing.Callable[[], T_Result],
        i64: typing.Callable[[], T_Result],
        timestamp: typing.Callable[[], T_Result],
        f32: typing.Callable[[], T_Result],
        f64: typing.Callable[[], T_Result],
        bool_: typing.Callable[[], T_Result],
        string16: typing.Callable[[], T_Result],
        string32: typing.Callable[[], T_Result],
        string_set16: typing.Callable[[], T_Result],
        string_set32: typing.Callable[[], T_Result],
        point: typing.Callable[[], T_Result],
        text: typing.Callable[[], T_Result],
        json: typing.Callable[[], T_Result],
        binary: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FieldType.U8:
            return u8()
        if self is FieldType.U16:
            return u16()
        if self is FieldType.U32:
            return u32()
        if self is FieldType.U64:
            return u64()
        if self is FieldType.I8:
            return i8()
        if self is FieldType.I16:
            return i16()
        if self is FieldType.I32:
            return i32()
        if self is FieldType.I64:
            return i64()
        if self is FieldType.TIMESTAMP:
            return timestamp()
        if self is FieldType.F32:
            return f32()
        if self is FieldType.F64:
            return f64()
        if self is FieldType.BOOL:
            return bool_()
        if self is FieldType.STRING16:
            return string16()
        if self is FieldType.STRING32:
            return string32()
        if self is FieldType.STRING_SET16:
            return string_set16()
        if self is FieldType.STRING_SET32:
            return string_set32()
        if self is FieldType.POINT:
            return point()
        if self is FieldType.TEXT:
            return text()
        if self is FieldType.JSON:
            return json()
        if self is FieldType.BINARY:
            return binary()
