

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemIdTwo(enum.StrEnum):
    PITR7 = "pitr_7"
    PITR14 = "pitr_14"
    PITR28 = "pitr_28"

    def visit(
        self,
        pitr7: typing.Callable[[], T_Result],
        pitr14: typing.Callable[[], T_Result],
        pitr28: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemIdTwo.PITR7:
            return pitr7()
        if self is ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemIdTwo.PITR14:
            return pitr14()
        if self is ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemIdTwo.PITR28:
            return pitr28()
