

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GiftCardType(enum.StrEnum):
    """ """

    PHYSICAL = "PHYSICAL"
    DIGITAL = "DIGITAL"

    def visit(self, physical: typing.Callable[[], T_Result], digital: typing.Callable[[], T_Result]) -> T_Result:
        if self is GiftCardType.PHYSICAL:
            return physical()
        if self is GiftCardType.DIGITAL:
            return digital()
