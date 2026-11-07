

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CatPetType(enum.StrEnum):
    CAT = "cat"

    def visit(self, cat: typing.Callable[[], T_Result]) -> T_Result:
        if self is CatPetType.CAT:
            return cat()
