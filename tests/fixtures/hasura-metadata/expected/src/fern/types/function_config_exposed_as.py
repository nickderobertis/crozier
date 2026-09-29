

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionConfigExposedAs(enum.StrEnum):
    QUERY = "query"
    MUTATION = "mutation"

    def visit(self, query: typing.Callable[[], T_Result], mutation: typing.Callable[[], T_Result]) -> T_Result:
        if self is FunctionConfigExposedAs.QUERY:
            return query()
        if self is FunctionConfigExposedAs.MUTATION:
            return mutation()
