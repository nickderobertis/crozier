

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeliveryModel(enum.StrEnum):
    GROW2_7_LEAF = "grow-2-7-leaf"
    AGENT412LARGE = "agent-4-12-large"
    PLAIN2A = "plain-2a"
    PLAIN0304 = "plain_03_04"
    UNIT20240701 = "unit-2024-07-01"

    def visit(
        self,
        grow2_7_leaf: typing.Callable[[], T_Result],
        agent412large: typing.Callable[[], T_Result],
        plain2a: typing.Callable[[], T_Result],
        plain0304: typing.Callable[[], T_Result],
        unit20240701: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DeliveryModel.GROW2_7_LEAF:
            return grow2_7_leaf()
        if self is DeliveryModel.AGENT412LARGE:
            return agent412large()
        if self is DeliveryModel.PLAIN2A:
            return plain2a()
        if self is DeliveryModel.PLAIN0304:
            return plain0304()
        if self is DeliveryModel.UNIT20240701:
            return unit20240701()
