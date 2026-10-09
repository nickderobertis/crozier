

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SeedlingMethod(enum.StrEnum):
    SEEDLING = "seedling"

    def visit(self, seedling: typing.Callable[[], T_Result]) -> T_Result:
        if self is SeedlingMethod.SEEDLING:
            return seedling()
