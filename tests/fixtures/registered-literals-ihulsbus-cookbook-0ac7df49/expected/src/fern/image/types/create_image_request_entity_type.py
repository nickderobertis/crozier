

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateImageRequestEntityType(enum.StrEnum):
    RECIPE = "recipe"
    INGREDIENT = "ingredient"

    def visit(self, recipe: typing.Callable[[], T_Result], ingredient: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateImageRequestEntityType.RECIPE:
            return recipe()
        if self is CreateImageRequestEntityType.INGREDIENT:
            return ingredient()
