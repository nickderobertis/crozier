

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ValueMapsTypeReferencesValue(enum.StrEnum):
    STRING = "STRING"
    BYTE = "BYTE"
    DOUBLE = "DOUBLE"
    INTEGER = "INTEGER"
    BIG_DECIMAL = "BIG_DECIMAL"
    UNBOUND_DECIMAL = "UNBOUND_DECIMAL"
    BIG_INTEGER = "BIG_INTEGER"
    UNBOUND_INTEGER = "UNBOUND_INTEGER"
    BOOLEAN = "BOOLEAN"
    LOCAL_DATE = "LOCAL_DATE"
    LOCAL_DATE_TIME = "LOCAL_DATE_TIME"
    SHORT = "SHORT"
    CHARACTER = "CHARACTER"
    LONG = "LONG"
    FLOAT = "FLOAT"
    ZONED_DATE_TIME = "ZONED_DATE_TIME"
    YEAR = "YEAR"
    YEAR_MONTH = "YEAR_MONTH"
    LOCAL_TIME = "LOCAL_TIME"
    TIME_UUID_TYPE = "TIME_UUID_TYPE"
    UUID_TYPE = "UUID_TYPE"
    BYTE_ARRAY = "BYTE_ARRAY"
    NULL = "NULL"
    OBJECT = "OBJECT"
    ARRAY = "ARRAY"
    ARRAY_ELEMENT = "ARRAY_ELEMENT"
    TYPE_REFERENCE = "TYPE_REFERENCE"
    POLYMORPHIC = "POLYMORPHIC"

    def visit(
        self,
        string: typing.Callable[[], T_Result],
        byte: typing.Callable[[], T_Result],
        double: typing.Callable[[], T_Result],
        integer: typing.Callable[[], T_Result],
        big_decimal: typing.Callable[[], T_Result],
        unbound_decimal: typing.Callable[[], T_Result],
        big_integer: typing.Callable[[], T_Result],
        unbound_integer: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
        local_date: typing.Callable[[], T_Result],
        local_date_time: typing.Callable[[], T_Result],
        short: typing.Callable[[], T_Result],
        character: typing.Callable[[], T_Result],
        long_: typing.Callable[[], T_Result],
        float_: typing.Callable[[], T_Result],
        zoned_date_time: typing.Callable[[], T_Result],
        year: typing.Callable[[], T_Result],
        year_month: typing.Callable[[], T_Result],
        local_time: typing.Callable[[], T_Result],
        time_uuid_type: typing.Callable[[], T_Result],
        uuid_type: typing.Callable[[], T_Result],
        byte_array: typing.Callable[[], T_Result],
        null: typing.Callable[[], T_Result],
        object: typing.Callable[[], T_Result],
        array: typing.Callable[[], T_Result],
        array_element: typing.Callable[[], T_Result],
        type_reference: typing.Callable[[], T_Result],
        polymorphic: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ValueMapsTypeReferencesValue.STRING:
            return string()
        if self is ValueMapsTypeReferencesValue.BYTE:
            return byte()
        if self is ValueMapsTypeReferencesValue.DOUBLE:
            return double()
        if self is ValueMapsTypeReferencesValue.INTEGER:
            return integer()
        if self is ValueMapsTypeReferencesValue.BIG_DECIMAL:
            return big_decimal()
        if self is ValueMapsTypeReferencesValue.UNBOUND_DECIMAL:
            return unbound_decimal()
        if self is ValueMapsTypeReferencesValue.BIG_INTEGER:
            return big_integer()
        if self is ValueMapsTypeReferencesValue.UNBOUND_INTEGER:
            return unbound_integer()
        if self is ValueMapsTypeReferencesValue.BOOLEAN:
            return boolean()
        if self is ValueMapsTypeReferencesValue.LOCAL_DATE:
            return local_date()
        if self is ValueMapsTypeReferencesValue.LOCAL_DATE_TIME:
            return local_date_time()
        if self is ValueMapsTypeReferencesValue.SHORT:
            return short()
        if self is ValueMapsTypeReferencesValue.CHARACTER:
            return character()
        if self is ValueMapsTypeReferencesValue.LONG:
            return long_()
        if self is ValueMapsTypeReferencesValue.FLOAT:
            return float_()
        if self is ValueMapsTypeReferencesValue.ZONED_DATE_TIME:
            return zoned_date_time()
        if self is ValueMapsTypeReferencesValue.YEAR:
            return year()
        if self is ValueMapsTypeReferencesValue.YEAR_MONTH:
            return year_month()
        if self is ValueMapsTypeReferencesValue.LOCAL_TIME:
            return local_time()
        if self is ValueMapsTypeReferencesValue.TIME_UUID_TYPE:
            return time_uuid_type()
        if self is ValueMapsTypeReferencesValue.UUID_TYPE:
            return uuid_type()
        if self is ValueMapsTypeReferencesValue.BYTE_ARRAY:
            return byte_array()
        if self is ValueMapsTypeReferencesValue.NULL:
            return null()
        if self is ValueMapsTypeReferencesValue.OBJECT:
            return object()
        if self is ValueMapsTypeReferencesValue.ARRAY:
            return array()
        if self is ValueMapsTypeReferencesValue.ARRAY_ELEMENT:
            return array_element()
        if self is ValueMapsTypeReferencesValue.TYPE_REFERENCE:
            return type_reference()
        if self is ValueMapsTypeReferencesValue.POLYMORPHIC:
            return polymorphic()
