

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OrderPrintRequestFinish(enum.StrEnum):
    NONE = "none"
    MATTE = "matte"
    GLOSS = "gloss"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        matte: typing.Callable[[], T_Result],
        gloss: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OrderPrintRequestFinish.NONE:
            return none()
        if self is OrderPrintRequestFinish.MATTE:
            return matte()
        if self is OrderPrintRequestFinish.GLOSS:
            return gloss()
