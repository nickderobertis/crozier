

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RetouchPhotoRequestOptionsFinish(enum.StrEnum):
    MATTE = "matte"
    GLOSS = "gloss"

    def visit(self, matte: typing.Callable[[], T_Result], gloss: typing.Callable[[], T_Result]) -> T_Result:
        if self is RetouchPhotoRequestOptionsFinish.MATTE:
            return matte()
        if self is RetouchPhotoRequestOptionsFinish.GLOSS:
            return gloss()
