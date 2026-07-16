

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetCreateStackRequestOnFailure(enum.StrEnum):
    DO_NOTHING = "DO_NOTHING"
    ROLLBACK = "ROLLBACK"
    DELETE = "DELETE"

    def visit(
        self,
        do_nothing: typing.Callable[[], T_Result],
        rollback: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetCreateStackRequestOnFailure.DO_NOTHING:
            return do_nothing()
        if self is GetCreateStackRequestOnFailure.ROLLBACK:
            return rollback()
        if self is GetCreateStackRequestOnFailure.DELETE:
            return delete()
