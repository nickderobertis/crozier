

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryType(enum.StrEnum):
    """
    Specifies the default QueryType: The following query types are supported:
    - **Union** (OR, disjunction),
    - **Intersection** (AND, conjunction),
    - **Phrase** (""),
    - **Not** (-).

    The default QueryType is superseded if the query parser detects that a different query type is specified within the query string (+ - "").
    """

    UNION = "Union"
    INTERSECTION = "Intersection"
    PHRASE = "Phrase"
    NOT = "Not"

    def visit(
        self,
        union: typing.Callable[[], T_Result],
        intersection: typing.Callable[[], T_Result],
        phrase: typing.Callable[[], T_Result],
        not_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is QueryType.UNION:
            return union()
        if self is QueryType.INTERSECTION:
            return intersection()
        if self is QueryType.PHRASE:
            return phrase()
        if self is QueryType.NOT:
            return not_()
