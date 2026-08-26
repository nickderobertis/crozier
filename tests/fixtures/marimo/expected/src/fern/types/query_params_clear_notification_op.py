

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryParamsClearNotificationOp(enum.StrEnum):
    QUERY_PARAMS_CLEAR = "query-params-clear"

    def visit(self, query_params_clear: typing.Callable[[], T_Result]) -> T_Result:
        if self is QueryParamsClearNotificationOp.QUERY_PARAMS_CLEAR:
            return query_params_clear()
