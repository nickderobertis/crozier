

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WeavePlanFinish(enum.StrEnum):
    """
    How the cloth is finished.
    """

    MATTE = "MATTE"
    GLOSS = "GLOSS"

    def visit(self, matte: typing.Callable[[], T_Result], gloss: typing.Callable[[], T_Result]) -> T_Result:
        if self is WeavePlanFinish.MATTE:
            return matte()
        if self is WeavePlanFinish.GLOSS:
            return gloss()
