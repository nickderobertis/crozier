

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryParamsAppendNotificationOp(enum.StrEnum):
    QUERY_PARAMS_APPEND = "query-params-append"

    def visit(self, query_params_append: typing.Callable[[], T_Result]) -> T_Result:
        if self is QueryParamsAppendNotificationOp.QUERY_PARAMS_APPEND:
            return query_params_append()
