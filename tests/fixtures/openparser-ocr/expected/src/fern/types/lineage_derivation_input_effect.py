

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LineageDerivationInputEffect(enum.StrEnum):
    DIRECT = "direct"
    INDIRECT = "indirect"

    def visit(self, direct: typing.Callable[[], T_Result], indirect: typing.Callable[[], T_Result]) -> T_Result:
        if self is LineageDerivationInputEffect.DIRECT:
            return direct()
        if self is LineageDerivationInputEffect.INDIRECT:
            return indirect()
