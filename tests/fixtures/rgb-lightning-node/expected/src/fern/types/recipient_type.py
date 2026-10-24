

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RecipientType(enum.StrEnum):
    BLIND = "Blind"
    WITNESS = "Witness"

    def visit(self, blind: typing.Callable[[], T_Result], witness: typing.Callable[[], T_Result]) -> T_Result:
        if self is RecipientType.BLIND:
            return blind()
        if self is RecipientType.WITNESS:
            return witness()
