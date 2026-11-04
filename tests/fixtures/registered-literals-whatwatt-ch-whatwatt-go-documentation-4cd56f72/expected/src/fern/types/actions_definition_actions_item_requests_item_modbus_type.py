

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActionsDefinitionActionsItemRequestsItemModbusType(enum.StrEnum):
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
        if self is ActionsDefinitionActionsItemRequestsItemModbusType.HEX:
            return hex()
        if self is ActionsDefinitionActionsItemRequestsItemModbusType.SHORT:
            return short()
        if self is ActionsDefinitionActionsItemRequestsItemModbusType.INT:
            return int_()
        if self is ActionsDefinitionActionsItemRequestsItemModbusType.LONG:
            return long_()
        if self is ActionsDefinitionActionsItemRequestsItemModbusType.FLOAT:
            return float_()
        if self is ActionsDefinitionActionsItemRequestsItemModbusType.DOUBLE:
            return double()
