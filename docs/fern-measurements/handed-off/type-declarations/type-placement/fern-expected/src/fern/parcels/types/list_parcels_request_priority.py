

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListParcelsRequestPriority(enum.StrEnum):
    STANDARD = "standard"
    EXPRESS = "express"

    def visit(self, standard: typing.Callable[[], T_Result], express: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListParcelsRequestPriority.STANDARD:
            return standard()
        if self is ListParcelsRequestPriority.EXPRESS:
            return express()
