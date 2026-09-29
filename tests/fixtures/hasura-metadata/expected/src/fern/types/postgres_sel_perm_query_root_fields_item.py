

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostgresSelPermQueryRootFieldsItem(enum.StrEnum):
    SELECT = "select"
    SELECT_BY_PK = "select_by_pk"
    SELECT_AGGREGATE = "select_aggregate"

    def visit(
        self,
        select: typing.Callable[[], T_Result],
        select_by_pk: typing.Callable[[], T_Result],
        select_aggregate: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostgresSelPermQueryRootFieldsItem.SELECT:
            return select()
        if self is PostgresSelPermQueryRootFieldsItem.SELECT_BY_PK:
            return select_by_pk()
        if self is PostgresSelPermQueryRootFieldsItem.SELECT_AGGREGATE:
            return select_aggregate()
