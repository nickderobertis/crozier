

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ShipParcelRequestService(enum.StrEnum):
    STANDARD = "standard"
    EXPRESS = "express"

    def visit(self, standard: typing.Callable[[], T_Result], express: typing.Callable[[], T_Result]) -> T_Result:
        if self is ShipParcelRequestService.STANDARD:
            return standard()
        if self is ShipParcelRequestService.EXPRESS:
            return express()
