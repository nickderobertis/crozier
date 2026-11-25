

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Finish(enum.StrEnum):
    MATTE = "matte"
    SATIN = "satin"
    GLOSS = "gloss"

    def visit(
        self,
        matte: typing.Callable[[], T_Result],
        satin: typing.Callable[[], T_Result],
        gloss: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Finish.MATTE:
            return matte()
        if self is Finish.SATIN:
            return satin()
        if self is Finish.GLOSS:
            return gloss()
