

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CoverRole(enum.StrEnum):
    COVER = "cover"
    RELIEF = "relief"

    def visit(self, cover: typing.Callable[[], T_Result], relief: typing.Callable[[], T_Result]) -> T_Result:
        if self is CoverRole.COVER:
            return cover()
        if self is CoverRole.RELIEF:
            return relief()
