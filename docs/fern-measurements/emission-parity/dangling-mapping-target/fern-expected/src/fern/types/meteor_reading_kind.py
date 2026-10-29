

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MeteorReadingKind(enum.StrEnum):
    METEOR = "METEOR"

    def visit(self, meteor: typing.Callable[[], T_Result]) -> T_Result:
        if self is MeteorReadingKind.METEOR:
            return meteor()
