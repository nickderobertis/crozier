

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TypesAnimalZeroAnimal(str, enum.Enum):
    DOG = "dog"

    def visit(self, dog: typing.Callable[[], T_Result]) -> T_Result:
        if self is TypesAnimalZeroAnimal.DOG:
            return dog()
