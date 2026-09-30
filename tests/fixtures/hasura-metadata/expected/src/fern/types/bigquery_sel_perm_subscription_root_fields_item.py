

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BigquerySelPermSubscriptionRootFieldsItem(enum.StrEnum):
    SELECT = "select"
    SELECT_BY_PK = "select_by_pk"
    SELECT_AGGREGATE = "select_aggregate"
    SELECT_STREAM = "select_stream"

    def visit(
        self,
        select: typing.Callable[[], T_Result],
        select_by_pk: typing.Callable[[], T_Result],
        select_aggregate: typing.Callable[[], T_Result],
        select_stream: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BigquerySelPermSubscriptionRootFieldsItem.SELECT:
            return select()
        if self is BigquerySelPermSubscriptionRootFieldsItem.SELECT_BY_PK:
            return select_by_pk()
        if self is BigquerySelPermSubscriptionRootFieldsItem.SELECT_AGGREGATE:
            return select_aggregate()
        if self is BigquerySelPermSubscriptionRootFieldsItem.SELECT_STREAM:
            return select_stream()
