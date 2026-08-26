

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryParamsSetNotificationOp(enum.StrEnum):
    QUERY_PARAMS_SET = "query-params-set"

    def visit(self, query_params_set: typing.Callable[[], T_Result]) -> T_Result:
        if self is QueryParamsSetNotificationOp.QUERY_PARAMS_SET:
            return query_params_set()
