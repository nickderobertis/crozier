

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConceptQueryType(enum.StrEnum):
    CONCEPT_QUERY = "CONCEPT_QUERY"

    def visit(self, concept_query: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConceptQueryType.CONCEPT_QUERY:
            return concept_query()
