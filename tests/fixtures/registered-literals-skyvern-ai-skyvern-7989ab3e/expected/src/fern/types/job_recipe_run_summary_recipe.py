

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobRecipeRunSummaryRecipe(enum.StrEnum):
    APPLY = "apply"
    EXTRACT = "extract"

    def visit(self, apply: typing.Callable[[], T_Result], extract: typing.Callable[[], T_Result]) -> T_Result:
        if self is JobRecipeRunSummaryRecipe.APPLY:
            return apply()
        if self is JobRecipeRunSummaryRecipe.EXTRACT:
            return extract()
