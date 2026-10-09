

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Mordant(enum.StrEnum):
    ALUM = "alum"
    IRON = "iron"
    TIN = "tin"

    def visit(
        self,
        alum: typing.Callable[[], T_Result],
        iron: typing.Callable[[], T_Result],
        tin: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Mordant.ALUM:
            return alum()
        if self is Mordant.IRON:
            return iron()
        if self is Mordant.TIN:
            return tin()
