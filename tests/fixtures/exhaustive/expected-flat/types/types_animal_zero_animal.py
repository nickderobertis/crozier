

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TypesAnimalZeroAnimal(enum.StrEnum):
    DOG = "dog"

    def visit(self, dog: typing.Callable[[], T_Result]) -> T_Result:
        if self is TypesAnimalZeroAnimal.DOG:
            return dog()
