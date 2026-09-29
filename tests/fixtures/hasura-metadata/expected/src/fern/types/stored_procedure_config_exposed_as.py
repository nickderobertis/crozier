

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StoredProcedureConfigExposedAs(enum.StrEnum):
    QUERY = "query"

    def visit(self, query: typing.Callable[[], T_Result]) -> T_Result:
        if self is StoredProcedureConfigExposedAs.QUERY:
            return query()
