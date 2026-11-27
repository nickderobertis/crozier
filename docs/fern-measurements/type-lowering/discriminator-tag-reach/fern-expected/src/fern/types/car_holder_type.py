

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CarHolderType(enum.StrEnum):
    CAR = "CAR"

    def visit(self, car: typing.Callable[[], T_Result]) -> T_Result:
        if self is CarHolderType.CAR:
            return car()
