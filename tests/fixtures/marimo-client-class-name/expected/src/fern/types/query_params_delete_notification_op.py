

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryParamsDeleteNotificationOp(enum.StrEnum):
    QUERY_PARAMS_DELETE = "query-params-delete"

    def visit(self, query_params_delete: typing.Callable[[], T_Result]) -> T_Result:
        if self is QueryParamsDeleteNotificationOp.QUERY_PARAMS_DELETE:
            return query_params_delete()
