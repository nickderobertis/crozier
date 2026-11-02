

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Hull(enum.StrEnum):
    STEEL = "STEEL"
    TIMBER = "TIMBER"
    COMPOSITE = "COMPOSITE"

    def visit(
        self,
        steel: typing.Callable[[], T_Result],
        timber: typing.Callable[[], T_Result],
        composite: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Hull.STEEL:
            return steel()
        if self is Hull.TIMBER:
            return timber()
        if self is Hull.COMPOSITE:
            return composite()
