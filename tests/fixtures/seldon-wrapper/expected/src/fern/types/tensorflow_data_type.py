

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TensorflowDataType(enum.StrEnum):
    """
    - DT_INVALID: Not a legal value for DataType.  Used to indicate a DataType field
    has not been set.
     - DT_FLOAT: Data types that all computation devices are expected to be
    capable to support.
     - DT_FLOAT_REF: Do not use!  These are only for parameters.  Every enum above
    should have a corresponding value below (verified by types_test).
    """

    DT_INVALID = "DT_INVALID"
    DT_FLOAT = "DT_FLOAT"
    DT_DOUBLE = "DT_DOUBLE"
    DT_INT32 = "DT_INT32"
    DT_UINT8 = "DT_UINT8"
    DT_INT16 = "DT_INT16"
    DT_INT8 = "DT_INT8"
    DT_STRING = "DT_STRING"
    DT_COMPLEX64 = "DT_COMPLEX64"
    DT_INT64 = "DT_INT64"
    DT_BOOL = "DT_BOOL"
    DT_QINT8 = "DT_QINT8"
    DT_QUINT8 = "DT_QUINT8"
    DT_QINT32 = "DT_QINT32"
    DT_BFLOAT16 = "DT_BFLOAT16"
    DT_QINT16 = "DT_QINT16"
    DT_QUINT16 = "DT_QUINT16"
    DT_UINT16 = "DT_UINT16"
    DT_COMPLEX128 = "DT_COMPLEX128"
    DT_HALF = "DT_HALF"
    DT_RESOURCE = "DT_RESOURCE"
    DT_VARIANT = "DT_VARIANT"
    DT_UINT32 = "DT_UINT32"
    DT_UINT64 = "DT_UINT64"
    DT_FLOAT_REF = "DT_FLOAT_REF"
    DT_DOUBLE_REF = "DT_DOUBLE_REF"
    DT_INT32REF = "DT_INT32_REF"
    DT_UINT8REF = "DT_UINT8_REF"
    DT_INT16REF = "DT_INT16_REF"
    DT_INT8REF = "DT_INT8_REF"
    DT_STRING_REF = "DT_STRING_REF"
    DT_COMPLEX64REF = "DT_COMPLEX64_REF"
    DT_INT64REF = "DT_INT64_REF"
    DT_BOOL_REF = "DT_BOOL_REF"
    DT_QINT8REF = "DT_QINT8_REF"
    DT_QUINT8REF = "DT_QUINT8_REF"
    DT_QINT32REF = "DT_QINT32_REF"
    DT_BFLOAT16REF = "DT_BFLOAT16_REF"
    DT_QINT16REF = "DT_QINT16_REF"
    DT_QUINT16REF = "DT_QUINT16_REF"
    DT_UINT16REF = "DT_UINT16_REF"
    DT_COMPLEX128REF = "DT_COMPLEX128_REF"
    DT_HALF_REF = "DT_HALF_REF"
    DT_RESOURCE_REF = "DT_RESOURCE_REF"
    DT_VARIANT_REF = "DT_VARIANT_REF"
    DT_UINT32REF = "DT_UINT32_REF"
    DT_UINT64REF = "DT_UINT64_REF"

    def visit(
        self,
        dt_invalid: typing.Callable[[], T_Result],
        dt_float: typing.Callable[[], T_Result],
        dt_double: typing.Callable[[], T_Result],
        dt_int32: typing.Callable[[], T_Result],
        dt_uint8: typing.Callable[[], T_Result],
        dt_int16: typing.Callable[[], T_Result],
        dt_int8: typing.Callable[[], T_Result],
        dt_string: typing.Callable[[], T_Result],
        dt_complex64: typing.Callable[[], T_Result],
        dt_int64: typing.Callable[[], T_Result],
        dt_bool: typing.Callable[[], T_Result],
        dt_qint8: typing.Callable[[], T_Result],
        dt_quint8: typing.Callable[[], T_Result],
        dt_qint32: typing.Callable[[], T_Result],
        dt_bfloat16: typing.Callable[[], T_Result],
        dt_qint16: typing.Callable[[], T_Result],
        dt_quint16: typing.Callable[[], T_Result],
        dt_uint16: typing.Callable[[], T_Result],
        dt_complex128: typing.Callable[[], T_Result],
        dt_half: typing.Callable[[], T_Result],
        dt_resource: typing.Callable[[], T_Result],
        dt_variant: typing.Callable[[], T_Result],
        dt_uint32: typing.Callable[[], T_Result],
        dt_uint64: typing.Callable[[], T_Result],
        dt_float_ref: typing.Callable[[], T_Result],
        dt_double_ref: typing.Callable[[], T_Result],
        dt_int32ref: typing.Callable[[], T_Result],
        dt_uint8ref: typing.Callable[[], T_Result],
        dt_int16ref: typing.Callable[[], T_Result],
        dt_int8ref: typing.Callable[[], T_Result],
        dt_string_ref: typing.Callable[[], T_Result],
        dt_complex64ref: typing.Callable[[], T_Result],
        dt_int64ref: typing.Callable[[], T_Result],
        dt_bool_ref: typing.Callable[[], T_Result],
        dt_qint8ref: typing.Callable[[], T_Result],
        dt_quint8ref: typing.Callable[[], T_Result],
        dt_qint32ref: typing.Callable[[], T_Result],
        dt_bfloat16ref: typing.Callable[[], T_Result],
        dt_qint16ref: typing.Callable[[], T_Result],
        dt_quint16ref: typing.Callable[[], T_Result],
        dt_uint16ref: typing.Callable[[], T_Result],
        dt_complex128ref: typing.Callable[[], T_Result],
        dt_half_ref: typing.Callable[[], T_Result],
        dt_resource_ref: typing.Callable[[], T_Result],
        dt_variant_ref: typing.Callable[[], T_Result],
        dt_uint32ref: typing.Callable[[], T_Result],
        dt_uint64ref: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TensorflowDataType.DT_INVALID:
            return dt_invalid()
        if self is TensorflowDataType.DT_FLOAT:
            return dt_float()
        if self is TensorflowDataType.DT_DOUBLE:
            return dt_double()
        if self is TensorflowDataType.DT_INT32:
            return dt_int32()
        if self is TensorflowDataType.DT_UINT8:
            return dt_uint8()
        if self is TensorflowDataType.DT_INT16:
            return dt_int16()
        if self is TensorflowDataType.DT_INT8:
            return dt_int8()
        if self is TensorflowDataType.DT_STRING:
            return dt_string()
        if self is TensorflowDataType.DT_COMPLEX64:
            return dt_complex64()
        if self is TensorflowDataType.DT_INT64:
            return dt_int64()
        if self is TensorflowDataType.DT_BOOL:
            return dt_bool()
        if self is TensorflowDataType.DT_QINT8:
            return dt_qint8()
        if self is TensorflowDataType.DT_QUINT8:
            return dt_quint8()
        if self is TensorflowDataType.DT_QINT32:
            return dt_qint32()
        if self is TensorflowDataType.DT_BFLOAT16:
            return dt_bfloat16()
        if self is TensorflowDataType.DT_QINT16:
            return dt_qint16()
        if self is TensorflowDataType.DT_QUINT16:
            return dt_quint16()
        if self is TensorflowDataType.DT_UINT16:
            return dt_uint16()
        if self is TensorflowDataType.DT_COMPLEX128:
            return dt_complex128()
        if self is TensorflowDataType.DT_HALF:
            return dt_half()
        if self is TensorflowDataType.DT_RESOURCE:
            return dt_resource()
        if self is TensorflowDataType.DT_VARIANT:
            return dt_variant()
        if self is TensorflowDataType.DT_UINT32:
            return dt_uint32()
        if self is TensorflowDataType.DT_UINT64:
            return dt_uint64()
        if self is TensorflowDataType.DT_FLOAT_REF:
            return dt_float_ref()
        if self is TensorflowDataType.DT_DOUBLE_REF:
            return dt_double_ref()
        if self is TensorflowDataType.DT_INT32REF:
            return dt_int32ref()
        if self is TensorflowDataType.DT_UINT8REF:
            return dt_uint8ref()
        if self is TensorflowDataType.DT_INT16REF:
            return dt_int16ref()
        if self is TensorflowDataType.DT_INT8REF:
            return dt_int8ref()
        if self is TensorflowDataType.DT_STRING_REF:
            return dt_string_ref()
        if self is TensorflowDataType.DT_COMPLEX64REF:
            return dt_complex64ref()
        if self is TensorflowDataType.DT_INT64REF:
            return dt_int64ref()
        if self is TensorflowDataType.DT_BOOL_REF:
            return dt_bool_ref()
        if self is TensorflowDataType.DT_QINT8REF:
            return dt_qint8ref()
        if self is TensorflowDataType.DT_QUINT8REF:
            return dt_quint8ref()
        if self is TensorflowDataType.DT_QINT32REF:
            return dt_qint32ref()
        if self is TensorflowDataType.DT_BFLOAT16REF:
            return dt_bfloat16ref()
        if self is TensorflowDataType.DT_QINT16REF:
            return dt_qint16ref()
        if self is TensorflowDataType.DT_QUINT16REF:
            return dt_quint16ref()
        if self is TensorflowDataType.DT_UINT16REF:
            return dt_uint16ref()
        if self is TensorflowDataType.DT_COMPLEX128REF:
            return dt_complex128ref()
        if self is TensorflowDataType.DT_HALF_REF:
            return dt_half_ref()
        if self is TensorflowDataType.DT_RESOURCE_REF:
            return dt_resource_ref()
        if self is TensorflowDataType.DT_VARIANT_REF:
            return dt_variant_ref()
        if self is TensorflowDataType.DT_UINT32REF:
            return dt_uint32ref()
        if self is TensorflowDataType.DT_UINT64REF:
            return dt_uint64ref()
