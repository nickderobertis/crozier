

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class ListSacksRequestPriority(enum.StrEnum):
    STANDARD = "standard"
    EXPRESS = "express"

    def visit(self, standard: typing.Callable[[], T_Result], express: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListSacksRequestPriority.STANDARD:
            return standard()
        if self is ListSacksRequestPriority.EXPRESS:
            return express()
