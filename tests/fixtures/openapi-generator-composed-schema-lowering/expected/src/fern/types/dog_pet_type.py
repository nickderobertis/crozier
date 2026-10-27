

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DogPetType(enum.StrEnum):
    DOG = "dog"

    def visit(self, dog: typing.Callable[[], T_Result]) -> T_Result:
        if self is DogPetType.DOG:
            return dog()
