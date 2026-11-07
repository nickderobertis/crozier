

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetActionsResponseActionsItemRequestsItemModbusType(enum.StrEnum):
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
        if self is GetActionsResponseActionsItemRequestsItemModbusType.HEX:
            return hex()
        if self is GetActionsResponseActionsItemRequestsItemModbusType.SHORT:
            return short()
        if self is GetActionsResponseActionsItemRequestsItemModbusType.INT:
            return int_()
        if self is GetActionsResponseActionsItemRequestsItemModbusType.LONG:
            return long_()
        if self is GetActionsResponseActionsItemRequestsItemModbusType.FLOAT:
            return float_()
        if self is GetActionsResponseActionsItemRequestsItemModbusType.DOUBLE:
            return double()
