

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TypesAnimalOneAnimal(str, enum.Enum):
    CAT = "cat"

    def visit(self, cat: typing.Callable[[], T_Result]) -> T_Result:
        if self is TypesAnimalOneAnimal.CAT:
            return cat()
