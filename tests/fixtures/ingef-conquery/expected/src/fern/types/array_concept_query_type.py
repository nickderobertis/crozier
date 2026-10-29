

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ArrayConceptQueryType(enum.StrEnum):
    ARRAY_CONCEPT_QUERY = "ARRAY_CONCEPT_QUERY"

    def visit(self, array_concept_query: typing.Callable[[], T_Result]) -> T_Result:
        if self is ArrayConceptQueryType.ARRAY_CONCEPT_QUERY:
            return array_concept_query()
