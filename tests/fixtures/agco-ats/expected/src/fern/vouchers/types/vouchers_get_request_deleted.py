

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class VouchersGetRequestDeleted(enum.StrEnum):
    NOT_DELETED = "NotDeleted"
    DELETED = "Deleted"
    ALL = "All"

    def visit(
        self,
        not_deleted: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VouchersGetRequestDeleted.NOT_DELETED:
            return not_deleted()
        if self is VouchersGetRequestDeleted.DELETED:
            return deleted()
        if self is VouchersGetRequestDeleted.ALL:
            return all_()
