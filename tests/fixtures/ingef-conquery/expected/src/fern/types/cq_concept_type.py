

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CqConceptType(enum.StrEnum):
    CONCEPT = "CONCEPT"

    def visit(self, concept: typing.Callable[[], T_Result]) -> T_Result:
        if self is CqConceptType.CONCEPT:
            return concept()
