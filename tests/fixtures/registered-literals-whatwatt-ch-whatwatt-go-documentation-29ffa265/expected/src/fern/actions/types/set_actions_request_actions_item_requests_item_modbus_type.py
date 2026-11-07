

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SetActionsRequestActionsItemRequestsItemModbusType(enum.StrEnum):
    HEX = "hex"
    SHORT = "short"
    INT = "int"
    LONG = "long"
    FLOAT = "float"
    DOUBLE = "double"

    def visit(
        self,
        hex: typing.Callable[[], T_Result],
        short: typing.Callable[[], T_Result],
        int_: typing.Callable[[], T_Result],
        long_: typing.Callable[[], T_Result],
        float_: typing.Callable[[], T_Result],
        double: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SetActionsRequestActionsItemRequestsItemModbusType.HEX:
            return hex()
        if self is SetActionsRequestActionsItemRequestsItemModbusType.SHORT:
            return short()
        if self is SetActionsRequestActionsItemRequestsItemModbusType.INT:
            return int_()
        if self is SetActionsRequestActionsItemRequestsItemModbusType.LONG:
            return long_()
        if self is SetActionsRequestActionsItemRequestsItemModbusType.FLOAT:
            return float_()
        if self is SetActionsRequestActionsItemRequestsItemModbusType.DOUBLE:
            return double()
